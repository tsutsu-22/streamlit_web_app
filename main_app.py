import streamlit as st
from PIL import Image

st.title('サンプルアプリ')
st.caption('これはサンプルアプリです.')

img = Image.open('./data/cat.jpg')
st.image(img,width=200)
