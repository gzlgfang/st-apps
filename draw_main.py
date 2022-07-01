import streamlit as st
import matplotlib  as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False#坐标轴的负号正常显示
mpl.rcParams["font.size"]=24


def axes_settings(fig,ax,title):
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title)

x=np.linspace(0,3*np.pi,500)
y1=2*np.sin(x)
y2=3*np.cos(1.5*x)

fig,ax=plt.subplots(3,3,figsize=(15,15))#设置3×3图组
#绘制普通曲线
ax[0,0].plot(x,y1,lw=2)#绘制x和y1之间的函数曲线
title="Draw curve"
axes_settings(fig,ax[0,0],title)

#绘制散点趋势点图
x=np.random.rand(500)
y=np.random.rand(500)#随机产生500个0-1的数据
ax[0,1].scatter(x,y,color="blue")
title="Draw scatter graph"
ax[0,1].set_ylim(0,1)
axes_settings(fig,ax[0,1],title)

#绘制柱状图
x3=np.arange(1,7)
y3=[3,8,1,5,7,4]
ax[0,2].bar(x3,y3,color="bisque",align="center",hatch="//", edgecolor='g')
title="Draw bar chart"
axes_settings(fig,ax[0,2],title)

#绘制条状图
x4=np.arange(1,7)
y4=[3,8,1,5,7,4]
ax[1,0].barh(x4,y4,color="green",align="center",hatch="/", edgecolor='b')
title="Draw barh chart"
axes_settings(fig,ax[1,0],title)

#绘制直方图
x5=np.random.randint(0,8,100)#随机产生100个0-8之间的整数
bins=range(0,9,1)#数据统计的间隔及范围
ax[1,1].hist(x5,bins=bins,histtype="bar",rwidth=1,color="m",hatch="/",alpha=0.6, edgecolor='b')
title="Draw  histogram"
axes_settings(fig,ax[1,1],title)
ax[1,1].set_xlim(0,8)

#绘制饼图
mpl.rcParams["font.sans-serif"]=["SimHei"]#保证显示中文字
mpl.rcParams["axes.unicode_minus"]=False
labels=["math","chemical","physics","philosophy"]
students=[0.35,0.25,0.10,0.30]
colors=["red","blue","green","pink"]
explode=(0.1,0.1,0.1,0.1)
ax[1,2].pie(students,explode=explode,labels=labels,startangle=45,shadow=True,
        colors=colors,autopct="%3.1f%%")
ax[1,2].set_title("Pie chart drawing")

#绘制棉棒图
x6=np.linspace(1,10,10)
y6=np.random.randn(10)
ax[2,0].stem(x6,y6,linefmt="-.",markerfmt="*",basefmt="-")#linefmt=棉棒的样式，markerfmt=棉棒末端样式,basefmt=基线样式)
title="Draw stem "
axes_settings(fig,ax[2,0],title)

#绘制箱线图
x7=np.random.randn(800)
ax[2,1].boxplot(x7)
title="Draw  boxplot"
axes_settings(fig,ax[2,1],title)

#绘制误差图
x8=np.linspace(1,10,10)
y8=np.random.randn(10)
ax[2,2].errorbar(x8,y8,fmt="bo:",yerr=0.2,xerr=0.1)
title="Draw errorbar"
axes_settings(fig,ax[2,2],title)


#plt.show()
plt.tight_layout()
st.pyplot(fig)
