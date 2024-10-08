# Feature expansion (preprocessing)

For a binary dataset, `expandfeatures.py` or `expandfeatures.cpp` can add features of value $a \lor b$ for each possible combination of two distinct features $a$ and $b$ present in the initial dataset.

**Example:** for a dataset containing 4 features $a$, $b$, $c$ and $d$, the algorithm will add the following 6 new features:
- $a \lor b$
- $a \lor c$
- $a \lor d$
- $b \lor c$
- $b \lor d$
- $c \lor d$

The number of new features added is $k * \binom{m}{2}$ where $m$ is the number of features in the initial dataset and $k$ is the number of CNFs used.

The other supported CNFs are $(\neg x \lor y)$, $(x \lor \neg y)$, $(\neg x \lor \neg y)$ and $(x \oplus y)$. They can also be combined.

## Usage

Using Python or equivalent using C++
```
python expandfeatures.py 11111 dataset expanded_dataset
```

Each digit of the first argument can be set to 1 or 0 (true or false). These digits are for the following CNFs respectively:
- $x \lor y$
- $\neg x \lor y$
- $x \lor \neg y$
- $\neg x \lor \neg y$
- $x \oplus y$

So with 10001 as argument, the CNFs used will be ($x \lor y$) and ($x \oplus y$).



# Printing solutions (postprocessing)

## Requirements

- [Graphviz](https://graphviz.org/)
- anytree
```
pip install anytree
```

## Usage

Running Blossom with `--print_sol` gives an output (sol) used by `printsol.py` to create an image (target) of the tree.

```
python printsol.py sol dataset target
```

The dataset given here should **NEVER** be an expanded dataset.
Average length of explanations and number of nodes given in output.



# Abductive explanation (postprocessing)

## Requirements

- constraint
```
pip install constraint
```

## Usage

`CSPSolver.py` allow to solve a CSP and manually find a weak AXp of a decision.
