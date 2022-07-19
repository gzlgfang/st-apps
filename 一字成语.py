import streamlit as st
global n
n=0
st.header("有关一字开头的成语学习")

st.subheader("第1题")
select=st.radio("下面有关一字的四个词组，哪个不是成语:",
     ('一成不变', '一个不剩', '一夫当关','一蹴而就'),horizontal=True)

if select == '一个不剩':
     n=n+1
st.subheader("第2题")
select=st.radio("关于成语一窍不通解释正确的是:",
     ('只有一窍不通', '有一半不通', '有九窍不通','没有一窍是通的'),horizontal=True)

if select == '没有一窍是通的':
     n=n+1
st.write("你答对",n,"题")
