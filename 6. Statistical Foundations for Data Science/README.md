# 6. Statistical Foundations for Data Science using Python

An eight-notebook module covering the statistics an undergraduate needs before touching a
machine-learning model. Every concept is derived on paper (in Markdown/LaTeX), implemented
in Python, and then **verified by simulation** so students can see the theory hold up.

## Contents

| # | Notebook | Topics |
|---|---|---|
| 1 | [Probability Basics](1.%20Probability%20Basics.ipynb) | Sample spaces, events, axioms, addition & multiplication rules, conditional probability, independence, law of total probability, **Bayes' theorem**, permutations & combinations, simulation (birthday problem, Monty Hall) |
| 2 | [Random Variables](2.%20Random%20Variables.ipynb) | Discrete vs continuous, PMF/PDF/CDF, **expectation**, **variance**, `ddof` and Bessel's correction, linearity, z-scores, skewness & kurtosis, LOTUS & Jensen's inequality, joint/marginal/conditional distributions |
| 3 | [Probability Distributions](3.%20Probability%20Distributions.ipynb) | Bernoulli, Binomial, Poisson, Geometric, Uniform, **Normal**, Exponential, Log-normal, t, chi-square, F; empirical rule; choosing & fitting a distribution; Q–Q plots; CLT preview |
| 4 | [Sampling Techniques](4.%20Sampling%20Techniques.ipynb) | Parameter vs statistic; simple random, systematic, **stratified**, cluster sampling; non-response & survivorship bias; standard error; the **Central Limit Theorem**; **confidence intervals**; **bootstrap**; sample-size formulas; train/test splitting |
| 5 | [Correlation and Covariance](5.%20Correlation%20and%20Covariance.ipynb) | Covariance, **Pearson r**, r², Spearman & Kendall, Anscombe's quartet, correlation matrices/heatmaps, significance & Fisher-z CIs, confounding, **partial correlation**, **Simpson's paradox**, spurious correlation, **multicollinearity & VIF** |
| 6 | [Hypothesis Testing](6.%20Hypothesis%20Testing.ipynb) | H₀/H₁, test statistics, **p-values** (and what they are not), α/β, **Type I & II errors**, **power analysis**, one- vs two-tailed, **permutation tests**, **effect size**, multiple comparisons, Bonferroni & Benjamini–Hochberg, p-hacking |
| 7 | [t-Test](7.%20t-Test.ipynb) | Why t not z, degrees of freedom, one-sample, two-sample, **Welch's** test, **paired** t-test, assumption checks (Q–Q, Levene, Shapiro), non-parametric fallbacks, complete **A/B test walkthrough** |
| 8 | [Chi-Square Test](8.%20Chi-Square%20Test.ipynb) | χ² statistic, **goodness-of-fit**, **independence**, **homogeneity**, contingency tables, expected-count rules, Yates' correction, **Fisher's exact test**, McNemar, **Cramér's V**, residual analysis, categorical feature selection, model calibration |

Work through them in order — each notebook builds on the previous one.

## Running the notebooks

From the repository root:

```bash
poetry install
```

Then launch Jupyter and select the Poetry/`.venv` interpreter as the kernel:

```bash
poetry run jupyter notebook
```

The notebooks ship without stored outputs. To run them all once and save the results
(figures and printed output) into the files:

```bash
poetry run jupyter nbconvert --to notebook --execute --inplace *.ipynb
```

Libraries used: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy`, `scikit-learn` — all
already in the project's `pyproject.toml`. No downloads or API keys are needed; every
dataset is either simulated with a fixed seed or bundled with scikit-learn
(`load_diabetes`, `load_iris`).

## How the notebooks are structured

Each one follows the same rhythm so students know what to expect:

1. **Intent** — what the notebook covers and why it matters
2. **Theory** — the definition and formula, stated plainly
3. **Code** — the same thing computed by hand, then with the library one-liner
4. **Simulation** — proof that the formula matches reality
5. **Visualisation** — the picture that makes it stick
6. **Pitfalls** — the mistakes this topic invites, demonstrated rather than asserted
7. **Exercises** — four per notebook, each with a worked solution in the following cell

All randomness is seeded, so every number in the text matches what students will see.

## Teaching notes

- **Suggested pacing:** one notebook per 90-minute session; notebooks 1, 4 and 6 are the
  densest and may need two.
- **Cells are meant to be edited.** The simulations are the pedagogical core — ask students
  to change a parameter (sample size, effect size, α) and predict the result before running.
- **Exercise solutions sit directly below each question.** For assessment, delete the
  solution cells before distributing, or ask students to attempt them in a copy first.
- **Recurring threads worth calling out explicitly:** the difference between
  $P(A\mid B)$ and $P(B\mid A)$ (notebooks 1, 6); statistical significance vs. practical
  importance (notebooks 5, 6, 7, 8); and "plot the data before you trust the number"
  (notebook 5).
- **Prerequisites:** basic Python and NumPy/pandas — see
  [2. Python Intro and Math Foundation](../2.%20Python%20Intro%20and%20Math%20Foundation).
- **Leads into:** regression and classification in
  [4. ML Algorithms](../4.%20ML%20Algorithms), which assume the sampling, correlation and
  hypothesis-testing material here.
