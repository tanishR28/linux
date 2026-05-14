# Assembler Experiment — Full Concept Explanation

This experiment is about simulating basic working of an assembler.

Your syllabus asks: 

```text id="q1m8vc"
Generate:
1. H Record
2. E Record
3. Symbol Table
```

from an assembly language program.

---

# What Is an Assembler?

Assembler converts:

```text id="w4q7pk"
Assembly Language
        ↓
Machine/Object Code
```

Example:

```asm id="m9t2vr"
LDA NUM
ADD ONE
```

gets converted into machine instructions.

---

# Main Concepts Used

Your experiment mainly uses:

| Concept      | Purpose                     |
| ------------ | --------------------------- |
| LOCCTR       | Tracks memory address       |
| Symbol Table | Stores labels and addresses |
| H Record     | Program information         |
| E Record     | Execution start address     |

---

# INPUT OF YOUR PROGRAM

Your code input is:

```python id="x6m3lc"
program = [

    "COPY START 1000",
    "A LDA NUM",
    "B ADD ONE",
    "NUM WORD 5",
    "ONE WORD 1",
    "END"
]
```

This is an assembly program.

---

# Understanding Input Line by Line

---

# 1. START Directive

```text id="r8q1pk"
COPY START 1000
```

Meaning:

* Program name = `COPY`
* Starting memory address = `1000`

So:

```text id="v5m9tr"
LOCCTR = 1000
```

---

# 2. Instruction

```text id="n2q7vc"
A LDA NUM
```

Meaning:

* Label = `A`
* Opcode = `LDA`
* Operand = `NUM`

---

# 3. Another Instruction

```text id="f7m4pk"
B ADD ONE
```

Meaning:

* Label = `B`
* Opcode = `ADD`
* Operand = `ONE`

---

# 4. Data Declaration

```text id="k3q8tr"
NUM WORD 5
```

Meaning:

* variable `NUM`
* value = 5

---

# 5. Another Variable

```text id="p9m1vc"
ONE WORD 1
```

---

# 6. END Directive

```text id="t4q6pk"
END
```

Program ends.

---

# What Is LOCCTR?

LOCCTR means:

```text id="y7m2tr"
Location Counter
```

It stores:

```text id="g1q9vc"
current memory address
```

VERY IMPORTANT concept.

---

# LOCCTR Flow in Your Program

---

# Initial

```text id="d5m8pk"
START 1000
```

So:

```text id="j2q4tr"
LOCCTR = 1000
```

---

# A LDA NUM

Instruction size assumed:

```text id="m6v1lc"
3 bytes
```

Store:

```text id="r9q7pk"
A → 1000
```

Then:

```text id="x3m2tr"
LOCCTR = 1003
```

---

# B ADD ONE

Store:

```text id="f8q5vc"
B → 1003
```

Then:

```text id="n1m9pk"
LOCCTR = 1006
```

---

# NUM WORD 5

Store:

```text id="q4v7tr"
NUM → 1006
```

Then:

```text id="u8m3lc"
LOCCTR = 1009
```

---

# ONE WORD 1

Store:

```text id="z2q6pk"
ONE → 1009
```

Then:

```text id="h5m1tr"
LOCCTR = 100C
```

(hexadecimal increment)

---

# SYMBOL TABLE

Main purpose:

```text id="c9q4vc"
store labels and addresses
```

---

# Final Symbol Table

| Symbol | Value |
| ------ | ----- |
| A      | 1000  |
| B      | 1003  |
| NUM    | 1006  |
| ONE    | 1009  |

---

# How Code Creates Symbol Table

This line:

```python id="p3m8pk"
symbol_table[label] = hex(locctr)[2:].upper()
```

Stores:

```text id="w7q1tr"
label → current address
```

---

# H RECORD CONCEPT

H means:

```text id="b4m9vc"
Header Record
```

Format:

```text id="k8q2pk"
H^ProgramName^StartAddress^ProgramLength
```

---

# In Your Program

```text id="r1m6tr"
H^COPY^001000^00000C
```

---

# Meaning

| Part   | Meaning        |
| ------ | -------------- |
| COPY   | Program name   |
| 001000 | Start address  |
| 00000C | Program length |

---

# Program Length

Calculated by:

```python id="x5q7vc"
program_length = locctr - start_address
```

---

# Example

```text id="g9m3pk"
100C - 1000 = 000C
```

(hexadecimal)

---

# E RECORD CONCEPT

E means:

```text id="m2q8tr"
End Record
```

Format:

```text id="v6m1lc"
E^StartExecutionAddress
```

---

# Your Output

```text id="t9q4pk"
E^001000
```

Meaning:

```text id="y3m7tr"
execution starts from address 1000
```

---

# FINAL OUTPUT OF YOUR CODE

---

# H Record

```text id="d8q1vc"
H^COPY^001000^00000C
```

---

# E Record

```text id="j4m9pk"
E^001000
```

---

# Symbol Table

```text id="q7v2tr"
Symbol   Value

A        1000
B        1003
NUM      1006
ONE      1009
```

---

# WHY HEXADECIMAL USED?

Memory addresses are usually represented in:

```text id="x1m5lc"
hexadecimal
```

because:

* compact
* easy binary conversion

---

# MOST IMPORTANT VIVA QUESTIONS

---

# What is assembler?

Converts assembly language into machine code.

---

# What is LOCCTR?

Tracks current memory location.

---

# What is Symbol Table?

Stores:

```text id="c6q9pk"
label → address
```

---

# What is H Record?

Contains:

* program name
* start address
* program length

---

# What is E Record?

Contains execution start address.

---

# Why symbol table needed?

To resolve label addresses during translation.

---

# MOST IMPORTANT UNDERSTANDING

Your code is mainly simulating:

```text id="n8m2tr"
PASS 1 OF ASSEMBLER
```

because:

* building symbol table
* assigning addresses

Actual machine code generation is NOT done here.

---

# Real Assembler Has 2 Passes

| Pass   | Work                     |
| ------ | ------------------------ |
| Pass 1 | Symbol table + addresses |
| Pass 2 | Generate machine code    |

Your experiment mostly focuses on:

```text id="r5q1vc"
PASS 1
```
