import streamlit as st
import  pandas as pd
st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("cat.png")

with col2:
    st.title("Cat the legend")
    st.write("hello whats up are you fine i the cat having extra knowledge of catching mouse")

content2 = """Hello this is content 2 written below here"""
st.write(content2)
df =pd.read_csv("data.csv",sep=";")

col3,empty_col, col4 = st.columns([1.5,0.5,1.5])
with col3:
    for index,row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image("images/" +row['image'])
        st.write(f"Source code :({row['url']})")


with col4:
    for index,row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image("images/" + row['image'])
        st.write(f"Source code :({row['url']})")

