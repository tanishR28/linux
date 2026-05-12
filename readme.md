I’ll make this as clean viva-ready notes you can directly paste into a Markdown file.

# NLP Practical Viva Notes

---

# Q1. Tokenization Task

## Theory

Tokenization is the process of breaking text into smaller units called tokens.

Types:

* Sentence Tokenization → paragraph into sentences
* Word Tokenization → sentence into words

Used in:

* NLP preprocessing
* Search engines
* Chatbots

## Important Functions

| Syntax    | Purpose             |
| --------- | ------------------- |
| `split()` | split text          |
| `len()`   | count tokens        |
| `strip()` | remove extra spaces |

## Viva Points

* Token = smallest text unit
* Word tokenization splits sentence into words
* Sentence tokenization splits paragraph into sentences

---

# Q2. Stopword Removal

## Theory

Stopwords are common words that carry little meaning.

Examples:

```python
is, the, and, a, an
```

Removing stopwords:

* reduces noise
* improves NLP efficiency

## Important Concepts

* Manual stopword list
* Filtering meaningful words

## Viva Points

* Stopwords are frequently occurring words
* Used in preprocessing

---

# Q3. Stemming vs Lemmatization

## Stemming

Removes suffixes using simple rules.

Example:

```python
playing → play
worked → work
```

May produce invalid words.

---

## Lemmatization

Converts words into meaningful dictionary root forms.

Example:

```python
better → good
went → go
```

More accurate than stemming.

---

## Difference

| Stemming                 | Lemmatization             |
| ------------------------ | ------------------------- |
| Rule-based cutting       | Dictionary-based          |
| Faster                   | More accurate             |
| May create invalid words | Produces meaningful words |

---

# Q4. Morphological Analysis

## Theory

Morphology studies word structure.

Words are divided into morphemes.

---

## Morpheme

Smallest meaningful unit of language.

Example:

```python
unhappy = un + happy
```

---

## Free Morpheme

Can stand alone.

Examples:

```python
happy, play, nation
```

---

## Bound Morpheme

Cannot stand alone.

Examples:

```python
un, ed, ness
```

---

# Q5. POS Tagging

## Theory

Part-of-Speech tagging assigns grammatical categories to words.

Examples:

* Noun
* Verb
* Adjective
* Adverb

---

## Common POS

| POS         | Meaning            |
| ----------- | ------------------ |
| Noun        | person/place/thing |
| Verb        | action             |
| Adjective   | describes noun     |
| Adverb      | describes verb     |
| Conjunction | joins words        |
| Article     | a, an, the         |

---

## Rule Examples

| Rule                  | POS    |
| --------------------- | ------ |
| words ending in `-ly` | Adverb |
| words ending in `-ed` | Verb   |

---

# Q6. Ambiguity Detection

## Theory

Ambiguity means multiple meanings.

---

## Types

### Syntactic Ambiguity

Multiple sentence structures.

Example:

```python
I saw the man with a telescope
```

---

### Semantic Ambiguity

Word has multiple meanings.

Example:

```python
bank
```

---

# Q7. Bag of Words (BoW)

## Theory

Bag of Words represents text using word frequencies.

Steps:

1. Create vocabulary
2. Count word occurrences
3. Build matrix

---

## Example

| Word | Count |
| ---- | ----- |
| NLP  | 2     |
| AI   | 1     |

---

## Viva Points

* Ignores grammar/order
* Focuses on frequency

---

# Q8. TF-IDF

## Theory

TF-IDF measures importance of words.

---

## TF (Term Frequency)

TF = \frac{\text{Word Count}}{\text{Total Words}}

---

## IDF (Inverse Document Frequency)

IDF = \log\left(\frac{\text{Total Documents}}{\text{Documents containing word}}\right)

---

## TF-IDF

TF\text{-}IDF = TF \times IDF

---

## Viva Points

* Rare important words get high TF-IDF
* Common words get low score

---

# Q9. Cosine Similarity

## Theory

Measures similarity between vectors/documents.

Value:

* 1 → identical
* 0 → unrelated

---

## Formula

\text{Cosine Similarity} = \frac{A \cdot B}{|A||B|}

---

## Uses

* Recommendation systems
* NLP similarity
* Search engines

---

# Q11. Naive Bayes Classification

## Theory

Probability-based classification algorithm.

Used in:

* Spam detection
* Sentiment analysis

---

## Formula

P(Class|Words) \propto P(Class) \times P(Word_1|Class) \times P(Word_2|Class)

---

## Important Terms

| Term                  | Meaning                   |
| --------------------- | ------------------------- |
| Prior Probability     | Initial class probability |
| Likelihood            | Word probability          |
| Posterior Probability | Final probability         |

---

## Viva Points

* Assumes word independence
* Called “Naive” because of independence assumption

