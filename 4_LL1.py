# LL(1) Predictive Parser

table = {
    ('E', 'i'): 'TA',
    ('E', '('): 'TA',

    ('A', '+'): '+TA',
    ('A', ')'): 'e',
    ('A', '$'): 'e',

    ('T', 'i'): 'FB',
    ('T', '('): 'FB',

    ('B', '+'): 'e',
    ('B', '*'): '*FB',
    ('B', ')'): 'e',
    ('B', '$'): 'e',

    ('F', 'i'): 'i',
    ('F', '('): '(E)'
}


def is_non_terminal(ch):
    return ch.isupper()


def show(stack, input_string, pointer, action):
    print("".join(stack), "\t\t", input_string[pointer:], "\t\t", action)


print("\nGrammar Used:\n")
print("E -> TA")
print("A -> +TA | e")
print("T -> FB")
print("B -> *FB | e")
print("F -> (E) | i")

input_string = input("\nEnter input string: ")

if input_string[-1] != '$':
    input_string += '$'

stack = ['$', 'E']
pointer = 0

print("\n--------------------------------------------------")
print("STACK\t\tINPUT\t\tACTION")
print("--------------------------------------------------")

while stack:
    top = stack[-1]
    current = input_string[pointer]

    # Case 1: Terminal match
    if top == current:
        show(stack, input_string, pointer, "Match " + current)

        stack.pop()
        pointer += 1

        if top == '$':
            print("\nSTRING ACCEPTED")
            break

    # Case 2: Non-terminal expansion
    elif is_non_terminal(top):
        key = (top, current)

        if key not in table:
            show(stack, input_string, pointer, "ERROR")
            print("\nSTRING REJECTED")
            break

        production = table[key]
        show(stack, input_string, pointer, top + " -> " + production)

        stack.pop()

        if production != 'e':
            for symbol in reversed(production):
                stack.append(symbol)

    # Case 3: Invalid terminal
    else:
        show(stack, input_string, pointer, "ERROR")
        print("\nSTRING REJECTED")
        break