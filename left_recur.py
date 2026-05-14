# Left Recursion Removal

grammar = {}

n = int(input("Enter number of productions: "))

print("Enter productions:")

# INPUT
for i in range(n):

    rule = input()

    left, right = rule.split("->")

    grammar[left] = right.split("|")


print("\nGrammar after removing left recursion:\n")

# PROCESS EACH NON-TERMINAL
for nt in grammar:

    alpha = []   # recursive part
    beta = []    # non-recursive part

    for prod in grammar[nt]:

        # Left recursive production
        if prod[0] == nt:

            alpha.append(prod[1:])

        else:
            beta.append(prod)

    # Left recursion exists
    if alpha:

        new_nt = nt + "'"

        # A -> βA'
        print(nt, "->", end=" ")

        for i in range(len(beta)):

            print(beta[i] + new_nt, end="")

            if i != len(beta) - 1:
                print(" | ", end="")

        print()

        # A' -> αA' | e
        print(new_nt, "->", end=" ")

        for i in range(len(alpha)):

            print(alpha[i] + new_nt, end=" | ")

        print("e")

    else:
        # No left recursion
        print(nt, "->", " | ".join(grammar[nt]))