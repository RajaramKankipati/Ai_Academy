import nbformat as nbf
import os

nb = nbf.v4.new_notebook()

cells = []

# 1. Introduction
cells.append(nbf.v4.new_markdown_cell("""# Text Summarization

## Introduction to Text Summarization
Text summarization is the process of distilling the most important information from a source (or sources) to produce an abridged version for a particular user or task.

There are two main approaches to text summarization:
1. **Extractive Summarization**: Identifies important sections of the text and crops out and stitches together portions of the content to produce a condensed version.
2. **Abstractive Summarization**: Produces important material in a new way. It involves interpreting and examining the text using advanced natural language techniques in order to generate a new shorter text that conveys the most critical information from the original text (much like humans do).
"""))

# Extractive Summarization
cells.append(nbf.v4.new_markdown_cell("""---
## 1. Extractive Summarization

Extractive summarization pulls the most important sentences from the original text based on certain statistical or linguistic metrics.
"""))

# 1.1 Rule-based
cells.append(nbf.v4.new_markdown_cell("""### 1.1 Rule-based Approach (Score Based on Word Frequencies)

One of the simplest methods is to score sentences based on the frequency of the words they contain. Words are weighted by their frequency, and sentences that contain high-frequency words are ranked higher.
"""))

cells.append(nbf.v4.new_code_cell("""import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

text = \"\"\"
Natural language processing (NLP) is an interdisciplinary subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data. The goal is a computer capable of "understanding" the contents of documents, including the contextual nuances of the language within them. The technology can then accurately extract information and insights contained in the documents as well as categorize and organize the documents themselves. Challenges in natural language processing frequently involve speech recognition, natural-language understanding, and natural-language generation.
\"\"\"

# Tokenize sentences and words
sentences = sent_tokenize(text)
stop_words = set(stopwords.words('english'))

# Calculate word frequencies
word_frequencies = {}
for word in word_tokenize(text.lower()):
    if word.isalnum() and word not in stop_words:
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

# Maximum frequency to normalize
max_frequency = max(word_frequencies.values())
for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word] / max_frequency)

# Calculate sentence scores
sentence_scores = {}
for sent in sentences:
    for word in word_tokenize(sent.lower()):
        if word in word_frequencies:
            if sent not in sentence_scores:
                sentence_scores[sent] = word_frequencies[word]
            else:
                sentence_scores[sent] += word_frequencies[word]

# Get the top 2 sentences
summarized_sentences = nlargest(2, sentence_scores, key=sentence_scores.get)
print("Rule-based Summary:")
print(" ".join(summarized_sentences))
"""))

# 1.2 Statistical (TF-IDF)
cells.append(nbf.v4.new_markdown_cell("""### 1.2 Statistical Approach (TF-IDF)

Term Frequency-Inverse Document Frequency (TF-IDF) can identify the most relevant sentences in a document without standard frequency bias for common words.
"""))

cells.append(nbf.v4.new_code_cell("""from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(sentences)

# Score sentences by the sum of their TF-IDF scores
sentence_scores_tfidf = np.array(tfidf_matrix.sum(axis=1)).flatten()

# Get indices of top 2 sentences
top_sentence_indices = sentence_scores_tfidf.argsort()[-2:][::-1]

# Reorder to original sequence
top_sentence_indices = sorted(top_sentence_indices)

print("Statistical (TF-IDF) Summary:")
for idx in top_sentence_indices:
    print(sentences[idx])
"""))

# 1.3 Graph-based
cells.append(nbf.v4.new_markdown_cell("""### 1.3 Graph-based Approach (TextRank)

TextRank is an algorithm based on PageRank. Sentences are modeled as vertices in a graph, and the edges between sentences represent their similarity.
"""))

cells.append(nbf.v4.new_code_cell("""import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity

# We can use the previously computed tfidf_matrix to compute sentence similarities
similarity_matrix = cosine_similarity(tfidf_matrix)

# Convert similarity matrix to a graph
nx_graph = nx.from_numpy_array(similarity_matrix)

# Compute TextRank scores
scores = nx.pagerank(nx_graph)

# Rank sentences
ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

print("Graph-based (TextRank) Summary:")
# Top 2 sentences
for i in range(2):
    print(ranked_sentences[i][1])
"""))

