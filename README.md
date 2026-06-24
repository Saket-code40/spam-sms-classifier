# 📩 Spam SMS Classifier

A Machine Learning web application that classifies SMS messages as **Spam** or **Not Spam (Ham)** using Natural Language Processing (NLP) and Streamlit.

## 🚀 Demo

Enter any SMS message and the model predicts whether it is spam or legitimate.

---

## 📌 Features

- SMS Spam Detection
- Text Preprocessing using NLTK
- Stopword Removal
- Stemming using Porter Stemmer
- TF-IDF Vectorization
- Machine Learning Classification
- Interactive Streamlit Web Interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- NLTK
- Scikit-Learn
- Pandas
- NumPy
- Pickle

---

## 📂 Project Structure

```text
Spam-Classifier/
│
├── main.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/spam-sms-classifier.git
cd spam-sms-classifier
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Linux/Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run main.py
```

---

## 🧠 Machine Learning Pipeline

1. Convert text to lowercase
2. Tokenization using NLTK
3. Remove special characters
4. Remove stopwords
5. Perform stemming
6. Convert text into numerical features using TF-IDF
7. Predict using trained ML model

---

## 📊 Example Messages

### Spam

```
Congratulations! You have won a FREE iPhone 16 Pro. Click here to claim your prize.
```

### Not Spam

```
Hey Saket, are you coming to Data Mining class today?
```

---

## 📈 Future Improvements

- Deploy on Streamlit Cloud
- Add confidence score
- Support multiple languages
- Improve model accuracy
- Add message history

---

## 👨‍💻 Author

**Saket Sharma**

Data Science Student | Machine Learning Enthusiast

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: Add your LinkedIn profile here

---

## ⭐ If you found this project useful, consider giving it a star.
