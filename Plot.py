import altair as alt
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff


chart_data = pd.DataFrame(np.random.randn(500,5), columns = ["a","b","c","d","e"])
data = alt.Chart(chart_data).mark_circle().encode(x = "a", y = "b", size = "c", tooltip =["a","b","c","d","e"])
st.altair_chart(data)



df = pd.read_csv(r"C:\Users\hp\Downloads\geeks for geeks\streamlit\lang_data.csv")
lang_list = df.columns.tolist()
lang_choice = st.multiselect("please select your choice : ", lang_list)
new_df = df[lang_choice]
st.line_chart(new_df)
st.bar_chart(new_df)
st.area_chart(new_df)


df = pd.read_csv(r"C:\Users\hp\Downloads\geeks for geeks\streamlit\tips.csv")
st.dataframe(df.head(10))


data = px.pie(df,values = "total_bill" ,names = "day")
st.plotly_chart(data)
