def get_combinations(word_len):
    my_list = []

    if word_len == 2:
        my_list.append([1, 1])

    for i in range(2, word_len):
        mod = word_len % i

        if mod + i == word_len:
            if mod == 0:
                my_list.append([i, i])
            else:
                my_list.append([mod, i])
                my_list.append([i, mod])

    return my_list


def cykParse(word):
    word = list(word)
    n = len(word)

    # Initialize the table
    T = [[dict() for j in range(n)] for i in range(n)]

    # Filling in the table
    for i in range(n):

        # Iterate over the rules
        for l, rule in R.items():
            for r in rule:

                # If a terminal is found
                if len(r) == 1 and r[0] == w[i]:
                    T[0][i][l] = 1

    for i in range(n - 1):
        combinations = get_combinations(i + 2)

        for j in range(n - 1 - i):
            for comb in combinations:
                # comb represents one possible divide of word - e.g. n = 3, then it can be comb[0] = 2, comb[1] = 1
                # so we know that we are looking for combination of subword of length 2 and subword of length 1
                # subword of length 2 is in second row (indexing from 0, so on index 1, that's why - 1)
                # subword of length 1 is in first row (indexing from 0, so on index 0, that's why - 1) and
                # + comb[0] because the word will continue in column of that index
                for x in T[comb[0] - 1][j]:
                    for y in T[comb[1] - 1][j + comb[0]]:
                        # Iterate over the rules
                        for l, rule in R.items():
                            for r in rule:
                                if len(r) == 2 and r[0] == x and r[1] == y:
                                    dt_count = T[comb[0] - 1][j].get(x) * T[comb[1] - 1][j + comb[0]].get(y)
                                    T[i + 1][j][l] = T[i + 1][j].get(l, 0) + dt_count

    for i in range(n - 1, -1, -1):
        print(T[i])


# Non-terminal & terminal symbols
non_terminals = ["S", "A", "B", "C"]
terminals = ["a", "b"]

# Rules of the grammar
R = {
    "S": [["A", "B"], ["B", "C"]],
    "A": [["B", "A"], ["a"]],
    "B": [["C", "C"], ["b"]],
    "C": [["A", "B"], ["a"]]
}

# Given string
w = "baaba"

# Function Call
cykParse(w)
