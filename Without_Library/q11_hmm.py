# Transition Probabilities
transition = {
    "Noun->Verb": 0.4,
    "Verb->Noun": 0.6
}

# Emission Probabilities
emission = {
    "Noun->dog": 0.5,
    "Verb->barks": 0.8
}

print("Transition Probabilities:")
for k, v in transition.items():
    print(k, "=", v)

print("\nEmission Probabilities:")
for k, v in emission.items():
    print(k, "=", v)