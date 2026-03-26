import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Regional Sales Forecast", layout="wide")

# Título
st.title("📊 Regional Sales Forecast Dashboard")

# Cargar datos
@st.cache_data
def load_data():
    data = pd.read_csv('regional_sales_forecast.csv')
    return data

df = load_data()

# Sidebar - Filtros
st.sidebar.header("🔍 Filtros")
years = sorted(df['Order Year'].unique())
selected_years = st.sidebar.multiselect("Selecciona años:", years, default=years)

regions = sorted(df['Region'].unique())
selected_regions = st.sidebar.multiselect("Selecciona regiones:", regions, default=regions)

# Filtrar datos
filtered_df = df[(df['Order Year'].isin(selected_years)) & (df['Region'].isin(selected_regions))]

# Métricas principales
st.sidebar.markdown("---")
st.sidebar.header("📈 Estadísticas")
total_sales = filtered_df['Sales'].sum()
avg_sales = filtered_df['Sales'].mean()

st.sidebar.metric("Total Ventas", f"${total_sales:,.0f}")
st.sidebar.metric("Promedio", f"${avg_sales:,.0f}")

# Gráficos principales
col1, col2 = st.columns(2)

# Gráfico 1: Ventas por Región
with col1:
    st.subheader("Ventas por Región")
    region_sales = filtered_df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
    fig1 = px.bar(region_sales, labels={'value': 'Ventas ($)', 'index': 'Región'})
    st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2: Ventas por Año
with col2:
    st.subheader("Ventas por Año")
    year_sales = filtered_df.groupby('Order Year')['Sales'].sum()
    fig2 = px.bar(year_sales, labels={'value': 'Ventas ($)', 'index': 'Año'})
    st.plotly_chart(fig2, use_container_width=True)

# Gráfico 3: Línea de tendencia
st.subheader("Tendencia de Ventas")
fig3 = px.line(filtered_df.sort_values('Order Year'), x='Order Year', y='Sales', color='Region', markers=True)
st.plotly_chart(fig3, use_container_width=True)

# Tabla de datos
st.subheader("📋 Datos Detallados")
st.dataframe(filtered_df.sort_values(['Order Year', 'Region']), use_container_width=True)
