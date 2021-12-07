# Python implementation for the
# CYK Algorithm


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


# Function to perform the CYK Algorithm
def cykParse(word):
    word = list(word)
    n = len(word)

    # Initialize the table
    T = [[dict() for j in range(n)] for i in range(n)]

    # Filling in the table
    for i in range(n):

        # Iterate over the rules
        for lhs, rule in R.items():
            for rhs in rule:

                # If a terminal is found
                if len(rhs) == 1 and rhs[0] == w[i]:
                    T[0][i][lhs] = 1

    for i in range(n - 1):
        combinations = get_combinations(i + 2)

        for j in range(n - 1 - i):
            for comb in combinations:
                for x in T[comb[0] - 1][j]:
                    for y in T[comb[1] - 1][j + comb[0]]:
                        # Iterate over the rules
                        for lhs, rule in R.items():
                            for rhs in rule:
                                if len(rhs) == 2 and rhs[0] == x and rhs[1] == y:
                                    dt_count = T[comb[0] - 1][j].get(x) * T[comb[1] - 1][j + comb[0]].get(y)
                                    T[i + 1][j][lhs] = T[i + 1][j].get(lhs, 0) + dt_count

    for i in range(n - 1, -1, -1):
        print(T[i])


# Non-terminal symbols
non_terminals = ["S", "A", "B", "C"]
terminals = ["a", "b"]
R = {
    "S": [["A", "B"], ["B", "C"]],
    "A": [["B", "A"], ["a"]],
    "B": [["C", "C"], ["b"]],
    "C": [["A", "B"], ["a"]]
}
# Rules of the grammar

# Given string
w = "baaba"

# Function Call
cykParse(w)
