"""This is the main file for the video game sales EDA project.
It uses Streamlit to create an interactive dashboard for exploring the dataset.
The dashboard includes summary statistics, a histogram of global sales,
a scatterplot of EU sales vs global sales,
and a bar graph of sales by year and country."""

import streamlit as st
import pandas as pd
import plotly.express as px


## main title ##
st.title("Video Game Sales EDA")
st.markdown(
    "Featuring video games popular in North America, Japan, Europe, and beyond, "
    "this dataset only includes titles with a minimum of 100k in global sales."
)

if "check_opt" not in st.session_state:
    st.session_state["check_opt"] = "Platform_Company"
if "check_bool" not in st.session_state:
    st.session_state["check_bool"] = False


## callback function
def update_state():
    """Updates the state of the checkbox
    and the corresponding option
    for coloring the scatterplot."""

    if st.session_state["check_bool"]:
        st.session_state["check_opt"] = "Platform"
    else:
        st.session_state["check_opt"] = "Platform_Company"


### upload the dataset ###
URL = "vgsales.csv"
df = pd.read_csv(URL)

### long dataset ###
df_long = df.melt(
    id_vars=[
        "Name",
        "Year",
        "Platform",
        "Platform_Generation",
        "Platform_Company",
        "Global_Sales",
    ],
    var_name="Country",
    value_name="Sales",
)

df_long["Country"] = df_long["Country"].apply(lambda x: x.split("_")[0])

## summary stats ##
st.divider()
st.caption("Sample Of The Dataset: Table 1")
st.write(df.sample(10))
st.divider()

summary_container = st.container()
with summary_container:
    st.subheader("Summary Statistics")

    col1_s, col2_s = st.columns(2)

    with col1_s:
        st.caption("Numeric Variables: Table 2")
        st.write(df.describe())

    with col2_s:
        st.caption("Categorical Variables: Table 3")
        st.write(df.describe(include="object"))

st.markdown(
    " - Table 2 is the summary of 9989 video games sales from 1990 to 2017, with average "
    "sales highest in North America (0.315 million), followed "
    "by Europe (0.179 million) and Japan (0.089 million). The maximum sales "
    "in North America reached 41.49 million compared to 29.02 million in Japan."
)

st.markdown(
    " - Table 3 contains 6925 unique game titles across 15 platform generations, "
    "with 'NBA Jam' being the most frequent title of 7 occurrences, "
    "and the PS2 as the dominant platform with 2127 games."
)

## my main cointainers ##
histogram_section = st.container()
bargraph_section = st.container()
scatterplot_section = st.container()
st.divider()

with histogram_section:
    st.divider()
    st.subheader("Histogram")

    fig = px.histogram(df, x="Global_Sales", title="Distribution Of Global Sales")
    st.plotly_chart(fig)


st.divider()
with scatterplot_section:
    st.divider()

    st.subheader("Scatterplot")

    fig = px.scatter(
        df, x="EU_Sales", y="Global_Sales", color=st.session_state["check_opt"]
    )

    st.plotly_chart(fig)

    st.checkbox("Game Console", value=False, key="check_bool", on_change=update_state)


with bargraph_section:
    st.divider()
    st.subheader("Bar Graph")

    fig = px.bar(
        df_long,
        x="Year",
        y="Sales",
        color="Country",
        hover_name="Sales",
        barmode="group",
        title="Video Game Sales Each Year By Country",
        labels={"Sales": "Sales (millions)"},
    )
    st.plotly_chart(fig)
