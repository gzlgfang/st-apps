import streamlit as st
import numpy as np
import random as rnd
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime as dt
import time
import datetime

mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 18  # 设置字体大小
mpl.rcParams["ytick.right"] = True
mpl.rcParams["xtick.top"] = True
mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
mpl.rcParams["ytick.direction"] = "in"

# https://gzlgfang-st-apps/

# streamlit  run "g:/st-app/EEtest.py"

# 基层生态环工作人员知识学习考试系统
# 包含隐患排查与治理、法律法规、各类标准、信访回复、噪声检测与争议、水质检测与争议、废气检测与争议、土壤检测
# 单选题 str_test[序号] = ["下面有关一字的四个词组，哪个不是成语:", '一成不变', '一个不剩', '一夫当关', '一蹴而就']
# start_time = dt.now()
# start_time = time.time()
start_time = time.process_time()
answer = list()
str_test = 200 * [5 * ["NA"]]
# str_test = list()
# 隐患排查与治理：0-99，共100题
str_test[0] = [
    "企业环境安全隐患排查的时间为",
    "制定环境应急预案前",
    "制定环境应急预案中",
    "环境应急预案报备后",
    "任何时候",
]
str_test[1] = [
    "企业突发环境事件风险分级方法》中风险评估分析的M值是指",
    "风险物质数量与临界量比值",
    "突发环境事件风险物质临界量",
    "生产工艺过程与环境风险控制水平",
    "环境风险受体敏感程度",
]
str_test[2] = [
    "《突发环境事件应急管理办法》第三十八条规定未按规定开展环境安全隐患排查治理工作的可以处",
    "一万元以上二万元以下罚款",
    "一万元以上三万元以下罚款",
    "二万元以上三万元以下罚款",
    "三万元以上五万元以下罚款",
]
str_test[3] = [
    "企业对待环境安全隐患和风险的态度是",
    "发现隐患必须及时处理，而必要的风险允许存在",
    "发现隐患和风险都必须及时处理",
    "发现风险必须及时处理，而一般隐患允许存在",
    "发现隐患和风险都不必及时处理",
]
str_test[4] = [
    "环境安全隐患资料中常说的“一案三制”是指",
    "消防预案、体制、机制、法制",
    "突发环境事件应急预案、体制、机制、规制",
    "安全预案、体制、机制、法制",
    "突发环境事件应急预案、体制、机制、法制",
]
str_test[5] = ["中华人民共和国环境保护法》（第一版）通过的时间为", "1986年", "1989年", "2004年", "2005年"]
str_test[6] = [
    "水质检测中有一项指标简称SS,它的含义是",
    "水中化学耗氧量",
    "水中生物耗氧量",
    "水中悬浮固体含量",
    "水中细菌含量",
]
str_test[7] = [
    "广东省环境保护条例是哪一年通过的",
    "1998年",
    "2004年",
    "1996年",
    "2008",
]
str_test[8] = [
    "下面哪种物质不属于危险化学品",
    "84消毒液",
    "甲醇",
    "食用油",
    "乙醇",
]
str_test[9] = [
    "下面那一种不属于企业隐患排查方式",
    "综合排查",
    "全厂排查 ",
    "日常排查",
    "抽查",
]
str_test[10] = [
    "下面哪一种属于环境安全隐患一般分类方法中的一类",
    "特大隐患",
    "重大隐患",
    "较大隐患",
    "常规隐患",
]
str_test[11] = ["若空间不够，在保证安全的情况下，实验室废液桶可以叠放，最高不超过（ ）层。", "三层", "四层", "两层", "一层"]
str_test[12] = [
    "关于实验室安全规范，说法错误的是（ ）。",
    "实验室内应穿实验衣，必要时戴护目镜及口罩。",
    "进行化验时可以中途离开。",
    "不可用口或鼻直接尝、嗅化学试剂。",
    "实验室内不得嬉闹、吸烟、吃东西，不准用实验器皿盛装食物。",
]
str_test[13] = [
    "关于实验室个人防护措施，说法错误的是（ ）。",
    "为了防止工作服上附着的化学药品的扩散，工作服不得穿到其它公共场所如食堂、会议室等。",
    "在实验室中为了防止手受到伤害，可根据需要选戴各种手套。",
    "所有人员进入实验室都必须穿工作服，其目的是为了统一服装。",
    "工作人员应穿平底、防滑、合成皮或皮质的满口鞋，不得穿凉鞋、拖鞋、高跟鞋。",
]
str_test[14] = [
    "关于易燃易爆危险品的操作，错误的是（ ）。",
    "钾、钠操作时可以与水、卤代烷接触。",
    "操作、倾倒易燃液体，应远离火源。",
    "黄磷、金属钾、纳、氢化铝锉，氢化钠等自燃物，数量较大者应在防火实验室内操作",
    "接触可引起燃爆事故的性质不相容物，如氧化剂与易燃物，不得一起研磨。",
]
str_test[15] = ["下列物品不是剧毒物的是（ ）。", "氰化钠", "三氯化磷", "氢气", "乙酸汞"]
str_test[16] = [
    "下列物品相互接触时，可能会大量放热并着火、爆炸的有（ ）。",
    "水和乙醇",
    "高锰酸钾和浓硫酸",
    "四氯化碳和乙醇",
    "苯和四氯化碳",
]
str_test[17] = ["遇水会发生剧烈反应的有（ ）。", "乙醇", "苯", "四氯化碳", "金属钠"]
str_test[18] = ["下列药品常温下可以与水接触的是（ ）。", "金属钠", "电石", "白磷", "金属氢化物"]
str_test[19] = ["实验室常用的重铬酸钾洗液，当它失效时洗液颜色变为（ ）。", "绿色", "无色", "红色", "黄色"]
str_test[20] = [
    "苯酚毒性非常大，实验室发生苯酚泄露时，应该采取的措施是（ ）。",
    "用水冲洗",
    "直接扫走",
    "用酸处理",
    "用沙土，干燥石灰或苏打灰混合覆盖",
]

