# 6. Statistical Foundations for Data Science using Python

A twelve-notebook module built as **one continuous project**: building a
trustworthy heart-disease risk-screening system for a clinic's patient registry.
Every notebook uses the same dataset and works toward the same goal — no
dataset-switching, no disconnected examples. Each one is a stage in a systems
pipeline, and each stage's output is exactly what the next stage needs as input.

## The system, and why it's built this way

A predictive model isn't just an algorithm — it's a pipeline: raw measurements go
in, a validated, honestly-evaluated probability of disease comes out. Skipping or
misunderstanding any stage of that pipeline doesn't just weaken one notebook's
topic — it propagates forward and corrupts everything built after it. That's the
systems-thinking thread running through the whole module: every notebook asks not
just "what is this technique" but "what happens downstream if we get this stage
wrong."

```
Stage 1: Understand the raw signals        Notebooks 1-3
         (probability, random variables, distributions)
              |
              v
Stage 2: Design trustworthy data collection   Notebook 4
         (sampling)
              |
              v
Stage 3: Map relationships between signals    Notebook 5
         (correlation, covariance)
              |
              v
Stage 4: Validate claims before trusting them Notebooks 6-8
         (hypothesis testing, t-test, chi-square)
              |
              v
Stage 5: Build and validate the predictive core   Notebooks 9-12
         (regression, train-test split, overfitting, bias-variance)
              |
              v
         A trustworthy probability of disease for a new patient
```

## Contents

| # | Notebook | This stage's question |
|---|---|---|
| 1 | [Probability Basics](1.%20Probability%20Basics.ipynb) | How do we correctly read the system's eventual output — a probability? |
| 2 | [Random Variables](2.%20Random%20Variables.ipynb) | How does each individual input (age, cholesterol, …) behave on its own? |
| 3 | [Probability Distributions](3.%20Probability%20Distributions.ipynb) | What *shape* does each input's variation take, and why does it matter? |
| 4 | [Sampling Techniques](4.%20Sampling%20Techniques.ipynb) | How do we make sure the registry itself isn't quietly biased? |
| 5 | [Correlation and Covariance](5.%20Correlation%20and%20Covariance.ipynb) | Which inputs relate to disease, and to each other? |
| 6 | [Hypothesis Testing](6.%20Hypothesis%20Testing.ipynb) | Is a relationship we found real, or could it be chance? (general framework) |
| 7 | [t-Test](7.%20t-Test.ipynb) | …specifically, for comparing a continuous measurement between two groups |
| 8 | [Chi-Square Test](8.%20Chi-Square%20Test.ipynb) | …specifically, for comparing categorical variables between groups |
| 9 | [Regression Basics](9.%20Regression%20Basics.ipynb) | How do we learn the modeling tool itself, safely, before the real stakes? |
| 10 | [Train-Test Split](10.%20Train-Test%20Split.ipynb) | Does the assembled system actually work on patients it hasn't seen? |
| 11 | [Overfitting](11.%20Overfitting.ipynb) | When does more model complexity start hurting instead of helping? |
| 12 | [Bias-Variance Tradeoff](12.%20Bias-Variance%20Tradeoff.ipynb) | How much complexity can this system actually support, and why? |

Work through them in order — every notebook explicitly opens with what the
previous stage handed it, and closes with what it hands to the next.

## The dataset

Every single notebook uses one file:
`5. MLOps/2. End-to-End ML/data/heart_disease_cleaned_2.csv` — 438 patients, with
clinical measurements (`age`, `chol`, `trestbps`, `thalach`), categorical findings
(`sex`, `cp`, `fbs`, `restecg`, `exang`, `slope`, `thal`), and the outcome
(`target`: disease presence). Deliberately one dataset throughout: switching
datasets between topics would mean re-learning the data every notebook instead of
building cumulative familiarity with it — the same way a real analyst goes deep on
one problem rather than shallow across many.

A small number of illustrative sections (Notebook 7's paired-vs-independent t-test
comparison) use a clearly-labeled synthetic example specifically because the
registry has no repeated measurements per patient to draw from — even there, the
mechanism demonstrated is the one you'd apply directly to this same registry the
moment it gained follow-up visits.

## How each notebook is structured

1. **The topic** — a plain definition
2. **Why it matters for this system** — what breaks downstream if this stage is
   done wrong, in systems-thinking terms
3. **The toolkit** — what methods/options exist for this topic
4. **How to choose** — decision criteria for picking between them, not just how to
   run one
5. **Applied to the registry** — actually run on the same 438 patients every other
   notebook uses
6. **Systems view** — explicitly, what this stage produces and what the next stage
   consumes
7. **Try it yourself** — extend the same analysis further on the same data

## Running the notebooks

From the repository root:

```bash
poetry install
poetry run jupyter notebook
```

Libraries used: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy`,
`scikit-learn`, `statsmodels` — all already in `pyproject.toml`.

## Teaching notes

- **Suggested pacing:** one notebook per 60-90 minute session; the five-stage
  pipeline diagram above is worth drawing on a whiteboard before Notebook 1 so
  students see the whole arc before starting.
- **Cells are meant to be edited.** Swap in a different input column and predict
  the result before running — since every notebook shares one dataset, a change
  made while exploring Notebook 5 is directly relevant again in Notebook 9.
- **The "systems view" section of each notebook is not filler** — it's the
  connective tissue that makes this a project instead of twelve unrelated
  exercises. Worth discussing explicitly in a classroom setting: ask "what would
  happen to Notebook N+2 if this notebook's stage were skipped or done badly?"
- **Prerequisites:** basic Python and NumPy/pandas — see
  [2. Python Intro and Math Foundation](../2.%20Python%20Intro%20and%20Math%20Foundation).
- **Leads into:** regression and classification in
  [4. ML Algorithms](../4.%20ML%20Algorithms) and
  [7. Machine Learning Fundamentals and Predictive Analytics](../7.%20Machine%20Learning%20Fundamentals%20and%20Predictive%20Analytics),
  which assume the sampling, correlation, and hypothesis-testing material here.
