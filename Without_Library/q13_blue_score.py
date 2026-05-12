reference = "the cat is on the mat"
candidate = "the cat sat on the mat"

# Tokenization
ref_words = reference.split()
cand_words = candidate.split()

# Count matching words
match = 0

for w in cand_words:
    if w in ref_words:
        match += 1

# BLEU Score
bleu = match / len(cand_words)

print("Matching Words:", match)
print("BLEU Score:", round(bleu, 2))