import re

text = "Hello!!! NLP 2025 is FUN."

# Convert to lowercase
text = text.lower()

# Remove numbers
text = re.sub(r'\d+', '', text)

# Remove punctuation
text = re.sub(r'[^\w\s]', '', text)

# Remove extra spaces
text = " ".join(text.split())

print("Cleaned Text:")
print(text)


