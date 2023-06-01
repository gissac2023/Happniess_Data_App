import streamlit as st
import pandas as pd
import plotly.express as px

st.title("In Search for Happiness")

select_x = st.selectbox("Select the data for the X-axis",
                        ("GDP", "Happiness", "Generosity"),
                        key="selector_x")
select_y = st.selectbox("Select the data for the X-axis",
                        ("GDP", "Happiness", "Generosity"),
                        key="selector_y")

st.header(f"{select_x} and {select_y}")


def load_data(x, y):
    df = pd.read_csv("happy.csv")
    x_out = df[f"{x.lower()}"]
    y_out = df[f"{y.lower()}"]
    return x_out, y_out


x_axis, y_axis = load_data(select_x, select_y)
figure = px.scatter(x=x_axis, y=y_axis,
                    labels={"x": f"{select_x}",
                            "y": f"{select_y}"})
st.plotly_chart(figure)
