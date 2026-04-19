import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Image Processing App", layout="wide")

st.title("✨ Image Processing Web App")

uploaded_file = st.file_uploader("Upload an Image")

if uploaded_file:
    img = Image.open(uploaded_file)
    img = np.array(img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    noisy = gray.copy()
    prob = 0.02
    rnd = np.random.rand(*gray.shape)
    noisy[rnd < prob] = 0
    noisy[rnd > 1 - prob] = 255

    filtered = cv2.medianBlur(noisy, 3)

    enhanced = cv2.equalizeHist(filtered)

    col1, col2 = st.columns(2)

    with col1:
        st.image(gray, caption="Gray")
        st.image(filtered, caption="Filtered")

    with col2:
        st.image(noisy, caption="Noisy")
        st.image(enhanced, caption="Enhanced")