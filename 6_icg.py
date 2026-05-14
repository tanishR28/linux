# Intermediate Code Generation
# Infix to Postfix + Quadruple + Triple

operators = ['+', '-', '*', '/', '=']
precedence = {
    '=': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}
# ---------- INFIX TO POSTFIX ----------

def infix_to_postfix(expr):
    output = []
    stack = []

    for ch in expr:
        if ch.isalnum():          # operand
            output.append(ch)

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()           # remove '('

        elif ch in operators:
            while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[ch]:
                output.append(stack.pop())
            stack.append(ch)

    while stack:
        output.append(stack.pop())

    return output


# ---------- GENERATE QUADRUPLE AND TRIPLE ----------

def generate_icg(postfix):
    stack = []
    quadruple = []
    triple = []
    temp_count = 1

    for symbol in postfix:
        if symbol not in operators:
            stack.append(symbol)

        else:
            op2 = stack.pop()
            op1 = stack.pop()

            temp = "T" + str(temp_count)

            # Quadruple: operator, arg1, arg2, result
            quadruple.append([symbol, op1, op2, temp])

            # Triple: operator, arg1, arg2
            t_op1 = op1
            t_op2 = op2

            if op1.startswith("T"):
                t_op1 = "(" + str(int(op1[1:]) - 1) + ")"

            if op2.startswith("T"):
                t_op2 = "(" + str(int(op2[1:]) - 1) + ")"

            triple.append([symbol, t_op1, t_op2])

            stack.append(temp)
            temp_count += 1

    return quadruple, triple


# ---------- INPUT ----------

choice = input("Enter expression type (infix/postfix): ").lower()

if choice == "infix":
    expr = input("Enter infix expression: ")
    postfix = infix_to_postfix(expr)
else:
    postfix = input("Enter postfix expression with spaces: ").split()


# ---------- OUTPUT POSTFIX ----------

print("\nPostfix Expression:")
print(" ".join(postfix))


# ---------- ICG OUTPUT ----------

quadruple, triple = generate_icg(postfix)


print("\nQuadruple Representation:\n")
print("Operator\tArg1\tArg2\tResult")

for op, arg1, arg2, result in quadruple:
    print(op, "\t\t", arg1, "\t", arg2, "\t", result)


print("\nTriple Representation:\n")
print("Index\tOperator\tArg1\tArg2")

for i, row in enumerate(triple):
    print(i, "\t", row[0], "\t\t", row[1], "\t", row[2])












# # Intermediate Code Generation
# # Infix to Postfix / Prefix + Quadruple + Triple

# operators = ['+', '-', '*', '/', '^']

# precedence = {
#     '+': 1,
#     '-': 1,
#     '*': 2,
#     '/': 2,
#     '^': 3
# }

# # ---------- INFIX TO POSTFIX ----------

# def infix_to_postfix(expr):

#     stack = []
#     output = []

#     for ch in expr:

#         if ch.isalnum():
#             output.append(ch)

#         elif ch == '(':
#             stack.append(ch)

#         elif ch == ')':

#             while stack[-1] != '(':
#                 output.append(stack.pop())

#             stack.pop()

#         else:

#             while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[ch]:

#                 output.append(stack.pop())

#             stack.append(ch)

#     while stack:
#         output.append(stack.pop())

#     return "".join(output)


# # ---------- INFIX TO PREFIX ----------

# def infix_to_prefix(expr):

#     expr = expr[::-1]

#     temp = ""

#     for ch in expr:

#         if ch == '(':
#             temp += ')'

#         elif ch == ')':
#             temp += '('

#         else:
#             temp += ch

#     postfix = infix_to_postfix(temp)

#     prefix = postfix[::-1]

#     return prefix


# # ---------- QUADRUPLE + TRIPLE ----------

# def generate_icg(postfix):

#     stack = []

#     quadruple = []

#     triple = []

#     temp_count = 1

#     for ch in postfix:

#         if ch.isalnum():

#             stack.append(ch)

#         else:

#             op2 = stack.pop()

#             op1 = stack.pop()

#             temp = "T" + str(temp_count)

#             quadruple.append([ch, op1, op2, temp])

#             t1 = op1
#             t2 = op2

#             if op1.startswith("T"):
#                 t1 = "(" + str(int(op1[1:]) - 1) + ")"

#             if op2.startswith("T"):
#                 t2 = "(" + str(int(op2[1:]) - 1) + ")"

#             triple.append([ch, t1, t2])

#             stack.append(temp)

#             temp_count += 1

#     return quadruple, triple


# # ---------- INPUT ----------

# expr = input("Enter infix expression: ")

# # ---------- CONVERSIONS ----------

# postfix = infix_to_postfix(expr)

# prefix = infix_to_prefix(expr)

# print("\nPostfix Expression:", postfix)

# print("Prefix Expression :", prefix)

# # ---------- ICG ----------

# quadruple, triple = generate_icg(postfix)

# # ---------- QUADRUPLE ----------

# print("\nQuadruple Representation:\n")

# print("Op\tArg1\tArg2\tResult")

# for row in quadruple:

#     print(row[0], "\t", row[1], "\t", row[2], "\t", row[3])

# # ---------- TRIPLE ----------

# print("\nTriple Representation:\n")

# print("Index\tOp\tArg1\tArg2")

# for i, row in enumerate(triple):

#     print(i, "\t", row[0], "\t", row[1], "\t", row[2])