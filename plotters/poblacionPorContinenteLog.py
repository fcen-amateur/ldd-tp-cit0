import seaborn.objects as so
from gapminder import gapminder
import pandas as pd

PopContinent=gapminder.groupby(["continent","year"])["pop"].sum()
PopContinentDF=pd.DataFrame(PopContinent)

def plot():
    figura = (
        so.Plot(data=PopContinentDF, x="year", y="pop", color="continent")
        .add(so.Line())
        .label(title="Evolución de la población por continente", x="Año", y="Población (escala logarítmica)")
        .scale(y="log")
    )
    return dict(
        descripcion="Se compara la variación de poblacion entre los continentes. Como la diferencia de población total entre Asia (mayor poblacion) y Oceania (menor poblacion) no se aprecia correctamente en escala lineal, se muestra en una escala logarítmica.",
        autor="Juan Pablo Gervasi",
        figura=figura,
    )