answer[0:11:1] = [3, 3, 2, 1, 4, 2, 3, 2, 3, 2, 2]

##100-199

###
global n, num, step
n = 0
num = 10
step = 1
# li = list(np.arange(0, 100))
# 从列表 items 中随机取出100 个元素，但不改变原列表。

add_selectbox = st.sidebar.radio(
    "选择做题内容", ("隐患排查与治理", "法律法规", "各类标准", "信访回复", "检测与争议", "综合")
)
if add_selectbox == "隐患排查与治理":
    name_test = "隐患排查与治理"
    sel_no = 1
elif add_selectbox == "法律法规":
    name_test = "法律法规"
    sel_no = 2
elif add_selectbox == "信访回复":
    name_test = "信访回复"
    sel_no = 3
elif add_selectbox == "检测与争议":
    name_test = "检测与争议"
    sel_no = 4
elif add_selectbox == "综合":
    name_test = "综合"
    sel_no = 5


# step=1#调试用
st.header("基层生态环境工作人员培训知识考试")
st.subheader("点击左上角的→可选择考试内容")

st.text("本软件代码由方利国开发")
st.text("发现错误之处请联系lgfang@scut.edu.cn,不胜感谢。")
st.text("点击左上方的>可以选择考试内容")
name = st.text_input("请输入您的姓名", "张三")
dt = datetime.datetime.now()
st.subheader("当前时间" + str(dt))

with st.form("my_form"):
    for i in range(10):
        str_k = "第" + str(i + 1) + "题"
        st.subheader(str_k)
        # k=test_num[i]
        k = i * step + (sel_no - 1) * 100
        k = int(k)
        select = st.radio(
            str_test[k][0],
            (str_test[k][1], str_test[k][2], str_test[k][3], str_test[k][4]),
            horizontal=True,
        )  # 前面题目，后面4个选项
        if select == str_test[k][answer[k]]:  # 这里填正确答案,目前题目从0-1199
            n = n + 1
    submitted = st.form_submit_button("点击提交")
    if submitted:

        # end_time = time.time()
        end_time = time.process_time()
        time_use = end_time - start_time
        # con_num=1
        str_finsh = "欢迎您" + name + ",已完成考试,试卷内容呢为" + name_test
        st.subheader(str_finsh)
        str_time = "考试用时" + str(time_use) + "秒"

        # st.subheader(str_time)
        # for i in range(num):
        # k=test_num[i]
        # if select ==str_test[k][answer[k-100]] :  #这里填正确答案,目前题目从100 199
        # n=n+1
        if n / num > 0.9:
            str_n = str(n)
            sstr = (
                "恭喜您答对"
                + str_n
                + "题,答对率为"
                + str(int(100 * 100 * n / num + 0.5) / 100)
                + "%，是个生态环境工作大行家"
            )
            st.subheader(sstr)
            # st.experimental_rerun()
        elif n / num > 0.6:
            str_n = str(n)
            sstr = (
                "恭喜您答对"
                + str_n
                + "题,答对率为"
                + str(int(100 * 100 * n / num + 0.5) / 100)
                + "%，本次成绩不错，还有提升空间"
            )
            st.subheader(sstr)
            # st.experimental_rerun()
        elif n / num <= 0.6:
            str_n = str(n)
            sstr = (
                "本次只答对"
                + str_n
                + "题,答对率为"
                + str(int(100 * 100 * n / num + 0.5) / 100)
                + "%，成绩不理想，请多多学习"
            )
            st.subheader(sstr)
        fig = plt.figure(num="Correct Answer Chart", figsize=(8, 8))
        labels = ["Correct", "Mistake"]
        C_M_data = [n / num, 1 - n / num]  # 正确与错误数据
        colors = ["lightblue", "red"]  # 颜色
        explode = (0.1, 0.1)  # 间隔距离，半径的比例
        plt.pie(
            C_M_data,
            explode=explode,
            labels=labels,
            startangle=45,
            shadow=True,
            colors=colors,
            autopct="%3.1f%%",
        )
        # st.subheader("*******答题对错率图******")
        plt.title("Question Answering Correct and Mistake Rate Chart")

        st.pyplot(fig)
        dt = datetime.datetime.now()
        st.subheader("当前时间" + str(dt))
        str_finsh1 = str_finsh + "请截屏成绩发给指定人员或地址"
        sstr = (
            "本次只答对"
            + str(n)
            + "题,答对率为"
            + str(int(100 * 100 * n / num + 0.5) / 100)
            + "%"
        )
        sstr = sstr + str_finsh1
        add_selectbox = st.sidebar.subheader(sstr)
        add_selectbox = st.sidebar.subheader("##若要继续考试可重新选择左边的答题内容##")