# Abstractive Summarization
cells.append(nbf.v4.new_markdown_cell("""---
## 2. Abstractive Summarization

Abstractive summarization uses advanced deep learning techniques to generate novel sentences that capture the essence of the source text.
"""))

# 2.1 Seq2Seq
cells.append(nbf.v4.new_markdown_cell("""### 2.1 Sequence-to-Sequence (Seq2Seq) Models

Seq2Seq models, originally developed for machine translation, consist of an Encoder (reads the input sequence) and a Decoder (generates the output sequence). The addition of the "Attention Mechanism" allows these models to focus on specific parts of the input when generating the summary.

*Note: Training a full Seq2Seq Model from scratch requires a significant amount of data and time. Below is pseudocode/structure of how one is typically set up in TensorFlow/Keras or PyTorch.*
"""))

cells.append(nbf.v4.new_code_cell("""# Typical Architecture Sketch of an Encoder-Decoder with Attention for Summarization

'''python
import tensorflow as tf
from tensorflow.keras.layers import Input, LSTM, Dense, Concatenate, Attention

# 1. Encoder
encoder_inputs = Input(shape=(max_text_len,))
# ... embedding layer ...
encoder_lstm = LSTM(latent_dim, return_sequences=True, return_state=True)
encoder_outputs, state_h, state_c = encoder_lstm(encoder_inputs)

# 2. Decoder
decoder_inputs = Input(shape=(max_summary_len,))
# ... embedding layer ...
decoder_lstm = LSTM(latent_dim, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(decoder_inputs, initial_state=[state_h, state_c])

# 3. Attention Layer
attention_layer = Attention()
attention_out = attention_layer([decoder_outputs, encoder_outputs])

# 4. Concat attention input and decoder output
decoder_concat = Concatenate(axis=-1)([decoder_outputs, attention_out])

# 5. Output Layer
decoder_dense = Dense(vocab_size, activation='softmax')
decoder_outputs = decoder_dense(decoder_concat)

model = tf.keras.models.Model([encoder_inputs, decoder_inputs], decoder_outputs)
model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy')
'''
print("Seq2Seq Architectures are the foundation of modern abstractive summarization models.")
"""))

# 2.2 Transformers
cells.append(nbf.v4.new_markdown_cell("""### 2.2 Transformer-based Models (HuggingFace)

Modern state-of-the-art summarization models are based on the Transformer architecture using pre-trained weights (like BART, T5, or Pegasus). 
Using the HuggingFace `transformers` library, we can easily leverage these models.
"""))

cells.append(nbf.v4.new_code_cell("""# Install transformers if necessary: !pip install transformers

from transformers import pipeline

# We initialize a summarization pipeline. It downloads a default model (like distilbart-cnn-12-6 or similar)
try:
    summarizer = pipeline("summarization")
    
    # A longer text for abstractive summarization
    long_text = \"\"\"
    The James Webb Space Telescope (JWST) is a space telescope designed primarily to conduct infrared astronomy. 
    As the largest space telescope in history, its greatly improved infrared resolution and sensitivity allow it to view objects too old, distant, or faint for the Hubble Space Telescope. 
    This is expected to enable a broad range of investigations across the fields of astronomy and cosmology, such as observation of the first stars and the formation of the first galaxies, and detailed atmospheric characterization of potentially habitable exoplanets.
    The US National Aeronautics and Space Administration (NASA) led JWST's design and development and partnered with two major agencies: the European Space Agency (ESA) and the Canadian Space Agency (CSA).
    \"\"\"
    
    # Generate abstractive summary
    summary = summarizer(long_text, max_length=50, min_length=25, do_sample=False)
    
    print("Abstractive (Transformer) Summary:")
    print(summary[0]['summary_text'])
except Exception as e:
    print("Could not run summarizer. Please ensure 'transformers' and 'torch'/'tensorflow' are installed.")
    print(f"Error: {e}")
"""))

nb.cells = cells

# Save the notebook in the appropriate folder
output_dir = '/Users/rajaramkankipati/Documents/GitHub/AI_academy/10. NLP/From language to information/14. Summarization'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_path = os.path.join(output_dir, 'Text_Summarization.ipynb')
with open(output_path, 'w') as f:
    nbf.write(nb, f)

print(f"Notebook successfully created at {output_path}")
