import streamlit as st
import pandas as pd
from datetime import datetime
import math

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

    # Inputs de los números
    num1 = st.number_input("Número 1", step=1, format="%d")
    num2 = st.number_input("Número 2", step=1, format="%d")

    operacion = st.selectbox("Operación", ["Sumar", "Restar", "Multiplicar", "Dividir", "Potencia", "Módulo", "Raíz"])

    if st.button("Calcular"):
        resultado = None  # Inicializar resultado

        if operacion == "Sumar":
            resultado = num1 + num2
        elif operacion == "Restar":
            resultado = num1 - num2
        elif operacion == "Multiplicar":
            resultado = num1 * num2
        elif operacion == "Dividir":
            if num2 != 0:
                resultado = num1 / num2
            else:
                st.error("No se puede dividir por cero.")
        elif operacion == "Potencia":
            resultado = num1 ** num2
        elif operacion == "Módulo":
            if num2 != 0:
                resultado = num1 % num2
                if resultado == 0:
                    st.warning("El residuo es 0, significa que la división es exacta.")
            else:
                st.error("No se puede calcular módulo con divisor 0.")
        elif operacion == "Raíz":
            if num1 >= 0:
                resultado = math.sqrt(num1)
            else:
                st.error("No se puede calcular la raíz cuadrada de un número negativo.")
                resultado = None

        # Mostrar el resultado solo si es válido
        if resultado is not None:
            st.success(f"Resultado: {resultado}")
            registrar_operacion(usuario, f"{num1} {operacion} {num2}", resultado)

else:
    st.warning("Por favor, ingresa un usuario.")
