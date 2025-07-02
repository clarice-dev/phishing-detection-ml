# phishing-detection-ml
A ML model that predicts if a URL or email is a phishing attempt based on known features (e.g., URL length, HTTPS, domain age, etc.)

---
## 🚀 Project Status

✅ Dataset prepared  
✅ Feature/target separation  
✅ Train-test split  
✅ Trained Random Forest & XGBoost  
✅ Compared models using accuracy, precision, recall, and F1  
✅ Visualized model performance

---

## 🧠 Overview

Phishing attacks remain one of the most common cybersecurity threats. This project trains a supervised machine learning model to detect phishing URLs using engineered features like:

- URL length
- Presence of special characters
- HTTPS usage
- Domain information (age, prefix, etc.)

This model can be used as a foundational element in anti-phishing systems or browser extensions.

---

## 📂 Files Included

| File | Description |
|------|-------------|
| `phishing_detection.ipynb` | Main Google Colab notebook |
| `README.md` | Project summary and steps |

---

## 🧑‍💻 Getting Started

### 🔧 Requirements

- Python 3.7+
- Libraries:
  - pandas
  - scikit-learn
  - xgboost
  - seaborn
  - matplotlib
---
## 📊 Dataset

- Source: [Kaggle - Phishing Website Detector](https://www.kaggle.com/datasets/eswarchandt/phishing-website-detector)
- 11,000+ rows, 30 features
- Target: `class` (converted from `-1, 1` to `0, 1`)

---

- Source: [Kaggle - Phishing Website Detector](https://www.kaggle.com/datasets/eswarchandt/phishing-website-detector)
- 11,000+ rows, 30 features
- Target: `class` (converted from `-1, 1` to `0, 1`)

---

## 🔍 Features Used

| Feature                        | Description                                     |
|-------------------------------|-------------------------------------------------|
| URL Length                    | Total character count in the URL               |
| Uses HTTPS                    | Whether the URL uses HTTPS protocol            |
| Contains `@`, `//`, or `-`    | Common signs of phishing URLs                  |
| Has IP Address                | If the domain is an IP instead of text         |
| Subdomain Count               | Number of subdomains in the URL                |
| URL Shortening Service Used   | Checks if known shortening service is used     |
| Domain Age                    | Age of the domain (if WHOIS data is available) |

---

## ⚙️ Model Comparison

| Metric    | Random Forest | XGBoost |
|-----------|----------------|----------|
| Accuracy  | 94%           | 94%     |
| Precision | 94%           | 94%     |
| Recall    | 98%           | 96%     |
| F1 Score  | 98%           | 96%     |

---

## 🧠 Key Concepts Used

- Binary classification
- Confusion matrix, precision, recall, F1-score
- RandomForestClassifier, XGBClassifier
- Model comparison and performance visualization

---


## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📜 License

[MIT](LICENSE)

## 🧪 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/clarice-dev/phishing-detection-ml.git
cd phishing-detection-ml
