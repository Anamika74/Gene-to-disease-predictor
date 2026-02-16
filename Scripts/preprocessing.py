# preprocessing.py

# This file contains the functions to pre-process the inputs taken from the front end

import sys
import os
from pathlib import Path

# Add the project root to sys.path to enable imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import pickle
from tensorflow.keras.utils import pad_sequences

# Get the absolute path to the model directory
MODEL_DIR = os.path.join(project_root, "Model")

# Load tokenizer
with open(os.path.join(MODEL_DIR, "tokenizer.pkl"), "rb") as f:
    tokenizer = pickle.load(f)

# Set max_len to what was used during training
max_len = 20  # Replace with your actual maxlen

def preprocess_input(gene_id, associated_genes, related_genes):
    # Create a single string just like in training
    combined_text = f"{gene_id} {associated_genes} {related_genes}".lower()
    
    print("Combined Text:", combined_text)  # Optional debug

    # Tokenize the combined string
    sequence = tokenizer.texts_to_sequences([combined_text])
    
    print("Tokenized Sequence:", sequence)  # Optional debug

    padded = pad_sequences(sequence, maxlen=max_len, padding='post')
    return padded


