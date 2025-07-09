import streamlit as st

# ———————————— AVISO INICIAL ————————————
st.markdown("### AVISO IMPORTANTE")
st.markdown("**Todos los gases monoatómicos tienen el mismo valor de Cp y Cv.**")
st.markdown("**Cp = 20.8 kJ/kg·K** &nbsp;&nbsp;&nbsp;&nbsp; **Cv = 12.5 kJ/kg·K**")
st.markdown("---")

# ———————————— DATOS DE SUSTANCIAS ————————————
sustancias = {
    "Amoniaco (NH₃)": {
        "a": 27.568, "b": 2.5630 * 10**-2, "c": 0.99072 * 10**-5, "d": -6.699 * 10**-9, "M": 17.03
    },
    "Agua (vapor)": {
        "a": 32.24, "b": 0.1923 * 10**-2, "c": 1.055 * 10**-5, "d": -3.595 * 10**-9, "M": 18.02
    }
    # Puedes seguir agregando más sustancias aquí si deseas
}

# ———————————— FUNCIONES ————————————
def calcular_cp(a, b, c, d, T):
    return a + b*T + c*T**2 + d*T**3

def calcular_delta_u(a, b, c, d, T1, T2, R):
    delta_T = T2 - T1
    return (
        a * delta_T
        + b / 2 * (T2**2 - T1**2)
        + c / 3 * (T2**3 - T1**3)
        + d / 4 * (T2**4 - T1**4)
        - R * delta_T
    )

# ———————————— INTERFAZ ————————————
st.title("Cálculo de Cp y ΔU – Termodinámica")
st.markdown("**Autores: Juan Pablo Buitrago, Paula Cubillos, Santiago Villanueva**")

sustancia = st.selectbox("Selecciona una sustancia:", list(sustancias.keys()))
datos = sustancias[sustancia]

st.markdown(f"**Coeficientes:**")
st.code(f"a = {datos['a']}\nb = {datos['b']}\nc = {datos['c']}\nd = {datos['d']}")
st.markdown(f"Masa molar: **{datos['M']} kg/kmol**")

R_especifica = 8.314 / datos["M"]
st.markdown(f"Cálculo de R: 8.314 / {datos['M']} = **{R_especifica:.4f} kJ/kg·K**")

opcion = st.radio("¿Qué deseas calcular?", ("Cp a una temperatura", "ΔU entre dos temperaturas"))

if opcion == "Cp a una temperatura":
    T_celsius = st.number_input("Ingresa la temperatura (°C):", value=25.0)
    T_kelvin = T_celsius + 273.15
    cp_kmol = calcular_cp(datos["a"], datos["b"], datos["c"], datos["d"], T_kelvin)
    cp_kg = cp_kmol / datos["M"]

    st.markdown(f"**Conversión:** T = {T_celsius} °C = {T_kelvin:.2f} K")
    st.markdown(f"**Resultado antes de conversión:** Cp = {cp_kmol:.4f} kJ/kmol·K")
    st.markdown(f"**Resultado final:** Cp = {cp_kg:.4f} kJ/kg·K")

elif opcion == "ΔU entre dos temperaturas":
    T1_celsius = st.number_input("Temperatura inicial (°C):", value=25.0)
    T2_celsius = st.number_input("Temperatura final (°C):", value=100.0)
    T1_kelvin = T1_celsius + 273.15
    T2_kelvin = T2_celsius + 273.15

    delta_u_kmol = calcular_delta_u(
        datos["a"], datos["b"], datos["c"], datos["d"],
        T1_kelvin, T2_kelvin, 8.314
    )
    delta_u_kg = delta_u_kmol / datos["M"]

    st.markdown(f"**Conversión:** T1 = {T1_celsius} °C = {T1_kelvin:.2f} K | T2 = {T2_celsius} °C = {T2_kelvin:.2f} K")
    st.markdown(f"**Resultado sin conversión:** ΔU = {delta_u_kmol:.4f} kJ/kmol")
    st.markdown(f"**Resultado final:** ΔU = {delta_u_kg:.4f} kJ/kg")

    if delta_u_kg > 0:
        st.success("Interpretación: El sistema se calentó (ΔU positivo)")
    elif delta_u_kg < 0:
        st.warning("Interpretación: El sistema se enfrió (ΔU negativo)")
    else:
        st.info("Interpretación: No hubo cambio de energía interna (ΔU = 0)")
