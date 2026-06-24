import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download NLTK resources if not already installed.
# This will only attempt downloads once per environment.
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []

    # Keep only alphanumeric words
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y
    y = []

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    for i in text:
        if i not in stop_words:
            y.append(i)

    text = y
    y = []

    # Stemming
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


# Load model and vectorizer
try:
    with open('vectorizer.pkl', 'rb') as f:
        tfidf = pickle.load(f)

    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError as exc:
    st.error(f"Required model file not found: {exc.filename}")
    st.stop()

st.title("Fake SMS Classifier")

input_sms = st.text_area("Enter the SMS message")

if st.button("Predict"):
    if not input_sms.strip():
        st.warning("Please enter a message before predicting.")
    else:
        transformed_sms = transform_text(input_sms)
        vectorized_sms = tfidf.transform([transformed_sms])
        prediction = model.predict(vectorized_sms)[0]

        if prediction == 1:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam")

