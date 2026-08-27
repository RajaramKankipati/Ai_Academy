# 6. Statistical Foundations for Data Science

A twelve-session practical module built as **one continuous project**: a
heart-disease risk-screening system for a referral clinic's patient registry. Every
session uses the same dataset and works toward the same goal — no dataset-switching,
no disconnected examples. Each one is a stage in a pipeline, and each stage's output
is exactly what the next stage needs as input.

Each notebook is a self-contained, step-by-step lab in the same format as the
[MLOps Skilling Course](../11.%20MLOps%20Skilling%20Course): a short "what you'll build
and why" intro, a **Prerequisites** cell, numbered steps with runnable code, an
**Observe / Infer** note after every code cell, and a wrap-up naming what the session
hands to the next one.

## The dataset

Every session opens with the same nine lines, fetching the UCI **Heart Disease**
(Cleveland) dataset live from the UCI ML Repository:

```python
from ucimlrepo import fetch_ucirepo
import pandas as pd

heart_disease = fetch_ucirepo(id=45)
df = pd.concat([heart_disease.data.features, heart_disease.data.targets], axis=1)

df = df.dropna().reset_index(drop=True)
df["target"] = (df["num"] > 0).astype(int)
df = df.drop(columns="num")
```

303 patients are fetched and 297 survive `dropna()` (six are missing `ca` or `thal`),
so every session analyses the identical 297 patients. Fetching from the repository
rather than reading a local CSV keeps the notebooks runnable by anyone. The inputs are
clinical measurements (`age`, `trestbps`, `chol`, `thalach`, `oldpeak`) and categorical
findings (`sex`, `cp`, `fbs`, `restecg`, `exang`, `slope`, `ca`, `thal`); `num` is
angiographic disease severity 0-4, binarised here into `target`.

Deliberately one dataset throughout: switching datasets between topics would mean
re-learning the data every session instead of building cumulative familiarity with one
problem, the way a real analyst does.

## The system, and why it's built this way

A predictive model isn't just an algorithm — it's a pipeline: raw measurements go in, a
validated, honestly-evaluated probability of disease comes out. Skipping or
misunderstanding any stage doesn't just weaken one session's topic; it propagates
forward and corrupts everything built after it. Every session asks not only "what is
this technique" but "what happens downstream if we get this stage wrong."

```
Stage 1: Understand the raw signals          Sessions 1-3
         (probability, random variables, distributions)
              |
              v
Stage 2: Design trustworthy data collection  Session 4
         (sampling)
              |
              v
Stage 3: Map relationships between signals   Session 5
         (correlation, covariance)
              |
              v
Stage 4: Validate claims before trusting     Sessions 6-8
         (hypothesis testing, t-test, chi-square)
              |
              v
Stage 5: Build and validate the core         Sessions 9-12
         (regression, train-test split, overfitting, bias-variance)
              |
              v
         A trustworthy probability of disease for a new patient
```

## Delivery plan

| # | Session | This stage's question | Stage |
|---|---|---|---|
| 1 | [Probability Basics](1.%20Probability%20Basics.ipynb) | How do we read the system's eventual output — a probability — without misreading it? | 1 |
| 2 | [Random Variables](2.%20Random%20Variables.ipynb) | How does each individual input behave on its own? | 1 |
| 3 | [Probability Distributions](3.%20Probability%20Distributions.ipynb) | What *shape* does each input take, and which assumptions does that license? | 1 |
| 4 | [Sampling Techniques](4.%20Sampling%20Techniques.ipynb) | Is the registry itself a fair picture of the patients we'll deploy on? | 2 |
| 5 | [Correlation and Covariance](5.%20Correlation%20and%20Covariance.ipynb) | Which inputs relate to disease, and which are duplicates of each other? | 3 |
| 6 | [Hypothesis Testing](6.%20Hypothesis%20Testing.ipynb) | Would these relationships survive in the next 297 patients? | 4 |
| 7 | [t-Test](7.%20t-Test.ipynb) | …specifically, for a continuous measurement compared between two groups | 4 |
| 8 | [Chi-Square Test](8.%20Chi-Square%20Test.ipynb) | …specifically, for categorical inputs where a mean is meaningless | 4 |
| 9 | [Regression Basics](9.%20Regression%20Basics.ipynb) | How do we learn the modelling tool itself, safely, before the real stakes? | 5 |
| 10 | [Train-Test Split](10.%20Train-Test%20Split.ipynb) | Does the assembled system work on patients it has never seen? | 5 |
| 11 | [Overfitting](11.%20Overfitting.ipynb) | When does more complexity start hurting instead of helping? | 5 |
| 12 | [Bias-Variance Tradeoff](12.%20Bias-Variance%20Tradeoff.ipynb) | *Why* does it start hurting — and which cure applies? | 5 |

Work through them in order — every session opens with what the previous stage handed
it and closes with what it hands to the next.

## How each notebook is structured

1. **Goal** — one paragraph on what you'll be able to do afterwards
2. **What this stage does for the system** — what breaks downstream if it's done wrong
3. **The dataset / How to read this notebook / Prerequisites**
4. **Step 1** — load the registry from UCI (identical in every session)
5. **Steps 2-N** — a short motivation, runnable code, then an **Observe / Infer** note:
   *Observe* points at exactly what to look at in the output, *Infer* explains what to
   conclude and what a different result would have implied
6. **What this session hands to the next one** — the connective tissue that makes this
   a project rather than twelve unrelated exercises
7. **Try it yourself** — four extensions on the same registry

## Setup

From the repository root:

```bash
poetry install
poetry run jupyter notebook
```

Libraries used: `ucimlrepo`, `numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy`,
`scikit-learn`, `statsmodels` — all already in `pyproject.toml`. Every session runs
fully locally; no account or credentials are needed anywhere in the module.

## Teaching notes

- **Suggested pacing:** one session per 60-90 minute slot. The five-stage pipeline
  above is worth drawing on a whiteboard before Session 1 so students see the whole arc
  before starting.
- **The Observe / Infer notes are the lesson**, not commentary on it. Several flag
  results that look like bugs and aren't — Session 4's convenience sample having the
  *lowest* variance, Session 10's test score coming out *above* its training score,
  Session 9's negative R². Read them before running the next cell.
- **Cells are meant to be edited.** Swap in a different input column and predict the
  result before running; since every session shares one dataset, a change explored in
  Session 5 is directly relevant again in Session 9.
- **The "what this session hands to the next one" section is not filler.** Worth
  discussing explicitly: ask "what would happen to Session N+2 if this stage were
  skipped or done badly?" Session 12's final table answers that for all twelve at once.
- **Numbers in the notes are real.** Every figure quoted in an Observe note was
  produced by running that cell, so a mismatch means something changed — a different
  library version, or a dataset that no longer matches.
- **Prerequisites:** basic Python and NumPy/pandas — see
  [2. Python Intro and Math Foundation](../2.%20Python%20Intro%20and%20Math%20Foundation).
- **Leads into:** [4. ML Algorithms](../4.%20ML%20Algorithms) and
  [7. Machine Learning Fundamentals and Predictive Analytics](../7.%20Machine%20Learning%20Fundamentals%20and%20Predictive%20Analytics),
  which assume the sampling, correlation, and hypothesis-testing material here; and
  [11. MLOps Skilling Course](../11.%20MLOps%20Skilling%20Course), which takes a
  validated model and addresses what this module explicitly cannot — drift, versioning,
  and deployment.
