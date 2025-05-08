import streamlit as st
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load documents
def load_documents(folder_path):
    docs = []
    filenames = []
    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            with open(os.path.join(folder_path, file), 'r', encoding='utf-8', errors='ignore') as f:
                docs.append(f.read())
                filenames.append(file)
    return docs, filenames

# Process user query and return top matches
def search_documents(query, documents, filenames):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents + [query])
    similarity = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    scores = list(enumerate(similarity[0]))
    ranked = sorted(scores, key=lambda x: x[1], reverse=True)
    return [(filenames[i], documents[i][:500], round(score, 3)) for i, score in ranked[:5]]

# Streamlit UI
st.title("📜 AI-Powered Historical Document Search")
st.write("Upload .txt files and search using a natural language query.")

uploaded_files = st.file_uploader("Upload text files", accept_multiple_files=True)

if uploaded_files:
    folder_path = "uploaded_texts"
    os.makedirs(folder_path, exist_ok=True)
    for uploaded_file in uploaded_files:
        with open(os.path.join(folder_path, uploaded_file.name), "wb") as f:
            f.write(uploaded_file.read())

    documents, filenames = load_documents(folder_path)

    query = st.text_input("Enter your search query:")
    if query:
        results = search_documents(query, documents, filenames)
        st.subheader("🔍 Top Matches:")
        for filename, excerpt, score in results:
            st.markdown(f"**{filename}** (Score: {score})")
            st.text(excerpt + "...")
