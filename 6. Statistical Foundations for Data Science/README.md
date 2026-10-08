# 6. Statistical Foundations for Data Science

A 12-session practical module built as **one continuous project**. Each session teaches one statistical topic and uses
it to take the next step towards the same end goal, on the same dataset.

## The project

A credit-card issuer in Taiwan wants an **early-warning score**: for every card holder, the **probability that they
will miss next month's payment**, so its collections team can contact the riskiest customers first. Across the twelve
sessions you build that score and, just as important, find out how far it can be trusted.

The dataset is [UCI Default of Credit Card Clients](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients)
(id 350): 30,000 card holders in 2005, with credit limit, sex, education, marital status, age, six months of repayment
status, bills and payments, and whether they defaulted the following month. Each notebook downloads it with
[`ucimlrepo`](https://github.com/uci-ml-repo/ucimlrepo), so there are no CSV files to manage.

**Every session starts with the same loading cell**, which also locks away 6,000 customers (20%) as a final test set.
Sessions 1-11 work only on the other 24,000. Session 12 unlocks the test set once, for the final, honest verdict.

```
Stage 1  Understand the data           Sessions 1-3   What does default look like? How does each input behave?
              |
Stage 2  Trust the sample              Session 4      What do these customers represent? How precise are our numbers?
              |
Stage 3  Find the real signals         Sessions 5-8   Which inputs are genuinely related to default?
              |
Stage 4  Build and validate the score  Sessions 9-12  How good is the score, and how far can we trust it?
              |
         A calibrated probability of default, tested once on 6,000 untouched customers
```

## Delivery plan

| # | Session | Topics | What it contributes to the score |
|---|---|---|---|
| 1 | [Probability Basics](1.%20Probability%20Basics.ipynb) | Conditional probability, independence, Bayes, total probability | The 22.1% baseline; recent lateness as the key signal; why priors matter |
| 2 | [Random Variables](2.%20Random%20Variables.ipynb) | PMF, PDF/CDF, expectation, variance, sums, conditional expectation | The `months_late` input; the score as a conditional expectation |
| 3 | [Probability Distributions](3.%20Probability%20Distributions.ipynb) | Binomial (and when it fails), normal, log-normal, mixtures, data audit | `log_limit`; cleaning rules for undocumented and inconsistent codes |
| 4 | [Sampling Techniques](4.%20Sampling%20Techniques.ipynb) | Standard error, CLT, confidence intervals, stratification, sampling bias | Precision of every estimate; stratified splits; the representativeness question |
| 5 | [Correlation and Covariance](5.%20Correlation%20and%20Covariance.ipynb) | Pearson vs Spearman, CIs for r, partial correlation, VIF | `utilization` replaces six near-duplicate bills; the limit is partly confounded |
| 6 | [Hypothesis Testing](6.%20Hypothesis%20Testing.ipynb) | Permutation and z-tests, effect size, errors, power, multiple testing | Effect sizes over p-values; the decision to leave sex out |
| 7 | [t-Test](7.%20t-Test.ipynb) | One-sample, Welch and paired t-tests, Cohen's d, Mann-Whitney | Confirms the numeric signals; paired comparisons for later |
| 8 | [Chi-Square Test](8.%20Chi-Square%20Test.ipynb) | Goodness of fit, independence, residuals, Cramér's V, Fisher | The categorical encoding and merges |
| 9 | [Regression Basics](9.%20Regression%20Basics.ipynb) | Linear vs logistic regression, odds ratios, checking errors by group, collinearity | The first, interpretable score |
| 10 | [Train-Test Split](10.%20Train-Test%20Split.ipynb) | AUC and Brier score, stratified CV, tuning, leakage, paired model comparison | An honest estimate of the score; why the test set is locked |
| 11 | [Overfitting](11.%20Overfitting.ipynb) | Complexity and learning curves, feature explosion, regularisation, CV tuning | Shows extra flexibility barely helps; the candidate models |
| 12 | [Bias-Variance Tradeoff](12.%20Bias-Variance%20Tradeoff.ipynb) | Measuring bias and variance, data size, ensembles, calibration | The rule-based final choice and the verdict on untouched customers |

Work through them in order. Each session opens with the project roadmap (marking where you are) and closes with
**What this session hands to the project**. Sessions 9-12 share one `prepare()` function in which every line is a
decision made, with evidence, in an earlier session.

## How each notebook is structured

Each notebook follows the format of the [MLOps Skilling Course](../11.%20MLOps%20Skilling%20Course) guides: an
**Overview** with learning goals, **Prerequisites**, the **Dataset** and the **project roadmap**, numbered **steps** (a
short explanation, runnable code, then a **Read the output** note pointing at the numbers that matter), **What this
session hands to the project**, a **Common mistakes and fixes** table, and **Exercises**.

## Setup

All twelve notebooks share one pinned `requirements.txt` in this folder. From this folder:

```bash
python3.11 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter notebook
```

| Package | Why we need it |
| --- | --- |
| ucimlrepo | Downloads the dataset from UCI |
| scikit-learn | The locked test set, models, cross-validation and metrics |
| numpy, pandas | Arrays, tables, sampling |
| scipy | Distributions and statistical tests |
| statsmodels | Regression summaries, proportion tests, power analysis, VIF |
| matplotlib | Charts |
| notebook, ipykernel | Running the notebooks |

Everything runs locally. No account or credentials are needed, only an internet connection to download the data. Most
notebooks run in well under a minute; Sessions 11 and 12 take one to two minutes.

## Teaching notes

- **Suggested pacing:** one session per 60-90 minute slot. Draw the four-stage roadmap on the board before Session 1.
- **The "Read the output" notes are the lesson.** Each one quotes the numbers the cell actually prints with the versions
  in `requirements.txt`. If a learner's numbers differ in more than the last decimal place, check their library versions.
- **Several results contradict a first impression.** These make good discussion points:
  - the binomial fails for `months_late`, because lateness persists (Session 3);
  - the raw credit limit passes the 68-95-99.7 rule while being clearly skewed (Session 3);
  - the age U-shape disappears inside the model, because it was confounded (Session 9);
  - the locked test set scores lower than cross-validation, which is exactly why it was locked (Session 12);
  - the forest ranks better on the test set but is not adopted, because the choice was made by a rule fixed in advance
    (Session 12).
- **The project has explicit judgement calls:** excluding sex (Session 6), merging undocumented codes (Session 8) and the
  final model rule (Session 12). Ask learners whether they would have decided differently, and what evidence would change
  their mind.
- **Seeds are fixed** so every run gives the same numbers. Changing a seed is a good exercise: which conclusions survive?
- **Prerequisites:** basic Python and pandas; see
  [2. Python Intro and Math Foundation](../2.%20Python%20Intro%20and%20Math%20Foundation).
- **Leads into:** [4. ML Algorithms](../4.%20ML%20Algorithms),
  [7. Machine Learning Fundamentals and Predictive Analytics](../7.%20Machine%20Learning%20Fundamentals%20and%20Predictive%20Analytics),
  and the [11. MLOps Skilling Course](../11.%20MLOps%20Skilling%20Course), which picks up the limits listed at the end of
  Session 12: monitoring calibration, data drift and fairness once a model is deployed.
