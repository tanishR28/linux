import re

text = "Hello!!! NLP 2025 is FUN."

# Lowercase
text = text.lower()

# Remove Numbers
text = re.sub(r'\d+', '', text)

# Remove Punctuation
text = re.sub(r'[^\w\s]', '', text)

# Remove Extra Spaces
text = " ".join(text.split())

print("Cleaned Text:")
print(text)