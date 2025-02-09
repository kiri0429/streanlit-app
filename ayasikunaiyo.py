import streamlit as st
from PIL import Image
a=Image.open("GQEU6323.PNG")
st.title("おめでとうございます!100万円分の商品が無料になりました!")
title = st.text_input("ここにメールアドレスを入れたら商品をゲット！")
if title:
    print(title)
    st.image(a)