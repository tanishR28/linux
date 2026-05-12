# Prior Probabilities
P_spam = 0.5
P_ham = 0.5

# Word Probabilities
offer_spam = 0.8
win_spam = 0.7

offer_ham = 0.2
win_ham = 0.1

# Test Sentence: "offer win"

# Naive Bayes Calculation
spam_prob = P_spam * offer_spam * win_spam

ham_prob = P_ham * offer_ham * win_ham

print("Spam Probability:", spam_prob)
print("Ham Probability:", ham_prob)

# Classification
if spam_prob > ham_prob:
    print("Sentence is SPAM")
else:
    print("Sentence is HAM")


#better


# Training Data
spam_messages = [
    "win money now",
    "limited time offer",
    "win a free prize"
]

ham_messages = [
    "let us meet tomorrow",
    "project meeting today",
    "how are you"
]

# Test Sentence
test = "win offer"

# Tokenization
spam_words = " ".join(spam_messages).split()
ham_words = " ".join(ham_messages).split()

test_words = test.split()

# Prior Probabilities
total_msgs = len(spam_messages) + len(ham_messages)

P_spam = len(spam_messages) / total_msgs
P_ham = len(ham_messages) / total_msgs

# Initial probabilities
spam_prob = P_spam
ham_prob = P_ham

# Naive Bayes Calculation
for w in test_words:

    # Laplace smoothing
    spam_count = spam_words.count(w) + 1
    ham_count = ham_words.count(w) + 1

    spam_prob *= spam_count / len(spam_words)
    ham_prob *= ham_count / len(ham_words)

print("Spam Probability:", round(spam_prob, 5))
print("Ham Probability:", round(ham_prob, 5))

# Classification
if spam_prob > ham_prob:
    print("Sentence is SPAM")
else:
    print("Sentence is HAM")