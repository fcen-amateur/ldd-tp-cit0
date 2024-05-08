import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        (
            so.Plot( gapminder[gapminder.country == "Uganda"], x= "year", y = "gdpPercap")
            .add(so.Line(edgewidth = 7, linewidth = 4))
            .label(
                title="GDP per Capita en Uganda",
                x="Año",
                y="GPD per Cap",
                )
            .add(so.Line(color='red', linestyle='-', linewidth=2), so.PolyFit(1), label='Regresion lineal')
            .add(so.Line(color='green', linestyle='-', linewidth=2), so.PolyFit(5), label='Regresion quinta')
        )
    )
    return dict(
        descripcion="Expectativa de vida en Uganda a lo largo del tiempo y Estimaciones por cuadrados minimos",
        autor="Matias Gangui",
        figura=figura,
    )
