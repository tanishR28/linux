import nltk

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "Rahul is running quickly in a beautiful garden"

words = nltk.word_tokenize(sentence)

# POS Tagging
tags = nltk.pos_tag(words)

print(tags)