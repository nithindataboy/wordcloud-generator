import streamlit as st
import re
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random

# Download NLTK data if not present
nltk.download('stopwords')
nltk.download('punkt')

# Function to preprocess text
def preprocess_text(text):
    # Remove numbers and punctuation
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    # Tokenize and remove stopwords
    words = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

# Color functions
def random_color(word, font_size, position, orientation, random_state=None, **kwargs):
    return f"hsl({random.randint(0, 360)}, 70%, 50%)"

def blue_tones(word, font_size, position, orientation, random_state=None, **kwargs):
    return f"hsl({random.randint(200, 250)}, 70%, 50%)"

def vibrant(word, font_size, position, orientation, random_state=None, **kwargs):
    return f"hsl({random.randint(0, 360)}, 100%, 50%)"

color_funcs = {
    "Random": random_color,
    "Blue Tones": blue_tones,
    "Vibrant": vibrant
}

# Streamlit app with background image
st.markdown("""
<style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1506905925346-21bda4d32df4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80");
        background-size: cover;
        background-attachment: fixed;
    }
    .stApp > div > div > div {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 10px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.title("Word Cloud Generator")

text_input = st.text_area("Paste your text here (names, paragraphs, etc.)", height=200)

color_choice = st.selectbox("Choose color scheme", list(color_funcs.keys()))

if st.button("Generate Word Cloud"):
    if text_input.strip():
        processed_text = preprocess_text(text_input)
        if processed_text:
            wc = WordCloud(width=800, height=400, background_color='white', color_func=color_funcs[color_choice]).generate(processed_text)
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.imshow(wc, interpolation='bilinear')
            ax.axis('off')
            st.pyplot(fig)
        else:
            st.error("No valid words found after preprocessing.")
    else:
        st.error("Please enter some text.")
