import streamlit as st
import pickle

@st.cache_resource
def load_plots():
    plot_files = [
        "bar_plot",
        "box_bar",
        "box_plot_decade",
        "box_plot",
        "kde_plot",
        "line_chart",
        "map_graph",
    ]

    plots = {}

    for name in plot_files:
        with open(f"{name}.pkl", "rb") as file:
            plots[name] = pickle.load(file)

    return plots

plots = load_plots()

st.subheader('📈 CO₂ Emission Trend')
st.plotly_chart(plots["line_chart"], use_container_width=True)

st.divider()

st.subheader('CO₂ Emission by Country Map')
st.plotly_chart(plots["map_graph"], use_container_width=True)

st.divider()

st.plotly_chart(plots['bar_plot'],use_container_width=True)

st.divider()

st.subheader('Density Plot of Countries')
st.plotly_chart(plots['kde_plot'],use_container_width=True)

st.divider()

st.subheader('Variation of Carbon emission by top 12 countries')
st.plotly_chart(plots['box_plot'],use_container_width=True)

st.divider()

st.subheader('Variation of Carbon emission by top 12 countries')
st.plotly_chart(plots['box_plot_decade'],use_container_width=True)

st.divider()

st.subheader('Evolution of CO₂ Emissions Across Countries and Decades')
st.plotly_chart(plots['box_bar'],use_container_width=True)

