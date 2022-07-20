import streamlit as st
global n
n=0
st.header("有关一字开头的成语学习")

st.subheader("第1题")
select=st.radio("下面有关一字的四个词组，哪个不是成语:",
     ('一成不变', '一个不剩', '一夫当关','一蹴而就'),horizontal=True)#前面题目，后面4个选项

if select == '一个不剩':  #这里填正确答案
     n=n+1
st.subheader("第2题")
select=st.radio("关于成语《一窍不通》解释正确的是:",
     ('只有一窍不通', '有一半不通', '有九窍不通','没有一窍是通的'),horizontal=True)

if select == '没有一窍是通的':
     n=n+1
st.subheader("第3题")
select=st.radio("成语《一望无垠》中的<垠>的发音正确的是:",
     ('yin第四声', 'yin第三声', 'gen第四声','gen第二声'),horizontal=True)

if select == 'yin第三声':
     n=n+1


st.write("你答对",n,"题")







