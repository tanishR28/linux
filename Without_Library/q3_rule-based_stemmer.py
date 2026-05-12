words = ["playing", "worked", "quickly", "boxes", "cats"]

for w in words:

    # Rule-based stemming
    if w.endswith("ing"):
        stem = w[:-3]

    elif w.endswith("ed"):
        stem = w[:-2]

    elif w.endswith("ly"):
        stem = w[:-2]

    elif w.endswith("es"):
        stem = w[:-2]

    elif w.endswith("s"):
        stem = w[:-1]

    else:
        stem = w

    print(w, "->", stem)