import nbformat as nbf

nb = nbf.v4.new_notebook()

cells = []

# 1. Introduction
cells.append(nbf.v4.new_markdown_cell("""# Text Classification

## Introduction to Text Classification
Text classification is the process of categorizing text into organized groups. By using Natural Language Processing (NLP) and other AI techniques, text classifiers can automatically analyze text and then assign a set of pre-defined tags or categories based on its content.

## Types of Text Classification
1. **Binary Classification**: Classifying text into one of two mutually exclusive classes (e.g., Spam vs. Not Spam, Positive vs. Negative Sentiment).
2. **Multi-class Classification**: Classifying text into one of three or more mutually exclusive classes (e.g., categorizing news into Sports, Politics, Tech).
3. **Multi-label Classification**: Assigning multiple labels to a single text instance (e.g., a movie review might be tagged as both "Action" and "Sci-Fi").
4. **Hierarchical Classification**: Classifying text into a structured taxonomy or hierarchy of categories (e.g., Electronics -> Mobile Phones -> Accessories).

For each type of classification, a typical Machine Learning pipeline involves:
- **Input**: The raw text data and labels.
- **Data Preprocessing**: Cleaning text (lowercasing, removing punctuation/stopwords, stemming/lemmatization).
- **Vectorization**: Converting text to numerical representations (BoW, TF-IDF, Word Embeddings).
- **Model Training**: Fitting a machine learning or deep learning model.
- **Prediction**: Generating predictions on unseen text.
- **Evaluation Metrics**: Assessing model performance (Accuracy, Precision, Recall, F1-Score, etc.).
"""))

