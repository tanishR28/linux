# SIC Assembler
# H Record, E Record and Symbol Table

program = [
    "PG2 START 1000",
    "JMP ADD1",
    "JMP ADD2",
    "ADD1 LDA #1020",
    "STA #3040",
    "ADD2 LDA #1004",
    "DATA1 BYTE C='ABC'",
    "DATA2 EQU 10",
    "END"
]

opcodes = ["LDA", "STA", "JMP"]
symbol_table = {}
start_address = 0
location_counter = 0
program_name = ""


def to_hex(value, width=6):
    return hex(value)[2:].upper().zfill(width)


# ---------- PASS 1 ----------

for line in program:
    words = line.split()

    if words[0] == "END":
        break

    if "START" in words:
        program_name = words[0]
        start_address = int(words[2], 16)
        location_counter = start_address
        continue

    label = ""

    if words[0] not in opcodes and words[0] not in ["BYTE", "EQU"]:
        label = words[0]
        words = words[1:]

    mnemonic = words[0]
    operand = words[1] if len(words) > 1 else ""

    if label:
        if mnemonic == "EQU":
            symbol_table[label] = operand
        else:
            symbol_table[label] = to_hex(location_counter, 4)

    if mnemonic in opcodes:
        location_counter += 3
    elif mnemonic == "BYTE":
        value = operand.split("'")[1]
        location_counter += len(value)


# ---------- RECORDS ----------

program_length = location_counter - start_address

header = f"H^{program_name}^{to_hex(start_address)}^{to_hex(program_length)}"
end_record = f"E^{to_hex(start_address)}"


# ---------- OUTPUT ----------

print("\nH RECORD\n")
print(header)

print("\nE RECORD\n")
print(end_record)

print("\nSYMBOL TABLE\n")
print("Symbol Name\tValue")

for symbol, value in symbol_table.items():
    print(symbol, "\t\t", value)

    