---

# Q12. Hidden Markov Model (HMM)

## Theory

HMM is a probabilistic model used for sequence prediction.

Used in:

* POS tagging
* Speech recognition
* NLP

---

## Components

| Component              | Meaning                    |
| ---------------------- | -------------------------- |
| States                 | hidden conditions          |
| Transition Probability | state-to-state probability |
| Emission Probability   | observation probability    |

---

## Formula

P(O|S) \times P(S_i|S_{i-1})

---

# Q13. N-gram Text Generation

## Theory

N-grams are sequences of N words.

| Type    | Example     |
| ------- | ----------- |
| Unigram | NLP         |
| Bigram  | NLP is      |
| Trigram | NLP is easy |

---

## Bigram Generation

Predicts next word using previous word.

Example:

```python
I love → NLP
```

---

# Q14. BLEU Score

## Theory

BLEU evaluates similarity between:

* reference sentence
* candidate sentence

Used in machine translation.

---

## Formula

BLEU = \frac{\text{Matching Words}}{\text{Total Candidate Words}}

---

## Viva Points

* Higher BLEU → better translation
* Measures text similarity

---

# Q15. Regex-based Text Cleaning

## Theory

Regular Expressions (Regex) are patterns for text matching and cleaning.

Used for:

* removing punctuation
* removing numbers
* pattern matching

---

## Important Regex

| Regex | Meaning     |
| ----- | ----------- |
| `\d`  | digit       |
| `\w`  | word        |
| `\s`  | whitespace  |
| `+`   | one or more |

---

## Important Functions

| Function       | Purpose      |
| -------------- | ------------ |
| `re.sub()`     | replace      |
| `re.findall()` | find matches |

---

# Q16. CFG Parsing

## Theory

Context-Free Grammar checks sentence validity using grammar rules.

---

## Example Rules

S \rightarrow NP\ VP

---

## Terms

| Symbol | Meaning     |
| ------ | ----------- |
| S      | Sentence    |
| NP     | Noun Phrase |
| VP     | Verb Phrase |

---

## Viva Points

* Used in syntax checking
* Uses production rules

---

# Q17. Chunking

## Theory

Chunking groups words into meaningful phrases.

Also called:

```python
Shallow Parsing
```

---

## Noun Phrase Rule

NP \rightarrow Det\ +\ Adj\ +\ Noun

---

## Example

```python
the smart student
```

* the → Determiner
* smart → Adjective
* student → Noun

Together form NP.

---

# Q18. RNN Sentiment Analysis

## Theory

RNN (Recurrent Neural Network) processes sequential data.

Used in:

* NLP
* Translation
* Sentiment analysis

---

## Workflow

```python
Text
→ Tokenization
→ Padding
→ Embedding
→ RNN
→ Prediction
```

---

## Important Layers

| Layer     | Purpose           |
| --------- | ----------------- |
| Embedding | word vectors      |
| SimpleRNN | sequence learning |
| Dense     | output layer      |

---

## Viva Points

* RNN remembers previous information
* Good for sequential text

---

# Q19. Named Entity Recognition (NER)

## Theory

NER identifies important entities from text.

---

## Entity Types

| Entity       | Example |
| ------------ | ------- |
| Person       | Rahul   |
| Location     | Mumbai  |
| Organization | Google  |
| Date         | Monday  |

---

## Example

Sentence:

```python
Rahul works at Google in Mumbai
```

Entities:

* Rahul → Person
* Google → Organization
* Mumbai → Location

---

## Uses

* Information extraction
* Chatbots
* Search engines
* NLP systems

---

# Common Python Functions Used in NLP

| Function  | Purpose       |
| --------- | ------------- |
| `split()` | tokenize      |
| `lower()` | lowercase     |
| `count()` | frequency     |
| `len()`   | count items   |
| `set()`   | unique words  |
| `join()`  | combine text  |
| `strip()` | remove spaces |

---

# Common Regex Shortcuts

| Regex | Meaning     |
| ----- | ----------- |
| `\d`  | digit       |
| `\w`  | word        |
| `\s`  | whitespace  |
| `^`   | NOT/start   |
| `+`   | one or more |

---

# Important Viva One-Liners

| Topic             | One-Liner                    |
| ----------------- | ---------------------------- |
| Tokenization      | Breaking text into tokens    |
| Stemming          | Rule-based suffix removal    |
| Lemmatization     | Dictionary root conversion   |
| TF-IDF            | Word importance measure      |
| Cosine Similarity | Vector similarity measure    |
| Naive Bayes       | Probability-based classifier |
| CFG               | Grammar-rule based parsing   |
| Chunking          | Phrase grouping              |
| RNN               | Sequential neural network    |
| NER               | Entity extraction from text  |
