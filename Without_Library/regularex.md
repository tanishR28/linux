# Regular Expressions (RE / Regex)

A **Regular Expression (Regex)** is a pattern used to:

* search text
* match text
* clean text
* replace text

Used heavily in:

* NLP
* Data Cleaning
* Validation
* Search Engines

Python uses the `re` module for regex operations.

---

# Importing Regex Module

```python id="6l3l0o"
import re
```

---

# Most Important Function

## `re.sub()`

Syntax:

```python id="k4l6qx"
re.sub(pattern, replacement, text)
```

Meaning:

> Replace matching pattern with replacement.

Example:

```python id="3u8q0q"
re.sub(r'\d+', '', "abc123")
```

Output:

```python id="jlwm6n"
abc
```

(removes numbers)

---

# Important Regex Codes to Remember

| Regex  | Meaning                     | Example Match    |
| ------ | --------------------------- | ---------------- |
| `\d`   | digit                       | 0-9              |
| `\D`   | non-digit                   | a, #             |
| `\w`   | word character              | a-z, A-Z, 0-9    |
| `\W`   | non-word character          | @, #             |
| `\s`   | whitespace                  | space, tab       |
| `\S`   | non-whitespace              | letters          |
| `.`    | any character               | a,1,@            |
| `^`    | starts with / NOT inside [] | start            |
| `$`    | ends with                   | end              |
| `+`    | one or more                 | aaa              |
| `*`    | zero or more                | optional repeats |
| `?`    | zero or one                 | optional         |
| `[]`   | character set               | [abc]            |
| `[^ ]` | NOT in set                  | opposite match   |

---

# Important Examples

---

# 1. `\d` → Digits

```python id="f0x0bn"
import re

text = "abc123"

print(re.findall(r'\d', text))
```

Output:

```python id="2bc1ei"
['1', '2', '3']
```

---

# 2. `\w` → Word Characters

```python id="7q8a9u"
re.findall(r'\w', "Hi@123")
```

Output:

```python id="jlwm6m"
['H', 'i', '1', '2', '3']
```

---

# 3. `\s` → Spaces

```python id="2k9u5r"
re.findall(r'\s', "Hi There")
```

Finds spaces.

---

# 4. `+` → One or More

```python id="l1z8v4"
re.findall(r'\d+', "abc123xyz45")
```

Output:

```python id="1l2q6f"
['123', '45']
```

Groups consecutive digits.

---

# 5. `^` → NOT (inside brackets)

```python id="x4g0y8"
re.sub(r'[^\w\s]', '', text)
```

Meaning:

> Remove everything NOT word/space.

Used for punctuation removal.

---

# Most Useful NLP Regex Programs

---

# Remove Numbers

```python id="jlwm6l"
re.sub(r'\d+', '', text)
```

---

# Remove Punctuation

```python id="32n6k4"
re.sub(r'[^\w\s]', '', text)
```

---

# Remove Extra Spaces

```python id="i4m0x1"
re.sub(r'\s+', ' ', text)
```

---

# Find Words

```python id="w8t7h2"
re.findall(r'\w+', text)
```

---

# Find Emails

```python id="jlwm6k"
re.findall(r'\S+@\S+', text)
```

---

# Common Regex Functions

| Function       | Purpose              |
| -------------- | -------------------- |
| `re.sub()`     | replace              |
| `re.findall()` | return all matches   |
| `re.search()`  | first match          |
| `re.match()`   | match from beginning |
| `re.split()`   | split text           |

---

# Example of `findall()`

```python id="7l0u5o"
import re

text = "My marks are 85 and 90"

nums = re.findall(r'\d+', text)

print(nums)
```

Output:

```python id="9x0r1e"
['85', '90']
```

---

# Easy Memory Tricks

| Symbol | Memory    |
| ------ | --------- |
| `\d`   | d → digit |
| `\w`   | w → word  |
| `\s`   | s → space |
| `+`    | more      |
| `^`    | NOT/start |
| `[]`   | group/set |

---

# Viva One-Liner

> Regular expressions are patterns used for searching, matching, and cleaning text data.
