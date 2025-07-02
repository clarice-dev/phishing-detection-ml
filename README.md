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
