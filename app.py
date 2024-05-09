"""
# TPcit0: una galería de _gapminder_
"""

import streamlit as st
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import seaborn.objects as so
import importlib
import plotters
from pkgutil import iter_modules


def submodulos(modulo):
    return [submodule.name for submodule in iter_modules(modulo.__path__)]

# Para reducir el margen superior antes del título
# https://discuss.streamlit.io/t/how-do-i-reduce-or-eliminate-the-top-margin-of-my-mobile-screen/51530/2
st.markdown(
    " <style> div[class^='block-container'] { padding-top: 1rem; } </style> ",
    unsafe_allow_html=True,
)
st.write("# TPcit0: una galería de _gapminder_")

st.sidebar.write("### Un gráfico para cada gusto\n")
opcion = st.sidebar.radio("Mostrar...", sorted(submodulos(plotters)), index=None) or "JaponVsNigeria"

data = importlib.import_module(f"plotters.{opcion}").plot()

if isinstance(data, (so.Plot, Figure)) or hasattr(data, "figure"):
    data = dict(autor="N/A", descripcion="Descripción no disponible", figura=data)

figura = data["figura"]
fig = plt.figure()
if isinstance(figura, so.Plot):
    figura.on(fig).show()
elif isinstance(figura, Figure):
    fig = figura
else:
    try:
        fig = figura.figure
    except AttributeError:
        fig.text(0.5, 0.5, "Figura no disponible", fontsize=20, ha="center")

st.pyplot(fig)
st.write(data["descripcion"])
st.write("Autor(es):", data["autor"])
