sentences = [
    "I saw the man with a telescope",
    "The chicken is ready to eat",
    "He went to the bank",
    "She saw a bat"
]

for s in sentences:

    words = s.split()

    # Syntactic Ambiguity
    if "with" in words or "eat" in words:
        print(s)
        print("-> Syntactic Ambiguity\n")

    # Semantic Ambiguity
    elif "bank" in words or "bat" in words:
        print(s)
        print("-> Semantic Ambiguity\n")