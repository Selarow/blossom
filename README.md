# Preprocessing
## Feature expansion

For a binary dataset, **expandfeatures.py** can add features of value $a ∨ b$ for each possible combination of two distinct features $a$ and $b$ present in the initial dataset.

**Example:** for a dataset containing 4 features $a$, $b$, $c$ and $d$, the algorithm will add the following 6 new features:
- $a ∨ b$
- $a ∨ c$
- $a ∨ d$
- $b ∨ c$
- $b ∨ d$
- $c ∨ d$

The number of new features added is $\binom{n}{2}$ where $n$ is the number of features in the initial dataset.

The other supported cnfs are ($\neg x ∨ y$), ($x ∨ \neg y$) and ($x ⊕ y$). They can also be combined.

### Usage

```
python expandfeatures.py 1001 dataset.txt dataset_expanded.txt
```

Each digit of the first argument can be set to 1 or 0 (true or false). These digits are for the following cnfs respectively:
- $x$ ∨ $y$
- $\neg x$ ∨ $y$
- $x$ ∨ $\neg y$
- $x$ ⊕ $y$

So with 1001 as argument, the cnfs used will be ($x$ ∨ $y$) and ($x$ ⊕ $y$).