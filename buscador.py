import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN VISUAL DE LA PÁGINA
st.set_page_config(page_title="Buscador", layout="centered")

# Títulos principales
st.title("🔍 Buscador")
st.write("Cargue el archivo CSV y seleccione el método de búsqueda.")

# Componente para subir el archivo
archivo_csv = st.file_uploader("Arrastrá acá tu archivo .csv", type="csv")

# 2. FUNCIÓN DE CARGA
# 2. FUNCIÓN DE CARGA
@st.cache_data
def procesar_datos(file):
    df = pd.read_csv(file, sep=';', dtype=str, encoding='latin-1')
    df.columns = df.columns.str.strip()
    if 'NRO.CUIT' in df.columns:
        df = df.rename(columns={'NRO.CUIT': 'CUIT'})
        
    return df

# 3. LÓGICA DE INTERACCIÓN
if archivo_csv:
    df = procesar_datos(archivo_csv)
    st.success(f"Archivo processed con éxito. Total: {len(df):,} registros.")
    
    st.markdown("---")

    modo = st.radio("Buscar por:", ["CUIT", "Razón Social"])

    if modo == "CUIT":
        cuit_buscado = st.text_input("Ingresá el CUIT:")
    
        if cuit_buscado:
            termino_cuit = cuit_buscado.strip()
        
            # VALIDACIÓN DE CUIT: ¿Son solo números?
            if not termino_cuit.isdigit():
                st.warning("⚠️ El CUIT solo debe contener números (sin letras, guiones ni puntos).")
                resultado = pd.DataFrame()  # Creamos un resultado vacío para evitar errores
            else:
                # Si pasa la validación, hace el filtrado inteligente
                if len(termino_cuit) == 1:
                    filtro = df['CUIT'].str.strip().str.startswith(termino_cuit, na=False)
                else:
                    filtro = df['CUIT'].str.strip().str.contains(termino_cuit, na=False)
                resultado = df[filtro]
    
    else:
        nombre_buscado = st.text_input("Ingresa la RAZON SOCIAL:")
        
        if nombre_buscado:
            termino = nombre_buscado.upper().strip()
            
            # VALIDACIÓN DE RAZÓN SOCIAL: ¿Tiene números?
            texto_sin_espacios = termino.replace(" ", "")
            
            if texto_sin_espacios and not texto_sin_espacios.isalpha():
                st.warning("⚠️ La Razón Social no debería contener números.")
                resultado = pd.DataFrame()  # Resultado vacío
            else:
                # Si pasa la validación, busca normalmente
                if len(termino) == 1:
                    filtro = df['RAZON SOCIAL'].str.upper().str.startswith(termino, na=False)
                else:
                    filtro = df['RAZON SOCIAL'].str.upper().str.contains(termino, na=False)
                resultado = df[filtro]

    # 4. MOSTRAR RESULTADOS
    if (modo == "CUIT" and cuit_buscado) or (modo == "Razón Social" and nombre_buscado):
        if not resultado.empty:
            st.write(f"Se encontraron {len(resultado)} coincidencia(s):")
            
            # Mostrar tabla de resultados
            st.dataframe(resultado)
        else:
            st.error("No se encontraron resultados para tu búsqueda.")
else:
    st.info("cargue el archivo CSV para habilitar el buscador.")