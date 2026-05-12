import spacy

# Load English Model
nlp = spacy.load("en_core_web_sm")

text = "Sachin lives in Mumbai and works at Google"

doc = nlp(text)

# Named Entities
for ent in doc.ents:

    print(ent.text, "->", ent.label_)