# Quzer Tokenizer

Quzer is an experimental **Byte Pair Encoding (BPE)** tokenizer written in Python. It supports multilingual UTF-8 text, including Hindi, English, punctuation, and whitespace handling. This is the **first iteration** of a custom tokenizer project, designed with flexibility in mind — it's not production-ready yet, but serves as a strong starting point for further development.

---

## 🚀 Features (First Iteration)

- UTF-8 byte-level parsing
- Extraction of multi-byte character ranges (Hindi, etc.)
- Mixed handling of ASCII + multi-byte characters
- Pair generation from byte sequences
- Frequency-based vocabulary building with token IDs
- Outputs:
  - Decoded token pairs (ASCII + multi-byte)
  - Vocabulary with frequency counts and unique IDs

---

## 📦 Installation

Clone the repo and set up with `poetry`:

```bash
git clone https://github.com/Knoquant/quzer.git
cd quzer
poetry install
poetry run quzer