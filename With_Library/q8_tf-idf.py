from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

text = ["NLP is easy and NLP is powerful"]

# TF-IDF
tfidf = TfidfVectorizer()

result = tfidf.fit_transform(text)

# Table Format
df = pd.DataFrame(
    result.toarray(),
    columns=tfidf.get_feature_names_out()
)

print(df)