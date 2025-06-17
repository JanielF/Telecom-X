import pandas as pd
import numpy as np
import os


def clear_output():
    """Clear the output of the console."""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS/Linux
        os.system('clear')  

clear_output()


url = 'https://raw.githubusercontent.com/ingridcristh/challenge2-data-science-LATAM/refs/heads/main/TelecomX_Data.json'
df = pd.read_json(url)

print(df.head())

#Extraccion de datos de columnas con diccionarios

df_customer = pd.json_normalize(df['customer'])
df_internet = pd.json_normalize(df['internet'])
df_account = pd.json_normalize(df['account'])
df_phone = pd.json_normalize(df['phone'])

df = pd.concat([df, df_customer, df_internet, df_account, df_phone], axis=1)

print(df.info())

datos_totales = df.drop(['customer', 'internet', 'account', 'phone'], axis=1)

print(datos_totales.head())

#Transformacion de datos

#Exploracion de datos

print(datos_totales.info())

print(datos_totales.dtypes)

#Significado de las columnas

#customerID: número de identificación único de cada cliente
#Churn: si el cliente dejó o no la empresa
#gender: género (masculino y femenino)
#SeniorCitizen: información sobre si un cliente tiene o no una edad igual o mayor a 65 años
#Partner: si el cliente tiene o no una pareja
#Dependents: si el cliente tiene o no dependientes
#tenure: meses de contrato del cliente
#PhoneService: suscripción al servicio telefónico
#MultipleLines: suscripción a más de una línea telefónica
#InternetService: suscripción a un proveedor de internet
#OnlineSecurity: suscripción adicional de seguridad en línea
#OnlineBackup: suscripción adicional de respaldo en línea
#DeviceProtection: suscripción adicional de protección del dispositivo
#TechSupport: suscripción adicional de soporte técnico, menor tiempo de espera
#StreamingTV: suscripción de televisión por cable
#StreamingMovies: suscripción de streaming de películas
#Contract: tipo de contrato
#PaperlessBilling: si el cliente prefiere recibir la factura en línea
#PaymentMethod: forma de pago
#Charges.Monthly: total de todos los servicios del cliente por mes
#Charges.Total: total gastado por el cliente

#Mas importantes:

#Churn
#tenure
#PhoneService
#MultipleLines
#InternetSecurity
#Contract
#Charges.Monthly
#Charges.Total

#Comprobación de incoherencias de los datos

print(datos_totales.isnull().sum())

# Verificar Valores duplicados

print(datos_totales.duplicated().sum())

# Verificar valores ausentes

print(datos_totales.isna().sum())

datos_ausentes = datos_totales['Charges.Total'].isna()
print(datos_totales[datos_ausentes])

datos_totales = datos_totales.dropna(subset=['Charges.Total'])

print(datos_totales)

# Verificar formato de columna float

datos_totales['Charges.Total'] = datos_totales['Charges.Total'].str.replace(' ','').replace('$', '').replace(',', '').replace('', None).astype(float)

datos_totales['Charges.Total'].dtype

datos_totales['customerID'].isnull().sum()

print(datos_totales['Churn'].value_counts())

datos_totales = datos_totales[datos_totales['Churn'] != '']

print(datos_totales['Churn'].value_counts())

print(datos_totales)

print(datos_totales['InternetService'].unique())

print(datos_totales.head())

print(datos_totales['Charges.Monthly'].unique())

#Cuentas Diarias

datos_totales['Charges.Daily'] = datos_totales['Charges.Monthly'] / 30

#Verficiar si se hizo la insercion correctamente de la nueva columna

print(datos_totales.head())

print(datos_totales.columns)

print(datos_totales['TechSupport'].isnull().sum())


#Estandariazación y transformación de datos

# Convirtiendo valores de columnas que sean Object 'Yes' o 'No' en valores binarios 1 y 0

columnas_binarias = [
    'Churn', 'Partner', 'Dependents', 'OnlineSecurity', 'OnlineBackup',
    'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
    'PaperlessBilling', 'PhoneService', 'MultipleLines'
]

datos_totales[columnas_binarias] = datos_totales[columnas_binarias].replace({'Yes': 1, 'No': 0})

print(datos_totales.head())

# Verificar todas las columnas para hacer los cambios de nombres respectivos
# y hacer más amena la lectura y analisis de datos

columnas = []
columnas = datos_totales.columns
print(columnas)

# Diccionario con los nombres en español, en minúsculas y separados con guión bajo

