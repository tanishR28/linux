from nltk.translate.bleu_score import sentence_bleu

# Reference Sentence
reference = [["I", "love", "NLP"]]

# Candidate Sentence
candidate = ["I", "love", "AI"]

# BLEU Score
score = sentence_bleu(reference, candidate)

print("BLEU Score:", round(score, 2))