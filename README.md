# Preprocessing
## Feature expansion

For a binary dataset, **expandfeatures.py** can add features of value $a \lor b$ for each possible combination of two distinct features $a$ and $b$ present in the initial dataset.

**Example:** for a dataset containing 4 features $a$, $b$, $c$ and $d$, the algorithm will add the following 6 new features:
- $a \lor b$
- $a \lor c$
- $a \lor d$
- $b \lor c$
- $b \lor d$
- $c \lor d$

The number of new features added is $k * \binom{n}{2}$ where $n$ is the number of features in the initial dataset and $k$ is the number of cnfs used.

The other supported cnfs are $(\neg x \lor y)$, $(x \lor \neg y)$, $(\neg x \lor \neg y)$ and $(x \oplus y)$. They can also be combined.

### Usage

```
python expandfeatures.py 11111 dataset expanded_dataset
```

Each digit of the first argument can be set to 1 or 0 (true or false). These digits are for the following cnfs respectively:
- $x \lor y$
- $\neg x \lor y$
- $x \lor \neg y$
- $\neg x \lor \neg y$
- $x \oplus y$

So with 10001 as argument, the cnfs used will be ($x \lor y$) and ($x \oplus y$).