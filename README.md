# 🧬 Gene-to-Disease Prediction System

An AI-powered system that transforms raw genomic data into meaningful disease insights using **Natural Language Processing (NLP)**, **Deep Learning (LSTM)**, and **Generative AI**.

This project demonstrates how machine learning can bridge the gap between complex gene sequences and human-readable medical interpretation.

---

## 🚀 Project Overview

The **Gene-to-Disease Prediction System** accepts structured genetic inputs:

* **Gene ID**
* **Associated Genes**
* **Related Genes**

It predicts the **Top 3 most probable disease categories** along with confidence scores.

To improve accessibility, the system integrates **Google Gemini (1.5 Flash)** to generate **simple, non-technical explanations** for each predicted disease category.

> 🎯 Goal: Convert raw genomic signals into understandable medical insights.

---

## 🧠 Technical Workflow

### 1️⃣ Data Cleaning

* Custom **Regex parsing** handles complex genomic CSV structures.
* Resolves nested commas, quoted strings, and malformed entries.

### 2️⃣ Feature Engineering

* Concatenates genetic markers into structured textual sequences.
* Prepares data for NLP tokenization and sequence modeling.

### 3️⃣ Disease Cardinality Reduction (Clustering)

* Thousands of disease labels grouped into **15 broad disease categories**.
* Implemented using:

  * **TF-IDF Vectorization**
  * **K-Means Clustering**
* Reduces label sparsity and improves model generalization.

### 4️⃣ Deep Learning Model

* **LSTM (Long Short-Term Memory) Network**

  * Captures sequential dependencies in gene representations.
  * Learns latent relationships between gene patterns and disease categories.

### 5️⃣ Explainability with Generative AI

* Integrates **Gemini 1.5 Flash** model.
* Converts clinical labels into **patient-friendly explanations**.
* Enhances usability for non-technical users.

---

## 🛠️ Tech Stack

| Category      | Technology                 |
| ------------- | -------------------------- |
| Language      | Python                     |
| Deep Learning | TensorFlow / Keras         |
| NLP           | Tokenizer, TF-IDF, Padding |
| Clustering    | K-Means                    |
| App Framework | Streamlit                  |
| Generative AI | Google Gemini API          |
| Environment   | Dotenv                     |
| Serialization | Pickle                     |

---

## 📂 Repository Structure

```
├── app.py                # Streamlit user interface
├── predictor.py          # Model inference logic
├── preprocessing.py      # Text cleaning & sequence processing
├── gpt_api.py            # Gemini API integration
├── model/                # Trained model & encoders
│   ├── trained_model_2.keras
│   ├── tokenizer.pkl
│   └── label_encoder.pkl
├── Data/                 # Genomic datasets
├── requirements.txt      # Dependencies
├── .gitignore            # Ignored files
└── README.md             # Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Anamika74/Gene-to-disease-predictor.git
cd Gene-to-disease-predictor
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```
YOUR_GEMINI_API_KEY=your_actual_api_key_here
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 📊 Model Performance

* ✅ ~89% **Top-3 Accuracy**
* Reduced thousands of disease labels to **15 clustered categories**
* Improved prediction stability through cardinality reduction

---

## 🎯 Key Highlights

* **End-to-End ML Pipeline**
  Raw genomic data → NLP processing → Clustering → LSTM → Explainable Output

* **Hybrid AI Architecture**
  Predictive Deep Learning + Generative AI Explainability

* **Modular Codebase**
  Clean separation between preprocessing, inference, and UI layers

* **Practical GenAI Integration**
  Demonstrates real-world use of LLMs beyond conversational AI

---

## 🧪 Future Improvements

* Integrate **Attention Mechanisms** for enhanced interpretability
* Add **Model Evaluation Dashboard** in Streamlit
* Support multi-gene batch predictions
* Deploy using **Docker / Cloud Platforms**

---

## ⚠️ Disclaimer

This system is built for **educational and research purposes only**.
It is **not intended for clinical diagnosis or medical decision-making**.

---

## 👩‍💻 Author

**Anamika Sharma**

