# 4. ML Algorithms

A 12-session practical module on the core machine learning algorithms: regression, classification, clustering
and topic modelling. Each part starts by **building one algorithm from scratch** in NumPy, then moves to
scikit-learn, and ends with a **bootcamp**: an end-to-end project on a realistic dataset.

Every session works on a **real, public dataset**, downloaded by the notebook itself (from the UCI Machine Learning
Repository with [`ucimlrepo`](https://github.com/uci-ml-repo/ucimlrepo), or with scikit-learn), so there are no
CSV files to manage.

```
Part 1  Regression          Sessions 1-4    Predict a number       From scratch -> scikit-learn -> tree ensembles -> bootcamp
Part 2  Classification      Sessions 5-9    Predict a category     From scratch (x2) -> text pipelines -> multi-class -> bootcamp
Part 3  Clustering          Sessions 10-11  Find groups            From scratch -> bootcamp
Part 4  Topic modelling     Session 12      Find themes in text    LDA and NMF
```

## Delivery plan

| # | Session | Algorithms and topics | Dataset |
|---|---|---|---|
| 1 | [Linear Regression from Scratch with NumPy](1.%20Regression/1.%20Linear%20Regression%20from%20Scratch%20with%20NumPy.ipynb) | Cost function, gradient descent, learning rate, scaling, closed form, MAE/RMSE/R², residuals | [Combined Cycle Power Plant](https://archive.ics.uci.edu/dataset/294/combined+cycle+power+plant) |
| 2 | [Multiple Linear Regression with scikit-learn](1.%20Regression/2.%20Multiple%20Linear%20Regression%20with%20scikit-learn.ipynb) | Coefficients, collinearity, standardised coefficients, cross-validation, feature selection, polynomial features, overfitting | Combined Cycle Power Plant |
| 3 | [Tree Ensembles and Explaining Black-Box Regressors](1.%20Regression/3.%20Tree%20Ensembles%20and%20Explaining%20Black-Box%20Regressors.ipynb) | Decision trees, random forests, gradient boosting, permutation importance, partial dependence, SHAP | [Concrete Compressive Strength](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength) |
| 4 | [Bootcamp - Forecasting Bike-Sharing Demand](1.%20Regression/4.%20Bootcamp%20-%20Forecasting%20Bike-Sharing%20Demand.ipynb) | Target leakage, time-based splits, `TimeSeriesSplit`, one-hot encoding, log target, error analysis | [Bike Sharing](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset) |
| 5 | [Logistic Regression from Scratch with Gradient Descent](2.%20Classification/5.%20Logistic%20Regression%20from%20Scratch%20with%20Gradient%20Descent.ipynb) | Sigmoid, log-loss, decision boundary, L2 regularisation and `C`, confusion matrix, precision/recall, thresholds | [Breast Cancer Wisconsin (Diagnostic)](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic) |
| 6 | [Naive Bayes from Scratch - SMS Spam Filter](2.%20Classification/6.%20Naive%20Bayes%20from%20Scratch%20-%20SMS%20Spam%20Filter.ipynb) | Tokenising, Bayes' rule, Laplace smoothing, log-probabilities, `CountVectorizer`, `MultinomialNB` | [SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection) |
| 7 | [Text Classification Pipelines with scikit-learn](2.%20Classification/7.%20Text%20Classification%20Pipelines%20with%20scikit-learn.ipynb) | TF-IDF, character n-grams, linear SVM, average precision, grid search, threshold for a precision target, saving with `joblib` | SMS Spam Collection |
| 8 | [Multi-Class and Hierarchical Text Classification](2.%20Classification/8.%20Multi-Class%20and%20Hierarchical%20Text%20Classification.ipynb) | One-vs-rest, macro F1, large confusion matrices, flat vs top-down hierarchies, metadata leakage, multi-label | [20 Newsgroups](https://archive.ics.uci.edu/dataset/113/twenty+newsgroups) |
| 9 | [Bootcamp - Comparing Classifiers for Bank Marketing](2.%20Classification/9.%20Bootcamp%20-%20Comparing%20Classifiers%20for%20Bank%20Marketing.ipynb) | `ColumnTransformer`, seven classifiers compared fairly, ROC AUC vs accuracy, tuning, gains and lift | [Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing) |
| 10 | [k-Means Clustering from Scratch](3.%20Clustering/10.%20k-Means%20Clustering%20from%20Scratch.ipynb) | Lloyd's algorithm, inertia, local minima, k-means++, scaling, elbow and silhouette, ARI, cluster profiles | [Wine](https://archive.ics.uci.edu/dataset/109/wine) |
| 11 | [Bootcamp - Segmenting Wholesale Customers](3.%20Clustering/11.%20Bootcamp%20-%20Segmenting%20Wholesale%20Customers.ipynb) | Log transform, choosing k, hierarchical clustering and dendrograms, stability across algorithms, atypical customers | [Wholesale Customers](https://archive.ics.uci.edu/dataset/292/wholesale+customers) |
| 12 | [Topic Modelling with LDA](4.%20Topic%20Modelling/12.%20Topic%20Modelling%20with%20LDA.ipynb) | Bag of words, LDA, topic mixtures, perplexity vs readability, NMF, topics for new documents | 20 Newsgroups |

Work through them in order: each session builds on the ones before it, and says so in its **Prerequisites** line.

## How each notebook is structured

Each notebook follows the format of the [MLOps Skilling Course](../11.%20MLOps%20Skilling%20Course) guides and of
[6. Statistical Foundations for Data Science](../6.%20Statistical%20Foundations%20for%20Data%20Science): an
**Overview** with learning goals, **Prerequisites**, the **Dataset**, a **Where this fits** roadmap (marking the
current session), numbered **steps** (a short explanation, runnable code, then a **Read the output** note pointing
at the numbers that matter), **What this session hands to the next**, a **Common mistakes and fixes** table, and
**Exercises**. The bootcamps end with a summary table of every decision made and why.

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
| ucimlrepo | Downloads the UCI datasets |
| numpy, pandas | Arrays, tables, the from-scratch algorithms |
| scikit-learn | Models, pipelines, cross-validation, metrics; downloads 20 Newsgroups |
| scipy | The dendrogram (Session 11) |
| shap | Explaining individual predictions (Session 3) |
| joblib | Saving and loading a trained model (Session 7) |
| matplotlib | Charts |
| notebook, ipykernel | Running the notebooks |

Everything runs locally. No account or credentials are needed, only an internet connection to download the data
(the SMS Spam Collection comes as a zip file from UCI, and 20 Newsgroups is about 14 MB, cached after the first
run in `~/scikit_learn_data`). Most notebooks run in well under a minute; Sessions 9 and 12 take one to two
minutes.

## Slides

The slide decks are lecture companions: [Bootcamp.pptx](Bootcamp.pptx) (the machine-learning workflow and how to
choose between regression, classification and clustering), [Classification_naiveBayes.pptx](2.%20Classification/Classification_naiveBayes.pptx)
(Session 6) and [Clustering.pptx](3.%20Clustering/Clustering.pptx) (Session 10).

## Teaching notes

- **Suggested pacing:** one session per 60-90 minute slot; allow a double slot for each bootcamp (Sessions 4, 9, 11).
- **The "Read the output" notes are the lesson.** Each one quotes the numbers the cell actually prints with the
  versions in `requirements.txt`. If a learner's numbers differ in more than the last decimal place, check their
  library versions. Seeds are fixed, so every run gives the same numbers.
- **Several results contradict a first impression.** These make good discussion points:
  - with learning rate 0.001, gradient descent ends with a slope of the **wrong sign** (Session 1, Step 6);
  - humidity's coefficient **flips sign** when the other inputs are added (Session 2);
  - an unregularised logistic regression gets **worse on new data the longer it trains** (Session 5);
  - TF-IDF + naive Bayes looks terrible on recall but ranks almost as well as ever: a **threshold** problem,
    not a model problem (Session 7);
  - a top-down hierarchical classifier is **worse** than a flat one (Session 8);
  - shuffled cross-validation reports **half** the real forecasting error (Session 4).
- **Leakage appears in four forms**, worth naming explicitly: duplicate rows (Sessions 3 and 6), a target that is
  the sum of two inputs (Session 4), an input only known after the outcome (Session 9), and metadata that identifies
  the class (Session 8).
- **The from-scratch sessions** (1, 5, 6, 10) each end by matching scikit-learn exactly. Ask learners to predict the
  scikit-learn result before running that cell.
- **Prerequisites:** basic Python, NumPy and pandas; see
  [2. Python Intro and Math Foundation](../2.%20Python%20Intro%20and%20Math%20Foundation). Sessions 1, 5 and 6 refer
  back to [6. Statistical Foundations for Data Science](../6.%20Statistical%20Foundations%20for%20Data%20Science).
- **Leads into:** [7. Machine Learning Fundamentals and Predictive Analytics](../7.%20Machine%20Learning%20Fundamentals%20and%20Predictive%20Analytics),
  [10. NLP](../10.%20NLP) (after Sessions 6-8 and 12), and the [11. MLOps Skilling Course](../11.%20MLOps%20Skilling%20Course),
  which picks up where Session 7 stops: tracking, deploying and monitoring a saved model.
