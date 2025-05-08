
# 📜 AI-Powered Historical Document Search

A lightweight and interactive app to search through historical `.txt` documents using **cosine similarity**, **TF-IDF**, and **natural language queries**. Built with **Python** and **Streamlit** for fast prototyping and sharing.

---

## 🚀 Features
- Upload `.txt` files from historical sources (e.g., Project Gutenberg)
- Enter a search query and get top 5 matching documents
- Uses TF-IDF vectorization and cosine similarity
- Clean and user-friendly UI with Streamlit
- Easy to deploy and extend

---

## 📁 Project Structure

```
historical-search-app/
│
├── app.py    # Main Streamlit app
├── requirements.txt                     # Python dependencies
└── research.txt                           # Optional: Sample text file for testing
```

---

## 🔧 Requirements

- Python 3.7+
- streamlit
- pandas
- scikit-learn
- nltk (optional, if using stopwords)

---

## 💻 Run Locally

```bash
pip install -r requirements.txt
streamlit run historical_document_search_app.py
```

---

## 🌍 Live Demo (Optional)

Deploy on []() by connecting this repo and selecting the main script.

---

## 📚 Sample Text Sources

- Project Gutenberg: https://www.gutenberg.org/
- Internet Archive: https://archive.org/

---

## 🙌 Contributing

Feel free to fork this project and enhance it with:
- OCR for scanned files
- BERT or GPT-based search
- Multilingual support
- Archive metadata visualization

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---
