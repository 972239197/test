import streamlit as st

st.title("我的第一个 Streamlit 应用")
st.write("欢迎来到我的应用！")

name = st.text_input("请输入你的名字")
if name:
    st.success("你好，{name}!")
else:
    st.success("输入为空")