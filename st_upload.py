import streamlit as st
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# uploaded_files = st.file_uploader("Choose a excel file", accept_multiple_files=True)
# for uploaded_file in uploaded_files:
#      stf="g:/"+uploaded_file.name
#      DF = pd.read_csv(stf) 
#      # bytes_data = uploaded_file.read()
#      # st.write("filename:", uploaded_file.name)
#      # st.write(bytes_data)
     
     
#      #DF = pd.read_excel(stf, "Sheet1", na_filter=False, index_col=0)  # 共有31个城市坐标
#      # city_x = np.array(DF["x"])  # 数据分配
#      # city_y = np.array(DF["y"])
#      # st.write(city_x) 
#      st.write(DF)
# uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
# for uploaded_file in uploaded_files:
#      bytes_data = uploaded_file.read()
#      st.write("filename:", uploaded_file.name)
#      st.write(bytes_data)     
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     # To read file as bytes:
     # bytes_data = uploaded_file.getvalue()
     # st.write(bytes_data)

     # To convert to a string based IO:
     # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
     # st.write(stringio)

     # To read file as string:
     # string_data = stringio.read()
     # st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
     dataframe = pd.read_csv(uploaded_file)
     st.write(dataframe)
     st.write(dataframe.values[(0,1)])
     st.write(dataframe.values[(1,1)])
     x=dataframe.values[(1,1)]+dataframe.values[(2,1)]+dataframe.values[(3,1)]
     st.write(x)
     
