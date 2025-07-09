import streamlit as st

# ———————————— AVISO INICIAL ————————————
st.markdown("### AVISO IMPORTANTE")
st.markdown("**Todos los gases monoatómicos tienen el mismo valor de Cp y Cv.**")
st.markdown("**Cp = 20.8 kJ/kg·K** &nbsp;&nbsp;&nbsp;&nbsp; **Cv = 12.5 kJ/kg·K**")
st.markdown("---")

# ———————————— DATOS DE SUSTANCIAS ————————————
sustancias = {
    "Acetileno (C₂H₂)": {"a": 21.8, "b": 9.2143 * 10**-2, "c": -6.527 * 10**-5, "d": 18.21 * 10**-9, "M": 26.04},
    "Aire (mezcla)": {"a": 28.11, "b": 0.1967 * 10**-2, "c": 4.802 * 10**-5, "d": -1.966 * 10**-9, "M": 28.97},
    "Amoniaco (NH₃)": {"a": 27.568, "b": 2.5630 * 10**-2, "c": 0.99072 * 10**-5, "d": -6.699 * 10**-9, "M": 17.03},
    "Azufre (S₂)": {"a": 27.21, "b": 2.218 * 10**-2, "c": -1.628 * 10**-5, "d": 3.986 * 10**-9, "M": 64.13},
    "Benceno (C₆H₆)": {"a": -36.22, "b": 48.475 * 10**-2, "c": -31.57 * 10**-5, "d": 77.62 * 10**-9, "M": 78.11},
    "i-Butano": {"a": -7.913, "b": 41.60 * 10**-2, "c": -23.01 * 10**-5, "d": 49.91 * 10**-9, "M": 58.12},
    "n-Butano (C₄H₁₀)": {"a": 3.96, "b": 37.15 * 10**-2, "c": -18.34 * 10**-5, "d": 35.00 * 10**-9, "M": 58.12},
    "Cloruro de hidrógeno (HCl)": {"a": 30.33, "b": -0.7620 * 10**-2, "c": 1.327 * 10**-5, "d": -4.338 * 10**-9, "M": 36.46},
    "Dióxido de azufre (SO₂)": {"a": 25.78, "b": 5.795 * 10**-2, "c": -3.812 * 10**-5, "d": 8.612 * 10**-9, "M": 64.07},
    "Dióxido de carbono (CO₂)": {"a": 22.26, "b": 5.981 * 10**-2, "c": -3.501 * 10**-5, "d": 7.469 * 10**-9, "M": 44.01},
    "Dióxido de nitrógeno (NO₂)": {"a": 22.9, "b": 5.715 * 10**-2, "c": -3.52 * 10**-5, "d": 7.87 * 10**-9, "M": 46.01},
    "Etano (C₂H₆)": {"a": 6.900, "b": 17.27 * 10**-2, "c": -6.406 * 10**-5, "d": 7.285 * 10**-9, "M": 30.07},
    "Etanol (C₂H₆O)": {"a": 19.9, "b": 20.96 * 10**-2, "c": -10.38 * 10**-5, "d": 20.05 * 10**-9, "M": 46.07},
    "Etileno (C₂H₄)": {"a": 3.95, "b": 15.64 * 10**-2, "c": -8.344 * 10**-5, "d": 17.67 * 10**-9, "M": 28.05},
    "n-Hexano (C₆H₁₄)": {"a": 6.938, "b": 55.22 * 10**-2, "c": -28.65 * 10**-5, "d": 57.69 * 10**-9, "M": 86.18},
    "Hidrógeno (H₂)": {"a": 29.11, "b": -0.1916 * 10**-2, "c": 0.403 * 10**-5, "d": -0.804 * 10**-9, "M": 2.016},
    "Metano (CH₄)": {"a": 19.89, "b": 5.024 * 10**-2, "c": 1.269 * 10**-5, "d": -1.101 * 10**-9, "M": 16.04},
    "Metanol (CH₄O)": {"a": 21.1, "b": 9.152 * 10**-2, "c": -1.22 * 10**-5, "d": -8.039 * 10**-9, "M": 32.04},
    "Monóxido de carbono (CO)": {"a": 28.16, "b": 0.1675 * 10**-2, "c": 0.5372 * 10**-5, "d": -2.222 * 10**-9, "M": 28.01},
    "Nitrógeno (N₂)": {"a": 28.90, "b": -0.1571 * 10**-2, "c": 0.8081 * 10**-5, "d": -2.873 * 10**-9, "M": 28.02},
    "Óxido nítrico (NO)": {"a": 29.34, "b": -0.09395 * 10**-2, "c": 0.9747 * 10**-5, "d": -4.187 * 10**-9, "M": 30.01},
    "Óxido nitroso (N₂O)": {"a": 24.11, "b": 5.8632 * 10**-2, "c": -3.562 * 10**-5, "d": 10.58 * 10**-9, "M": 44.01},
    "Oxígeno (O₂)": {"a": 25.48, "b": 1.520 * 10**-2, "c": -0.7155 * 10**-5, "d": 1.312 * 10**-9, "M": 32.00},
    "n-Pentano (C₅H₁₂)": {"a": 6.774, "b": 45.43 * 10**-2, "c": -22.46 * 10**-5, "d": 42.29 * 10**-9, "M": 72.15},
    "Propano (C₃H₈)": {"a": -4.04, "b": 30.48 * 10**-2, "c": -15.72 * 10**-5, "d": 31.74 * 10**-9, "M": 44.10},
    "Propileno (C₃H₆)": {"a": 3.15, "b": 23.83 * 10**-2, "c": -12.18 * 10**-5, "d": 24.62 * 10**-9, "M": 42.08},
    "Trióxido de azufre (SO₃)": {"a": 16.40, "b": 14.58 * 10**-2, "c": -11.20 * 10**-5, "d": 32.42 * 10**-9, "M": 80.06},
    "Agua (vapor)": {"a": 32.24, "b": 0.1923 * 10**-2, "c": 1.055 * 10**-5, "d": -3.595 * 10**-9, "M": 18.02}
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

elif opcion == "2":
    st.markdown("### Fórmula: ∫ Cp dT  −  RΔT")
    st.markdown("Constante universal de los gases (R): 8.314 kJ/kmol·K")

    R_universal = 8.314
    R = R_universal / M
    st.markdown(f"R para esta sustancia: {R_universal} / {M} = {R:.4f} kJ/kg·K")

    T1_C = st.number_input("Ingresa la temperatura inicial (°C):", format="%.2f", key="T1")
    T2_C = st.number_input("Ingresa la temperatura final (°C):", format="%.2f", key="T2")

    if st.button("Calcular ΔU y ΔH"):
        # Conversión de temperaturas
        T1 = T1_C + 273.15
        T2 = T2_C + 273.15
        deltaT = T2 - T1

        st.markdown(f"Conversión: T₁ = {T1_C:.1f} °C = {T1:.2f} K   |   T₂ = {T2_C:.1f} °C = {T2:.2f} K")
        st.markdown(f"ΔT = {deltaT:.2f} K")

        # Cálculo de ΔH (sin R)
        deltaH_kJ_kmol = (
            a * deltaT +
            (b / 2) * (T2**2 - T1**2) +
            (c / 3) * (T2**3 - T1**3) +
            (d / 4) * (T2**4 - T1**4)
        )
        deltaH_kJ_kg = deltaH_kJ_kmol / M

        # Cálculo de ΔU = ΔH - RΔT
        deltaU_kJ_kmol = deltaH_kJ_kmol - R_universal * deltaT
        deltaU_kJ_kg = deltaU_kJ_kmol / M

        st.markdown("### Resultados:")
        st.markdown(f"Reemplazo ΔH: ΔH = {a}({deltaT}) + {b}/2({T2}² - {T1}²) + {c}/3({T2}³ - {T1}³) + {d}/4({T2}⁴ - {T1}⁴)")
        st.markdown(f"Resultado ΔH: ΔH = {deltaH_kJ_kmol:.4f} kJ/kmol → {deltaH_kJ_kg:.4f} kJ/kg")

        st.markdown(f"Reemplazo ΔU: ΔU = ΔH - RΔT = {deltaH_kJ_kmol:.4f} - {R:.4f}({deltaT:.2f})")
        st.markdown(f"Resultado ΔU: ΔU = {deltaU_kJ_kmol:.4f} kJ/kmol → {deltaU_kJ_kg:.4f} kJ/kg")

        interpretacion = "El sistema se calentó (ΔU positivo)" if deltaU_kJ_kg > 0 else "El sistema se enfrió (ΔU negativo)"
        st.markdown(f"Interpretación: {interpretacion}")
