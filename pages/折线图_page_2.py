

# Contents of ~/my_app/pages/page_2.py
import streamlit as st
st.markdown("绘制折线图")

import matplotlib  as mpl               #导入主库
import matplotlib.pyplot as plt            #导入次库
import numpy as np                     #导入numpy库方便数据处理
mpl.rcParams["font.sans-serif"]=["SimHei"]   #保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False   #坐标轴的负号正常显示
fig=plt.figure()#可以省略，系统默认设置一个画布
x=np.linspace(0,10,100)
plt.plot(x,np.sin(2*x),'r',x,2*np.cos(2*x),'b')
plt.subplots_adjust(left  = 0.1 ,right = 0.9, bottom = 0.1,top = 0.9)#调整子图位置

st.pyplot(fig)