nombres_columnas_es = {
    'customerID': 'id_cliente',
    'Churn': 'churn',
    'gender': 'genero',
    'SeniorCitizen': 'adulto_mayor',
    'Partner': 'pareja',
    'Dependents': 'dependientes',
    'tenure': 'meses_contrato',
    'InternetService': 'servicio_internet',
    'OnlineSecurity': 'seguridad_en_linea',
    'OnlineBackup': 'respaldo_en_linea',
    'DeviceProtection': 'proteccion_dispositivo',
    'TechSupport': 'soporte_tecnico',
    'StreamingTV': 'tv_streaming',
    'StreamingMovies': 'peliculas_streaming',
    'Contract': 'tipo_contrato',
    'PaperlessBilling': 'factura_electronica',
    'PaymentMethod': 'metodo_pago',
    'Charges.Monthly': 'cargo_mensual',
    'Charges.Total': 'cargo_total',
    'PhoneService': 'servicio_telefonico',
    'MultipleLines': 'multiples_lineas',
    'Charges.Daily': 'cargo_diario'
}

# Renombrar columnas en el DataFrame
datos_totales = datos_totales.rename(columns=nombres_columnas_es)

# Verificación de cambios hechos

print(datos_totales.head())

print(datos_totales['metodo_pago'].unique())

# Cambiar el contenido de las columnas con valores object para traducirlas al
# español

datos_totales['genero'] = datos_totales['genero'].replace({'Female': 'Femenino', 'Male': 'Masculino'})
datos_totales['servicio_internet'] = datos_totales['servicio_internet'].replace({'Fiber optic': 'Fibra Óptica', 'DSL': 'DSL', 'No': 'No'})
datos_totales['tipo_contrato'] = datos_totales['tipo_contrato'].replace({'Month-to-month': 'Mensual', 'One year': 'Anual', 'Two year': 'Doble Anual'})
datos_totales['metodo_pago'] = datos_totales['metodo_pago'].replace({'Electronic check': 'Cheque Electrónico', 'Mailed check': 'Cheque Postal', 'Bank transfer (automatic)': 'Transferencia Bancaria Automática', 'Credit card (automatic)': 'Tarjeta de Crédito Automática'})

# Verificar que cambios y traducciones se hayan hecho correctamente

print(datos_totales.head(15))


#3.Carga y Análisis (L - Load & Analysis)

print(datos_totales.describe())

#3.2. Distribución de evasión

import matplotlib.pyplot as plt
import seaborn as sns

ax =sns.countplot(x='churn', data=datos_totales, palette=['#66bb6a', "#ef5350"])
plt.title('Proporción de clientes que permanecen en comparación a los que abandonaron')
plt.ylabel('Cantidad')
plt.xticks([0, 1], ['Permanecen', 'Abandonaron'])

for p in ax.patches:
    altura = p.get_height()
    ax.annotate(f'{altura}',
                (p.get_x() + p.get_width() / 2., altura),
                ha='center', va='bottom', fontsize=10, fontweight='bold')
plt.show()


#3.3. Recuento de evasión por variables categóricas

variables_categoricas = [
    'genero', 'pareja', 'dependientes', 'servicio_telefonico',
    'multiples_lineas', 'servicio_internet', 'seguridad_en_linea',
    'respaldo_en_linea', 'proteccion_dispositivo', 'soporte_tecnico',
    'tv_streaming', 'peliculas_streaming', 'tipo_contrato',
    'factura_electronica', 'metodo_pago'
]

for col in variables_categoricas:
    datos_totales.groupby(col)['churn'].value_counts(normalize=True).unstack().plot(
        kind='bar', stacked=True, color=['#66bb6a', '#ef5350']
    )
    plt.title(f'Proporción de Abandono por {col.replace("_", " ").title()}')
    plt.ylabel('Proporción')
    plt.xlabel(col.replace("_", " ").title())
    plt.legend(['Permanecen', 'Abandonan'])
    plt.tight_layout()
    plt.show()

#3.4. Conteo de evasión de variables numéricas

# Listar columnas numéricas

numericas = ['meses_contrato', 'cargo_mensual', 'cargo_total', 'cargo_diario']

# Explorando la evasión a traves de un bloxplots
import matplotlib.pyplot as plt
import seaborn as sns

for col in numericas:
    plt.figure(figsize=(7, 5))
    ax = sns.boxplot(x='churn', y=col, data=datos_totales, palette={'0':'#66bb6a', '1':'#ef5350'})
    plt.title(f'Distribución de {col.replace("_", " ").title()}')
    plt.ylabel(col.replace("_", " ").title())
    plt.xlabel('Evasión (0 = No, 1 = Sí)')

    # Agregar etiquetas para mejor claridad

    for grupo in datos_totales['churn'].unique():
        datos = datos_totales[datos_totales['churn'] == grupo][col].dropna()
        minimo = datos.min()
        maximo = datos.max()
        promedio = datos.mean()
        q3 = datos.quantile(0.75)

        # Posición de texto sobre la caja

        x_pos = grupo
        y_pos = q3 + (q3 * 0.05)

        etiqueta = (
            f'Mínimo: {minimo:.2f}\n'
            f'Máximo: {maximo:.2f}\n'
            f'Promedio: {promedio:.2f}'
        )

        ax.text(x = x_pos, y = y_pos, s = etiqueta, ha = 'center', fontsize = 9,
                bbox=dict(facecolor='white', alpha = 0.8, boxstyle='round'))

    plt.tight_layout()
    plt.show()