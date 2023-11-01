# Preprocessing
## Feature expansion

For a binary dataset, **preprocessing.py** adds features of value $a ∨ b$ for each possible combination of two distinct features $a$ and $b$ present in the initial dataset.

**Example:** for a dataset containing 4 features $a$, $b$, $c$ and $d$, the algorithm will add the following 6 new features:
- $a ∨ b$
- $a ∨ c$
- $a ∨ d$
- $b ∨ c$
- $b ∨ d$
- $c ∨ d$

The number of new features added is $\binom{n}{2}$ where $n$ is the number of features in the initial dataset.

### Usage

```
python preprocessing.py dataset.txt dataset_expanded.txt
```
