

import streamlit as st

st.markdown("绘制柱状图")

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker
import matplotlib as mpl
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
x = np.arange(1, 13)
fig, ax1 = plt.subplots(figsize=(20, 9))
# 设置第一纵坐标轴的单位
ax1.yaxis.set_major_formatter(mticker.FormatStrFormatter('%d Ten thousand tons/Month'))
# 自定义横轴
ax1.set_xticklabels([str(i) + '月' for i in range(1, 13)], fontsize=18)
# 设置横轴 特定x值时显示刻度
ax1.set_xticks([i for i in range(1, 13, 1)])
ax1.tick_params(labelsize=20)
yxl = np.array([20, 30, 18, 40, 70, 100, 110, 150, 170, 190, 210, 200])
nxl = np.zeros(12)
s = 0
for i in range(0, 12):
    s = s + yxl[i]
    nxl[i] = s
plt.plot(x, yxl, 'g', label="Monthly sales weight")
# 显示网格
plt.grid(True)
plt.xlabel("Month", size=20)
plt.ylabel('Monthly sales weight', size=20)
plt.title("A company's methanol sales weight and summary chart", size=20)
# 设置线标的位置
plt.legend(loc='upper left')
plt.ylim(0, 220)
# 第二纵轴的设置和绘图
ax2 = ax1.twinx()
bar_width = 0.5
ax2.yaxis.set_major_formatter(mticker.FormatStrFormatter('%d 10 Thousand tons/month'))
plt.plot(x, nxl, 'r', label="Cumulative sales weight")
plt.bar(x, nxl, bar_width, label="Cumulative sales weight", align="center")
plt.legend(loc='upper right')
ax2.tick_params(labelsize=18)
ax2.set_ylabel("Cumulative sales weight", size=20)
# 限制横轴显示刻度的范围
plt.xlim(0, 13)
plt.ylim(0, nxl[-1] + 100)
st.pyplot(fig)

