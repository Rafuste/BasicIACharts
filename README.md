# 📊 Regional Sales Forecast Dashboard

Una aplicación interactiva de **Streamlit** que visualiza datos de ventas regionales con gráficos dinámicos y filtros personalizados.

## 🎯 ¿Qué hace esta aplicación?

Esta aplicación proporciona un dashboard completo para analizar ventas por región y año:

- **Gráficos de Barras**: Visualiza las ventas totales por región y año
- **Gráfico de Líneas**: Muestra la tendencia de ventas a lo largo del tiempo para cada región
- **Filtros Interactivos**: Selecciona años y regiones específicas para análisis detallados
- **Estadísticas Resumidas**: Visualiza el total de ventas y promedio en tiempo real
- **Tabla de Datos**: Explora los datos completos en formato tabular

## 📋 Características

✅ Interfaz interactiva y fácil de usar  
✅ Filtros dinámicos por año y región  
✅ Visualizaciones con Plotly  
✅ Estadísticas en vivo en la barra lateral  
✅ Tabla de datos detallada y ordenable  

## 🚀 Cómo ejecutar la aplicación

### Requisitos previos
- Python 3.8 o superior instalado
- Conexión a internet (para descargar dependencias)

### Pasos para ejecutar

**1. Clona el repositorio:**
```bash
git clone https://github.com/Rafuste/BasicIACharts.git
cd BasicIACharts
```

**2. Instala las dependencias:**
```bash
python -m pip install -r requirements.txt
```

**3. Ejecuta la aplicación:**
```bash
python -m streamlit run app.py
```

**4. Abre en tu navegador:**
La aplicación se abrirá automáticamente en `http://localhost:8501`

## 📁 Estructura del proyecto

```
BasicIACharts/
├── app.py                          # Aplicación principal de Streamlit
├── regional_sales_forecast.csv     # Datos de ventas
├── requirements.txt                # Dependencias del proyecto
└── README.md                       # Este archivo
```

## 📊 Datos

El archivo `regional_sales_forecast.csv` contiene:
- **Order Year**: Año del registro (2014-2023)
- **Region**: Región geográfica (Central, East, South, West)
- **Sales**: Monto de ventas en dólares

## 🛠️ Tecnologías utilizadas

- **Streamlit** - Framework para crear apps web interactivas
- **Pandas** - Manipulación y análisis de datos
- **Plotly** - Visualización de gráficos interactivos
- **Python 3.14** - Lenguaje de programación

## 💡 Ejemplo de uso

1. Abre la aplicación
2. Usa los filtros en la barra izquierda para seleccionar años específicos
3. Selecciona las regiones que quieres analizar
4. Observa cómo se actualizan los gráficos automáticamente
5. Desplázate hacia abajo para ver la tabla de datos completa

## 🤝 Contribuciones

Si deseas mejorar esta aplicación, siéntete libre de hacer fork y enviar un pull request.

**Autor**: Rafuste  
**Fecha de creación**: Marzo 2026
