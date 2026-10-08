# 7. Machine Learning Fundamentals and Predictive Analytics

An 11-session practical module for undergraduate students. Each session teaches one family of machine learning
methods by using it to **build one small, real project on one real dataset**, from the raw data to a tested, saved
model. It follows the format of the [MLOps Skilling Course](../11.%20MLOps%20Skilling%20Course), and each session
ends by pointing to the MLOps session that takes the same kind of model into production.

## The ML project recipe

Every session follows the same seven stages, so that by the end of the module the workflow is a habit:

```
1. Frame     What exactly do we predict? How do we measure success? What is known at prediction time?
2. Split     Lock away a test set before looking at the data
3. Explore   The target, the strongest inputs, anything odd
4. Baseline  The score of a model that learns nothing: the number to beat
5. Build     Prepare the inputs and fit the model, inside one pipeline
6. Improve   Cross-validate, tune, interpret, look at the errors
7. Test      Score once on the locked test set; save the model
```

Sessions 5 (clustering), 10 (time series) and 11 (recommenders) show how the recipe changes when there are no labels,
when time order matters, and when the data is a users × items matrix.

## Delivery plan

| # | Session | Project | Dataset | Topics |
|---|---|---|---|---|
| 1 | [Linear Regression](1.%20Linear%20Regression.ipynb) | Predict students' final grades in September | [UCI Student Performance](https://archive.ics.uci.edu/dataset/320/student+performance) | Least squares by hand, gradient descent, MAE/RMSE/R², `ColumnTransformer` pipelines, coefficients, **leakage**, Ridge/Lasso |
| 2 | [Logistic Regression](2.%20Logistic%20Regression.ipynb) | Rank bank clients for a term-deposit call campaign | [UCI Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing) | Sigmoid, the accuracy trap, confusion matrix, precision/recall/F1, **thresholds**, ROC AUC vs PR AUC, odds ratios |
| 3 | [Decision Trees](3.%20Decision%20Trees.ipynb) | A heart-disease screening rule doctors can read | [UCI Heart Disease](https://archive.ics.uci.edu/dataset/45/heart+disease) | Gini by hand, reading a tree, overfitting, pre- and post-pruning, impurity vs permutation importance, instability |
| 4 | [K-Nearest Neighbors](4.%20K-Nearest%20Neighbors.ipynb) | Sort dry beans by variety from shape measurements | [UCI Dry Bean](https://archive.ics.uci.edu/dataset/602/dry+bean+dataset) | KNN by hand, **scaling**, choosing k, multi-class confusion matrix, curse of dimensionality, lazy learning |
| 5 | [Clustering](5.%20Clustering.ipynb) | Segment a wholesaler's customers | [UCI Wholesale Customers](https://archive.ics.uci.edu/dataset/292/wholesale+customers) | K-means by hand, log + scale, elbow and silhouette, profiling segments, stability, ARI, dendrograms, DBSCAN |
| 6 | [Random Forest](6.%20Random%20Forest.ipynb) | Predict which website visits end in a purchase | [UCI Online Shoppers Purchasing Intention](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset) | Bagging by hand, `max_features`, OOB score, tuning, permutation importance, partial dependence, gradient boosting |
| 7 | [Support Vector Machines](7.%20Support%20Vector%20Machines.ipynb) | Classify breast tumour samples, minimising missed cancers | [UCI Breast Cancer Wisconsin (Diagnostic)](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic) | Maximum margin, support vectors, `C`, kernel trick, `C` × `gamma` grid, decision-function thresholds |
| 8 | [Naive Bayes](8.%20Naive%20Bayes.ipynb) | An SMS spam filter that never hides real messages | [UCI SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection) | Bayes' theorem by hand, bag of words, Naive Bayes by hand, Laplace smoothing, variants, overconfident probabilities |
| 9 | [Introduction to NLP](9.%20Introduction%20to%20NLP.ipynb) | Sentiment of review sentences | [UCI Sentiment Labelled Sentences](https://archive.ics.uci.edu/dataset/331/sentiment+labelled+sentences) | Tokenisation, the stop-word trap, stemming, n-grams, TF-IDF by hand, error analysis, **domain shift** |
| 10 | [Time Series Analytics](10.%20Time%20Series%20Analytics.ipynb) | Forecast tomorrow's bike rentals | [UCI Bike Sharing](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset) | Time-based splits, decomposition, naive baselines, ACF and stationarity, SARIMA, lag features, `TimeSeriesSplit`, anomalies |
| 11 | [Recommender Systems](11.%20Recommender%20Systems.ipynb) | Recommend ten unseen films to each member | [MovieLens 100K](https://grouplens.org/datasets/movielens/100k/) | Utility matrix, bias model, content-based, item-item CF, **matrix factorisation (ALS) from scratch**, precision@10, cold start, popularity bias |

Work through them in order: later sessions assume the evaluation habits (baselines, pipelines, cross-validation,
honest test sets, thresholds) built in the earlier ones.

## How each notebook is structured

Each notebook follows the format of the [MLOps Skilling Course](../11.%20MLOps%20Skilling%20Course) guides and of
[6. Statistical Foundations for Data Science](../6.%20Statistical%20Foundations%20for%20Data%20Science):

- **Overview**: the project, learning goals, **Prerequisites** and the **Dataset**.
- **The ML project recipe** table, showing which steps cover which stage.
- Numbered **steps**: a short explanation, runnable code, then a **Read the output** note that points at the numbers
  that matter. Key ideas are computed **by hand first**, then with the library one-liner, and checked to match.
- **What you built**, **Where this goes in the MLOps course**, a **Common mistakes and fixes** table, and four
  **Exercises**.

## Setup

All eleven notebooks share one pinned `requirements.txt` in this folder. From this folder:

```bash
python3.11 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter notebook
```

| Package | Why we need it |
| --- | --- |
| ucimlrepo | Downloads the UCI datasets |
| scikit-learn | Models, pipelines, cross-validation and metrics (and `joblib` for saving models) |
| numpy, pandas | Arrays and tables |
| scipy | Dendrograms (Session 5) |
| statsmodels | Decomposition, stationarity test and SARIMA (Session 10) |
| nltk | The Porter stemmer (Session 9); no extra downloads needed |
| matplotlib | Charts |
| notebook, ipykernel | Running the notebooks |

Everything runs locally. No account or credentials are needed, only an internet connection: each notebook downloads
its dataset when it runs (through `ucimlrepo`, or as a zip file for Sessions 8, 9 and 11). Every notebook runs in
under 30 seconds except Session 4 (about a minute) and Session 6 (one to two minutes).

The notebooks ship without stored outputs. Each saves its final model to a `models/` folder next to the notebooks,
which Git ignores.

## Teaching notes

- **Suggested pacing:** one session per 90-minute slot. Sessions 2, 6 and 10 are the longest and may need two.
- **The "Read the output" notes are the lesson.** Each one quotes the numbers the cell actually prints with the
  versions in `requirements.txt` and fixed random seeds. If a learner's numbers differ in more than the last decimal
  place, check their library versions. (Timings in Session 4, Step 11 depend on the machine; the pattern does not.)
- **Ask students to predict before they run.** Most steps change one thing (a setting, an input, a split). Ask what
  will happen first.
- **Several results contradict a first impression.** These make good discussion points:
  - the best-looking inputs are leaks: period grades (Session 1), call duration (Session 2), and possibly page value
    (Session 6);
  - students who receive extra school support get a *negative* coefficient (Session 1): association, not causation;
  - logistic regression ties the tuned SVM (Session 7) and almost ties KNN (Session 4): try the simple model first;
  - random input subsets do not help the forest on this data, because one input dominates (Session 6);
  - removing stop words *hurts* sentiment analysis, because "not" is a stop word (Session 9);
  - random forests fail in one forecasting fold because trees cannot extrapolate beyond the training range
    (Session 10);
  - the best rating predictor makes worse recommendation lists than "most popular" (Session 11).
- **Every session has a judgement call.** The number of customer segments (Session 5), the threshold that trades
  missed cancers against false alarms (Session 7) or hidden messages against caught spam (Session 8), whether to use
  actual weather as a stand-in for forecasts (Session 10). Ask learners what they would decide and why.
- **Exercise solutions are not included**, so the exercises can be used for assessment.
- **Prerequisites:** [2. Python Intro and Math Foundation](../2.%20Python%20Intro%20and%20Math%20Foundation) (Python,
  numpy, pandas) and [6. Statistical Foundations for Data Science](../6.%20Statistical%20Foundations%20for%20Data%20Science),
  especially Sessions 9-12 (regression, train/test split, overfitting, bias-variance).
- **Leads into:** the [11. MLOps Skilling Course](../11.%20MLOps%20Skilling%20Course), where models like these are
  tracked, served, tested and monitored, and [10. NLP](../10.%20NLP) for deep-learning approaches to the text
  problems of Sessions 8 and 9.
