# 7. Machine Learning Fundamentals and Predictive Analytics

An eleven-notebook module covering the standard supervised- and unsupervised-learning toolkit,
plus text, time series and recommender applications. It builds directly on
[6. Statistical Foundations for Data Science](../6.%20Statistical%20Foundations%20for%20Data%20Science) —
regression, train/test discipline, overfitting and the bias-variance trade-off are assumed
knowledge here, not re-derived.

## Contents

| # | Notebook | Topics |
|---|---|---|
| 1 | [Linear Regression](1.%20Linear%20Regression.ipynb) | Normal equation vs gradient descent, MAE/RMSE/R²/MAPE, feature scaling, **feature engineering**, **Ridge/Lasso/Elastic Net**, `Pipeline` + `ColumnTransformer` case study |
| 2 | [Logistic Regression](2.%20Logistic%20Regression.ipynb) | Sigmoid & log-odds, log loss, **confusion matrix**, precision/recall/F1, **ROC-AUC vs PR-AUC**, odds ratios, class imbalance, multiclass, **calibration** |
| 3 | [Decision Trees](3.%20Decision%20Trees.ipynb) | Gini/entropy, information gain by hand, regression trees, pre/post-**pruning**, impurity vs **permutation importance**, axis-aligned geometry |
| 4 | [K-Nearest Neighbors](4.%20K-Nearest%20Neighbors.ipynb) | Distance metrics, mandatory scaling, choosing $k$, distance weighting, **curse of dimensionality**, retrieval/recommendation use |
| 5 | [Clustering](5.%20Clustering.ipynb) | **K-Means**, elbow/silhouette, k-means++, **hierarchical/dendrograms**, **DBSCAN**, **Gaussian Mixture Models**, ARI/NMI, stability, customer segmentation |
| 6 | [Random Forest](6.%20Random%20Forest.ipynb) | Bagging & variance reduction, `max_features` decorrelation, **OOB scoring**, importances (impurity/permutation/drop-column), partial dependence, Extra Trees vs boosting |
| 7 | [Support Vector Machines](7.%20Support%20Vector%20Machines.ipynb) | Maximum margin, support vectors, hinge loss, **kernel trick** (linear/poly/RBF), `C`/`gamma` tuning, calibration cost, SVR, computational limits |
| 8 | [Naive Bayes](8.%20Naive%20Bayes.ipynb) | Bayes' theorem to a classifier by hand, Laplace smoothing, Gaussian/Multinomial/Bernoulli/Complement variants, spam filter from scratch, calibration weakness |
| 9 | [Introduction to NLP](9.%20Introduction%20to%20NLP.ipynb) | Tokenisation, stemming/lemmatisation, bag-of-words & n-grams, **TF-IDF**, toy NER/POS, **word embeddings**, NMF/LDA topic modelling, sentiment pipeline |
| 10 | [Time Series Analytics](10.%20Time%20Series%20Analytics.ipynb) | Decomposition, stationarity/ADF, ACF/PACF, exponential smoothing, **ARIMA/SARIMA**, lag-feature regression forecasting, `TimeSeriesSplit`, anomaly detection |
| 11 | [Recommender Systems](11.%20Recommender%20Systems.ipynb) | Utility matrix, content-based & collaborative filtering, **matrix factorisation**, cold start, precision/recall@k, implicit feedback, hybrids, popularity bias |

Work through them in order — later notebooks assume the evaluation habits (baselines,
cross-validation, honest test sets) built in the earlier ones.

## Running the notebooks

From the repository root:

```bash
poetry install
```

Then launch Jupyter and select the Poetry/`.venv` interpreter as the kernel:

```bash
poetry run jupyter notebook
```

The notebooks ship without stored outputs. To run them all once and save the results into the
files:

```bash
poetry run jupyter nbconvert --to notebook --execute --inplace *.ipynb
```

Libraries used: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy`, `scikit-learn`, and
`statsmodels` (Notebook 10 only) — all in the project's `pyproject.toml`. No downloads or API
keys are needed; every dataset is either simulated with a fixed seed or bundled with
scikit-learn (`load_iris`, `load_wine`, `load_digits`, `load_diabetes`, `load_breast_cancer`).

## How the notebooks are structured

Each one follows the rhythm established in the statistics module:

1. **Intent** — what the notebook covers and why it matters
2. **Theory** — the definition and formula, stated plainly
3. **Code** — the same thing computed by hand, then with the library one-liner
4. **Simulation** — proof that the formula/algorithm matches reality
5. **Visualisation** — the picture that makes it stick
6. **Pitfalls** — the mistakes this topic invites, demonstrated rather than asserted
7. **Exercises** — four per notebook, each with a worked solution in the following cell

All randomness is seeded, so every number in the text matches what students will see.

## Teaching notes

- **Suggested pacing:** one notebook per 90-minute session; notebooks 5 (Clustering), 6 (Random
  Forest) and 9 (NLP) run long and may need two.
- **Cells are meant to be edited.** Ask students to change a hyperparameter (`k`, `C`, `max_depth`,
  number of clusters) and predict the result before running — the validation/learning curves are
  built for this.
- **Exercise solutions sit directly below each question.** For assessment, delete the solution
  cells before distributing, or ask students to attempt them in a copy first.
- **Recurring threads worth calling out explicitly:** every notebook compares against a naive
  baseline (`DummyClassifier`/`DummyRegressor`/seasonal-naive/majority-vote) before claiming a
  model works; every notebook that touches probabilities distinguishes ranking quality (AUC) from
  calibration (log loss/Brier); and feature scaling is revisited as "mandatory" for KNN, SVM,
  Naive Bayes' Gaussian variant, and clustering, but explicitly *not needed* for trees and forests.
- **Prerequisites:** the full [Statistical Foundations for Data Science](../6.%20Statistical%20Foundations%20for%20Data%20Science)
  module, particularly Notebooks 9–12 (regression, train/test split, overfitting, bias-variance).
- **Leads into:** [5. MLOps](../5.%20MLOps) for taking a model from a notebook to a served,
  monitored system, and [10. NLP](../10.%20NLP) for the deep-learning extension of Notebook 9's
  classical pipeline.
