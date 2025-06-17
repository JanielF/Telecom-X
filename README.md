# Informe Final - Proyecto de Churn de Clientes

## 5.1. Introducción

Este informe documenta el análisis realizado en el proyecto **Churn de Clientes** para **Telecom X**, una empresa que atraviesa una elevada tasa de cancelaciones por parte de sus usuarios. El objetivo principal del análisis fue identificar los factores que influyen en el abandono del servicio, para generar acciones estratégicas basadas en datos que contribuyan a mejorar la retención de clientes.

Como asistente en el área de análisis de datos, se utilizó **Python** con bibliotecas como `pandas`, `matplotlib` y `seaborn`, desarrollando un flujo de trabajo alineado al paradigma **ETL (Extracción, Transformación y Carga)**. Posteriormente, se aplicó un proceso de **Análisis Exploratorio de Datos (EDA)**, permitiendo detectar patrones y relaciones significativas que fundamentan este informe.

---

## 5.2. Limpieza y Tratamiento de Datos

Antes de proceder al análisis, se garantizó la calidad del dataset mediante una exhaustiva etapa de limpieza y transformación. Los pasos incluyeron:

- **Eliminación de valores nulos**: Se identificaron columnas con datos ausentes (ej. `cargo_total`) y se eliminaron las filas correspondientes para evitar sesgos.
- **Conversión de tipos de datos**: Las variables categóricas con respuestas “Yes/No” fueron transformadas a enteros (`0/1`) para facilitar operaciones estadísticas.
- **Estandarización de nombres de columnas**: Todos los nombres fueron traducidos al español, en formato `snake_case`, para mejorar la legibilidad del análisis.
- **Creación de nuevas variables**:
  - `cargo_diario`: derivado de `cargo_mensual`, para analizar costos proporcionalmente.
  - `cantidad_servicios`: suma binaria de servicios contratados por cliente, representando el grado de compromiso.

Estas transformaciones fueron esenciales para estructurar un DataFrame coherente, listo para el análisis exploratorio.

---

## 5.3. Análisis Exploratorio de Datos (EDA)

Con el dataset limpio, se procedió a analizar el comportamiento de los clientes en relación al **churn** mediante estadísticas descriptivas y visualizaciones:

- **Distribución de evasión**:
  - Aprox. el **26%** de los clientes han abandonado el servicio.
  - Esta proporción se visualizó con un gráfico de barras, evidenciando la necesidad de intervención estratégica.

- **Relaciones con variables categóricas**:
  - Se analizaron variables como `tipo_de_contrato`, `factura_electronica`, `dependientes` y `forma_de_pago`.
  - Se utilizaron gráficos apilados para observar diferencias de churn dentro de cada categoría.

- **Relaciones con variables numéricas**:
  - Se utilizaron `boxplots` y `mapas de calor` para identificar relaciones con `meses_contrato`, `cargo_mensual`, `cargo_total` y `cantidad_servicios`.
  - Resultados clave:
    - Clientes con **más servicios contratados** tienden a permanecer.
    - Usuarios con **mayores cargos mensuales** o **menos tiempo con la empresa** presentan mayor propensión a la evasión.

- **Matriz de correlación**:
  - La variable `meses_contrato` mostró una correlación negativa fuerte con `churn`, indicando que los clientes más antiguos tienden a ser más leales.

---

## 5.4. Conclusiones e Insights

El análisis permitió identificar hallazgos clave que pueden fundamentar futuras estrategias de fidelización:

- **Antigüedad del cliente**: 
  - Existe una correlación clara entre **tiempo con la empresa** y **probabilidad de permanencia**.
  - Se recomienda enfocar estrategias en la **retención temprana**.

- **Percepción de costo**:
  - Los usuarios con cargos mensuales elevados tienden a abandonar más.
  - Es crucial revisar la **propuesta de valor percibida** o ajustar precios de forma segmentada.

- **Grado de compromiso**:
  - A mayor cantidad de servicios contratados (`cantidad_servicios`), menor tasa de churn.
  - Promover **paquetes integrados** podría mejorar significativamente la retención.

- **Factores personales**:
  - Clientes con pareja o dependientes presentan mayor fidelidad.
  - Estos perfiles pueden responder mejor a campañas familiares o de beneficios compartidos.

---

## 5.5. Recomendaciones

A partir de los hallazgos obtenidos, se sugieren los siguientes pasos:

1. **Implementación de modelos predictivos**:
   - Entrenar un modelo de clasificación que prediga el churn usando las variables más influyentes (`meses_contrato`, `cargo_mensual`, `cantidad_servicios`, etc.).

2. **Campañas dirigidas**:
   - Diseñar promociones para usuarios con alto riesgo de abandono (contratos mensuales, pocos servicios, cargos elevados).

3. **Onboarding optimizado**:
   - Mejorar la experiencia de nuevos clientes con el objetivo de convertirlos en usuarios de largo plazo.

4. **Segmentación estratégica**:
   - Identificar segmentos con alta retención y replicar características exitosas en clientes nuevos o inactivos.

---

## 📈 Recursos Adicionales

- Dataset original en formato JSON

---

Este informe representa una base sólida para el desarrollo de soluciones analíticas y predictivas que mejoren el desempeño de retención de clientes en **Telecom X**.
