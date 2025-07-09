
import streamlit as st

st.set_page_config(page_title="Cálculo Cp y ΔU – Termodinámica", layout="centered")

# Título principal
st.title("🧪 Termodinámica: Cálculo de Cp y ΔU")
st.markdown("##### Proyecto desarrollado por: Juan Pablo Buitrago Toro, Paula Cubillos y Santiago Villanueva")

st.markdown("---")
st.markdown("**AVISO IMPORTANTE**  
Todos los gases monoatómicos tienen el mismo valor de Cp y Cv.  
**Cp = 20.8 kJ/kg·K**  **Cv = 12.5 kJ/kg·K**")
st.markdown("---")

sustancias = [
    {"nombre": "Amoniaco", "formula": "NH₃", "a": 27.568, "b": 2.5630 * 10**-2, "c": 0.99072 * 10**-5, "d": -6.699 * 10**-9, "M": 17.03},
    {"nombre": "Agua (vapor)", "formula": "H₂O (g)", "a": 32.24, "b": 0.1923 * 10**-2, "c": 1.055 * 10**-5, "d": -3.595 * 10**-9, "M": 18.02},
    {"nombre": "Dióxido de carbono", "formula": "CO₂", "a": 22.26, "b": 5.981 * 10**-2, "c": -3.501 * 10**-5, "d": 7.469 * 10**-9, "M": 44.01},
    {"nombre": "Oxígeno", "formula": "O₂", "a": 25.48, "b": 1.520 * 10**-2, "c": -0.7155 * 10**-5, "d": 1.312 * 10**-9, "M": 32.00},
    {"nombre": "Aire", "formula": "Mezcla", "a": 28.11, "b": 0.1967 * 10**-2, "c": 4.802 * 10**-5, "d": -1.966 * 10**-9, "M": 28.97},
]

# Funciones
def calcular_cp(a, b, c, d, T):
    return a + b * T + c * T**2 + d * T**3

def calcular_delta_u(a, b, c, d, T1, T2, R):
    delta_T = T2 - T1
    return (
        a * delta_T
        + b / 2 * (T2**2 - T1**2)
        + c / 3 * (T2**3 - T1**3)
        + d / 4 * (T2**4 - T1**4)
        - R * delta_T
    )

# Selección de sustancia
nombres = [f"{s['nombre']} ({s['formula']})" for s in sustancias]
seleccion = st.selectbox("Selecciona la sustancia:", nombres)
s = sustancias[nombres.index(seleccion)]

st.markdown(f"**a = {s['a']} | b = {s['b']} | c = {s['c']} | d = {s['d']}**")
st.markdown(f"Masa molar **M = {s['M']} kg/kmol**")

R = 8.314 / s["M"]
st.markdown(f"Constante de gas: **R = 8.314 / {s['M']} = {R:.4f} kJ/kg·K**")

opcion = st.radio("¿Qué deseas calcular?", ["Cp a una temperatura", "ΔU entre dos temperaturas"])

if opcion == "Cp a una temperatura":
    T_C = st.number_input("Temperatura en °C", step=1.0, value=25.0)
    T_K = T_C + 273.15
    cp_kmol = calcular_cp(s["a"], s["b"], s["c"], s["d"], T_K)
    cp_kg = cp_kmol / s["M"]
    st.markdown(f"**Conversión:** T = {T_C} °C = {T_K:.2f} K")
    st.markdown(f"**Reemplazo:** Cp = {s['a']} + {s['b']}({T_K:.2f}) + {s['c']}({T_K:.2f}²) + {s['d']}({T_K:.2f}³)")
    st.markdown(f"**Resultado antes de conversión:** {cp_kmol:.4f} kJ/kmol·K")
    st.markdown(f"**Resultado final:** Cp = {cp_kg:.4f} kJ/kg·K")

elif opcion == "ΔU entre dos temperaturas":
    T1_C = st.number_input("Temperatura inicial (°C)", step=1.0, value=25.0)
    T2_C = st.number_input("Temperatura final (°C)", step=1.0, value=100.0)
    T1_K = T1_C + 273.15
    T2_K = T2_C + 273.15
    delta_u_kmol = calcular_delta_u(s["a"], s["b"], s["c"], s["d"], T1_K, T2_K, 8.314)
    delta_u_kg = delta_u_kmol / s["M"]
    st.markdown(f"**Conversión:** T1 = {T1_C} °C = {T1_K:.2f} K | T2 = {T2_C} °C = {T2_K:.2f} K")
    st.markdown(f"**Reemplazo:** ΔU = {s['a']}({T2_K - T1_K:.2f}) + {s['b']}/2({T2_K:.2f}² - {T1_K:.2f}²) + "
                f"{s['c']}/3({T2_K:.2f}³ - {T1_K:.2f}³) + {s['d']}/4({T2_K:.2f}⁴ - {T1_K:.2f}⁴) - {R:.4f}({T2_K - T1_K:.2f})")
    st.markdown(f"**Resultado sin conversión:** ΔU = {delta_u_kmol:.4f} kJ/kmol")
    st.markdown(f"**Resultado final:** ΔU = {delta_u_kg:.4f} kJ/kg")

    interpretacion = "se calentó (ΔU positivo)" if delta_u_kg > 0 else (
                     "se enfrió (ΔU negativo)" if delta_u_kg < 0 else
                     "no hubo cambio de energía interna")
    st.success(f"Interpretación: El sistema {interpretacion}")