cells.append(nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
import re
import nltk
from nltk.corpus import stopwords

# Ensure stopwords are downloaded
nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = text.split()
    tokens = [t for t in tokens if t not in stop_words]
    return ' '.join(tokens)
"""))

# 2. Binary Classification
cells.append(nbf.v4.new_markdown_cell("""## 1. Binary Text Classification
Classifying text into one of two exclusive categories.

**Example Task**: Sentiment Analysis (Positive vs. Negative)
"""))
cells.append(nbf.v4.new_code_cell("""from sklearn.linear_model import LogisticRegression

# 1. Input: Sample Data
data_binary = pd.DataFrame({
    'text': [
        'I love this product, it is amazing!',
        'This is the worst experience I have ever had.',
        'Absolutely fantastic service, highly recommend.',
        'Terrible quality, broke on the first day.',
        'It is okay, but I expected better.'
    ],
    'label': [1, 0, 1, 0, 0] # 1: Positive, 0: Negative
})

# 2. Data Preprocessing
data_binary['clean_text'] = data_binary['text'].apply(preprocess_text)

# Split data
X_train, X_test, y_train, y_test = train_test_split(data_binary['clean_text'], data_binary['label'], test_size=0.2, random_state=42)

# 3. Vectorization (TF-IDF)
vectorizer_bin = TfidfVectorizer()
X_train_vec = vectorizer_bin.fit_transform(X_train)
X_test_vec = vectorizer_bin.transform(X_test)

# 4. Model Training
model_bin = LogisticRegression()
model_bin.fit(X_train_vec, y_train)

# 5. Prediction
y_pred_bin = model_bin.predict(X_test_vec)

# 6. Evaluation Metrics
print("Binary Classification Results:")
print("Accuracy:", accuracy_score(y_test, y_pred_bin))
print(classification_report(y_test, y_pred_bin, zero_division=0))
"""))

# 3. Multi-class Classification
cells.append(nbf.v4.new_markdown_cell("""## 2. Multi-class Text Classification
Classifying text into one of three or more exclusive categories.

**Example Task**: Topic Categorization (Sports vs. Tech vs. Politics)
"""))
cells.append(nbf.v4.new_code_cell("""from sklearn.naive_bayes import MultinomialNB

# 1. Input: Sample Data
data_multi = pd.DataFrame({
    'text': [
        'The team won the championship match after a thrilling finale.',
        'The new smartphone features a revolutionary AI camera.',
        'The election results will be announced tomorrow by the council.',
        'Basketball players are preparing for the upcoming season.',
        'Tech giants are releasing new software updates.'
    ],
    'label': ['Sports', 'Tech', 'Politics', 'Sports', 'Tech']
})

# 2. Data Preprocessing
data_multi['clean_text'] = data_multi['text'].apply(preprocess_text)

# Split data
X_train, X_test, y_train, y_test = train_test_split(data_multi['clean_text'], data_multi['label'], test_size=0.2, random_state=42)

# 3. Vectorization (TF-IDF)
vectorizer_multi = TfidfVectorizer()
X_train_vec = vectorizer_multi.fit_transform(X_train)
X_test_vec = vectorizer_multi.transform(X_test)

# 4. Model Training
model_multi = MultinomialNB()
model_multi.fit(X_train_vec, y_train)

# 5. Prediction
y_pred_multi = model_multi.predict(X_test_vec)

# 6. Evaluation Metrics
print("Multi-class Classification Results:")
print("Accuracy:", accuracy_score(y_test, y_pred_multi))
print(classification_report(y_test, y_pred_multi, zero_division=0))
"""))

# 4. Multi-label Classification
cells.append(nbf.v4.new_markdown_cell("""## 3. Multi-label Text Classification
Assigning multiple relevant labels to each text instance.

**Example Task**: Movie Genre Tagging
"""))
cells.append(nbf.v4.new_code_cell("""from sklearn.tree import DecisionTreeClassifier
from sklearn.multioutput import MultiOutputClassifier

# 1. Input: Sample Data
data_multilabel = pd.DataFrame({
    'text': [
        'A futuristic space war with amazing visual effects and drama.',
        'A hilarious comedy about a group of friends going on a road trip.',
        'A terrifying monster haunts a small town in this thriller.',
        'A documentary about the history of artificial intelligence.',
        'An action-packed adventure in a fantasy world with magic.'
    ],
    # Labels: [Sci-Fi, Comedy, Action, Horror, Drama]
    'Sci-Fi': [1, 0, 0, 0, 0],
    'Comedy': [0, 1, 0, 0, 0],
    'Action': [1, 0, 0, 0, 1],
    'Horror': [0, 0, 1, 0, 0],
    'Drama':  [1, 0, 0, 0, 0]
})

target_cols = ['Sci-Fi', 'Comedy', 'Action', 'Horror', 'Drama']

# 2. Data Preprocessing
data_multilabel['clean_text'] = data_multilabel['text'].apply(preprocess_text)

# Split data
X_train, X_test, y_train, y_test = train_test_split(data_multilabel['clean_text'], data_multilabel[target_cols], test_size=0.2, random_state=42)

# 3. Vectorization (TF-IDF)
vectorizer_ml = TfidfVectorizer()
X_train_vec = vectorizer_ml.fit_transform(X_train)
X_test_vec = vectorizer_ml.transform(X_test)

# 4. Model Training
base_model = DecisionTreeClassifier(random_state=42)
model_ml = MultiOutputClassifier(base_model, n_jobs=-1)
model_ml.fit(X_train_vec, y_train)

# 5. Prediction
y_pred_ml = model_ml.predict(X_test_vec)

# 6. Evaluation Metrics
print("Multi-label Classification Results:")
for i, col in enumerate(target_cols):
    print(f"\\n--- {col} ---")
    print(classification_report(y_test.iloc[:, i], y_pred_ml[:, i], zero_division=0))
"""))

# 5. Hierarchical Classification
cells.append(nbf.v4.new_markdown_cell("""## 4. Hierarchical Text Classification
Classifying text into categories organized in a hierarchy (e.g., classifying a product first into "Electronics", then into "Laptops").

*Note: For simplicity, we demonstrate a two-level flat model approach or cascading approach where model 1 predicts the top level, and depending on output, model 2 predicts the sub-level.*
"""))
cells.append(nbf.v4.new_code_cell("""# 1. Input: Sample Data
data_hierarchical = pd.DataFrame({
    'text': [
        'The new smartphone has a great battery life.',
        'The latest television features a 4K OLED screen.',
        'I bought a new polo shirt for the summer.',
        'These running shoes are very comfortable.',
        'The gaming laptop overheats quickly.'
    ],
    'Level_1': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Electronics'],
    'Level_2': ['Mobile', 'TV', 'Shirts', 'Shoes', 'Laptop']
})

# 2. Data Preprocessing
data_hierarchical['clean_text'] = data_hierarchical['text'].apply(preprocess_text)

# Split (using a small sample so no train_test_split, just train and predict on same for demonstration)
X_text = data_hierarchical['clean_text']
y_l1 = data_hierarchical['Level_1']
y_l2 = data_hierarchical['Level_2']

# 3. Vectorization (TF-IDF)
vectorizer_h = TfidfVectorizer()
X_vec = vectorizer_h.fit_transform(X_text)

# 4. Model Training
# Level 1 Model
model_l1 = LogisticRegression()
model_l1.fit(X_vec, y_l1)

# For Level 2, typically we train separate models for each Level 1 category, 
# but for simplicity, we'll train one model for all subcategories here.
model_l2 = LogisticRegression()
model_l2.fit(X_vec, y_l2)

# 5. Prediction on a new sample
new_samples = ["I need a charger for my phone", "These sneakers are great for marathons"]
new_clean = [preprocess_text(t) for t in new_samples]
new_vec = vectorizer_h.transform(new_clean)

# Predict Level 1
pred_l1 = model_l1.predict(new_vec)
# Predict Level 2
pred_l2 = model_l2.predict(new_vec)

# 6. Evaluation / Output
print("Hierarchical Predictions:")
for text, l1, l2 in zip(new_samples, pred_l1, pred_l2):
    print(f"Text: '{text}' -> Level 1: {l1} -> Level 2: {l2}")
"""))

nb.cells = cells

# Save the notebook
output_path = '/Users/rajaramkankipati/Documents/GitHub/AI_academy/4. ML Algorithms/2. Classification/Text_Classification.ipynb'
with open(output_path, 'w') as f:
    nbf.write(nb, f)

print(f"Notebook successfully created at {output_path}")
