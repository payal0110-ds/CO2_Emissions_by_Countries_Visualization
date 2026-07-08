import streamlit as st
import pickle

st.set_page_config(
    page_title='CO₂ Emission Visualizations',
    page_icon='🌍',
    layout='wide'
)

st.title('Visualization: 🌍 CO2 Emissions World Wide from 1960 to 2018')

with open('bar_plot.pkl','rb') as file:
    bar_plot=pickle.load(file)
with open('box_bar.pkl','rb') as file:
    box_bar=pickle.load(file)
with open('box_plot_decade.pkl','rb') as file:
    box_plot_decade=pickle.load(file)
with open('box_plot.pkl','rb') as file:
    box_plot=pickle.load(file)
with open('kde_plot.pkl','rb') as file:
    kde_plot=pickle.load(file)
with open('line_chart.pkl','rb') as file:
    line_chart=pickle.load(file)
with open('map_graph.pkl','rb') as file:
    map_graph=pickle.load(file)

st.subheader('📈 CO₂ Emission Trend')
st.plotly_chart(line_chart,use_container_width=True)

st.divider()

st.subheader('CO₂ Emission by Country Map')
st.plotly_chart(map_graph,use_container_width=True)

st.divider()

st.plotly_chart(bar_plot,use_container_width=True)

st.divider()

st.subheader('Density Plot of Countries')
st.plotly_chart(kde_plot,use_container_width=True)

st.divider()

st.subheader('Variation of Carbon emission by top 12 countries')
st.plotly_chart(box_plot,use_container_width=True)

st.divider()

st.subheader('Variation of Carbon emission by top 12 countries')
st.plotly_chart(box_plot_decade,use_container_width=True)

st.divider()

st.subheader('Evolution of CO₂ Emissions Across Countries and Decades')
st.plotly_chart(box_bar,use_container_width=True)