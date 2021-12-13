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

    T = [[dict() for j in range(n)] for i in range(n)]

    for i in range(n):

        # Prechádzam pravidlá
        for l, rule in R.items():
            for r in rule:

                # Ak nájdem terminál
                if len(r) == 1 and r[0] == w[i]:
                    T[0][i][l] = 1

    for i in range(n - 1):
        combinations = get_combinations(i + 2)

        for j in range(n - 1 - i):
            for comb in combinations:
                # comb reprezentuje jedno možné rozdelenie slova - napr. n = 3, tak comb[0] = 2, comb[1] = 1
                # takže viem že hľadám kombináciu podslov dĺžky 2 a 1
                # podslovo dĺžky 2 je v druhom riadku (indexujem od 0, takže index 1, preto - 1)
                # podslovo dĺžky 1 je v prvom riadku (indexujem od 0, takže 0,  preto - 1) a
                # + comb[0], pretože slovo začne v stĺpci tohto indexu
                for x in T[comb[0] - 1][j]:
                    for y in T[comb[1] - 1][j + comb[0]]:
                        # Prechádzam pravidlá
                        for l, rule in R.items():
                            for r in rule:
                                if len(r) == 2 and r[0] == x and r[1] == y:
                                    dt_count = T[comb[0] - 1][j].get(x) * T[comb[1] - 1][j + comb[0]].get(y)
                                    T[i + 1][j][l] = T[i + 1][j].get(l, 0) + dt_count

    for i in range(n - 1, -1, -1):
        print(T[i])


# Symboly
non_terminals = ["S", "A", "B", "C"]
terminals = ["a", "b"]

# Pravidlá
R = {
    "S": [["A", "B"], ["B", "C"]],
    "A": [["B", "A"], ["a"]],
    "B": [["C", "C"], ["b"]],
    "C": [["A", "B"], ["a"]]
}

# Slovo
w = "baaba"

# Volanie algoritmu
cykParse(w)
