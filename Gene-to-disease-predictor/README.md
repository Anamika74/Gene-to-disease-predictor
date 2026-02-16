# 🧬 Gene-to-Disease Prediction System

An AI-powered system that uses **Natural Language Processing (NLP)** and **Deep Learning (LSTM)** to predict possible disease categories based on genetic sequences. This project bridges the gap between raw genomic data and human-readable medical insights using **Generative AI**.

---

## 🚀 Project Overview
This application takes genetic inputs (**Gene ID**, **Associated Genes**, and **Related Genes**) and predicts the **Top 3 most likely disease categories** with confidence scores. To make the results accessible, it integrates the **Google Gemini API** to provide simple, non-technical explanations for each predicted disease.

## 🧠 Technical Workflow
1.  **Data Cleaning:** Uses custom Regex parsing to handle complex genomic CSV data.
2.  **Feature Engineering:** Concatenates genetic markers into a textual sequence for NLP processing.
3.  **Clustering Logic:** To handle high disease cardinality (thousands of labels), the system uses **TF-IDF** and **K-Means Clustering** to group diseases into 15 broad categories.
4.  **Deep Learning Model:** An **LSTM (Long Short-Term Memory)** network captures the relationships between gene sequences.
5.  **Explainability:** The Gemini 1.5 Flash model converts clinical labels into "patient-friendly" descriptions.

## 🛠️ Tech Stack
* **Language:** Python
* **Deep Learning:** TensorFlow / Keras
* **NLP:** Tokenizer, TF-IDF, Padding
* **App Framework:** Streamlit
* **Generative AI:** Google Gemini API
* **Environment:** Dotenv for secure key management

## 📂 Repository Structure
```text
├── app.py                # Streamlit User Interface
├── predictor.py          # Model inference logic
├── preprocessing.py      # Text-to-sequence cleaning
├── gpt_api.py            # Gemini AI integration
├── model/                # Folder containing 
│   ├── trained_model_2.keras
│   ├── tokenizer.pkl
│   └── label_encoder.pkl
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation