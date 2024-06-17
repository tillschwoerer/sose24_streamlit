import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

# Initial Data Loading and Cleaning


@st.cache_data
def load_and_clean_data():
    df = pd.read_csv('wdi.csv')
    df = df.sort_values(
        ["name", "year"], ascending=True).reset_index(drop=True)
    df['gdp_capita'] = df.gdp / df.population
    return df


df = load_and_clean_data()


# Visualization
with st.sidebar:
    year = st.selectbox(label="Year", options=[1990, 2000, 2010, 2020])
    xvar = st.selectbox(label="x-variable",
                        options=['gdp_capita', 'population'])
    yvar = st.selectbox(label="y-variable",
                        options=['life_expectancy', 'suicides_100k'])
    colorvar = st.selectbox(label='Color-Variable',
                            options=['continent', 'income_level'])
    continents = st.multiselect(
        label="Continents", options=df.continent.unique())
    log_scale = st.toggle(label='Log Scale', value=False)

fig = px.scatter(df[(df.year == year) & (df.continent.isin(continents))], x=xvar, y=yvar,
                 color=colorvar, log_x=log_scale)

st.plotly_chart(fig, use_container_width=True)

st.dataframe(df)

####################
# Feature Requests
####################

# Button for Log Scale

# Different Types of Charts

# Selection of plotly theme
# Chain of actions: 1. Show plot, 2. User selects points on plot, 3. Additional information on these points are shown
