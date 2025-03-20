import streamlit as st
import pandas as pd
from datetime import datetime

# Función para registrar usuarios en Excel
def registrar_usuario(usuario):
    try:
        df = pd.read_excel("usuarios.xlsx")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Usuario", "Fecha"])
    nuevo_registro = pd.DataFrame({"Usuario": [usuario], "Fecha": [datetime.now()]})
    df = pd.concat([df, nuevo_registro], ignore_index=True)
    df.to_excel("usuarios.xlsx", index=False)

# Función para registrar operaciones en Excel
def registrar_operacion(usuario, operacion, resultado):
    try:
        df = pd.read_excel("operaciones.xlsx")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Usuario", "Operación", "Resultado", "Fecha"])
    nuevo_registro = pd.DataFrame({"Usuario": [usuario], "Operación": [operacion], "Resultado": [resultado], "Fecha": [datetime.now()]})
    df = pd.concat([df, nuevo_registro], ignore_index=True)
    df.to_excel("operaciones.xlsx", index=False)

# Interfaz de Streamlit
st.title("Calculadora con Registro")

usuario = st.text_input("Usuario")
if usuario:
    registrar_usuario(usuario)

   ##Input de los dígitos a operar
    num1 = st.number_input("Número 1", step=1, format="%d") 
    num2 = st.number_input("Número 2", step=1, format="%d")

    operacion = st.selectbox("Operación", ["+", "-", "*", "/"])

    if st.button("Calcular"):
        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                st.error("No se puede dividir por cero.")
                resultado = None

        if resultado is not None:
            st.write(f"Resultado: {resultado}")
            registrar_operacion(usuario, f"{num1} {operacion} {num2}", resultado)
else:
    st.warning("Por favor, ingresa un usuario.")