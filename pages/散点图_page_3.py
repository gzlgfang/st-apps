
# Contents of ~/my_app/pages/散点图_page_2.py
import streamlit as st
st.markdown("绘制散点图")

#st.sidebar.markdown("绘制散点图")

import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
mpl.rcParams["font.size"]=18
fig=plt.figure(num="scatter_draw",figsize=(16,16))

ax1=plt.subplot(221)
ax2=plt.subplot(222)
ax3=plt.subplot(223)
ax4=plt.subplot(224)
#默认设置绘制
x=np.random.randn(300)
y=np.random.randn(300)#随机产生300个数据
ax1.scatter(x,y)
title="Default setting scatter plot"
ax1.set_title(title)
#统一标记大小颜色散点图
x=np.random.randn(300)
y=np.random.randn(300)#随机产生300数据
ax2.scatter(x,y,s=20,c="b")
title="Uniform marker size and color"
ax2.set_title(title)
#大小颜色随数据改变
x=np.random.randn(300)
y=np.random.randn(300)#随机产生300个数据
ax3.scatter(x,y,s=(20*x+10*y)**2,c=np.random.rand(300),cmap=mpl.cm.RdYlBu)
title="Size and color change with data"
ax3.set_title(title)
#添加连接线散点图
x=np.random.randn(300)
y=np.random.randn(300)#随机产生300个数据
ax4.scatter(x,y,s=70,c="r",marker="*",label="Red scatter plot",alpha=0.6)
title="Red scatter plot"
ax4.set_title(title)
#plt.subplots_adjust(wspace=0.2,hspace=0.3)
plt.tight_layout()#和上面adjust语句功能相同
st.pyplot(fig)

