import seaborn.objects as so
from gapminder import gapminder

paises = ["United States", "United Kingdom", "Germany", "China", "Argentina"]

def plot():
    figura = (
        so.Plot(
            gapminder[gapminder["country"].isin(paises)],
            x="year",
            y="gdpPercap",
            color="country",
        )
        .add(so.Line(linewidth = 2))
        .label(
            title="PIB de los siguientes paises a lo largo del tiempo",
            x="Año",
            y="gdpPercap",
            color="País",
        )
    )
    return dict(
        descripcion="En el grafico vemos los diferentes valores de PIB que tienen estos 5 paises a lo largo de los años, desde 1950 hasta la actualidad",
        autor="Francisco Borda Rojas",
        figura=figura,
    )
