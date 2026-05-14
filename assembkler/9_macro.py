# Macro Processor
# Generate NAMETAB and DEFTAB

# ---------------- INPUT PROGRAM ----------------

program = [

    "MACRO INCR &P1,&P2",
    "LDA &P1",
    "ADD &P2",
    "STA &P1",
    "MEND",

    "MACRO SUBR &A,&B",
    "LDA &A",
    "SUB &B",
    "STA &A",
    "MEND",

    "START",
    "INCR A,B",
    "SUBR X,Y",
    "END"
]


# ---------------- TABLES ----------------

NAMETAB = []
DEFTAB = []


# ---------------- PROCESS ----------------

i = 0

while i < len(program):

    line = program[i]

    # MACRO FOUND
    if line.startswith("MACRO"):
        parts = line.split()
        macro_name = parts[1]

        start_index = len(DEFTAB)

        # store header in DEFTAB
        DEFTAB.append(line)

        i += 1

        # store macro body
        while program[i] != "MEND":

            DEFTAB.append(program[i])

            i += 1

        DEFTAB.append("MEND")

        end_index = len(DEFTAB) - 1

        # store in NAMETAB
        NAMETAB.append([
            macro_name,
            start_index,
            end_index
        ])

    i += 1


# ---------------- DISPLAY NAMETAB ----------------

print("\nNAMETAB\n")
print("Macro Name\tStart\tEnd")
for row in NAMETAB:
    print(row[0],"\t\t",row[1],"\t",row[2])


# ---------------- DISPLAY DEFTAB ----------------

print("\nDEFTAB\n")
for i in range(len(DEFTAB)):
    print(i,"\t",DEFTAB[i])




# For the Macro Processor experiment (`9_macro.py`), running is very easy because it’s just a normal Python program.

# ---

# # Step 1 — Save File

# Create file:

# ```text id="q1m7pk"
# 9_macro.py
# ```

# Paste your macro processor code inside it.

# ---

# # Step 2 — Open Terminal in Folder

# Example:

# ```bash id="v4q9tr"
# cd ~/Desktop/spcc
# ```

# (or wherever your file exists)

# ---

# # Step 3 — Run Python Program

# ```bash id="r8m2vc"
# python3 9_macro.py
# ```

# ---

# # If Your Code Uses Hardcoded Input

# Example:

# ```python id="x5q1pk"
# program = [
#     "MACRO",
#     "INCR",
#     "LOAD A",
#     "ADD B",
#     "STORE C",
#     "MEND",
#     "START",
#     "INCR",
#     "END"
# ]
# ```

# Then simply running:

# ```bash id="n9m4tr"
# python3 9_macro.py
# ```

# will directly show output.

# ---

# # Expected Output

# Example:

# ```text id="f3q8vc"
# MNT

# INCR -> 0

# MDT

# 0 LOAD A
# 1 ADD B
# 2 STORE C

# Expanded Code

# START
# LOAD A
# ADD B
# STORE C
# END
# ```

# ---

# # If You Want Input From File

# Create:

# ```text id="k6m1pk"
# input.txt
# ```

# Example content:

# ```text id="p2q7tr"
# MACRO
# INCR
# LOAD A
# ADD B
# STORE C
# MEND

# START
# INCR
# END
# ```

# ---

# # Then Modify Code

# Replace hardcoded list with:

# ```python id="t8m4vc"
# with open("input.txt") as f:
#     program = [line.strip() for line in f]
# ```

# ---

# # Then Run

# ```bash id="w1q9pk"
# python3 9_macro.py
# ```

# ---

# # Recommended for ESE

# Use:

# ```text id="d5m2tr"
# hardcoded input list
# ```

# because:

# * shorter
# * easier
# * fewer runtime errors

# ---

# # Check Python Installed

# If:

# ```bash id="j9q6vc"
# python3 9_macro.py
# ```

# doesn’t work:

# check:

# ```bash id="x3m8pk"
# python3 --version
# ```

# ---

# # If Python Missing

# Install:

# ```bash id="g7q1tr"
# sudo apt install python3
# ```

# Usually already installed on Ubuntu.

# ---

# # Final Commands

# ```bash id="m4q9vc"
# cd folder_name

# python3 9_macro.py
# ```

# That’s all.
