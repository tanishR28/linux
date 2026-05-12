sentence = "Sachin lives in Mumbai and works at Google"

words = sentence.split()

for w in words:

    # Simple NER Rule
    if w[0].isupper():

        if w in ["Mumbai", "Delhi", "India"]:
            tag = "Location"

        elif w in ["Google", "Microsoft"]:
            tag = "Organization"

        else:
            tag = "Person"

        print(w, "->", tag)