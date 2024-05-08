import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(
            gapminder[gapminder["country"].isin(["Argentina", "Brazil", "Uruguay", "Bolivia", "Ecuador", "Paraguay", "Colombia", "Venezuela", "Peru", "Chile"])],
            x="year",
            y="gdpPercap",
        )
        .add(so.Line(), color = "country")
        .label(
            title="PBI per cápita en Sudamérica",
            x="Año",
            y="PBI per cápita",
            color="País",
        )
    )
    return dict(
        descripcion="El Producto Bruto Interno per cápita de cada país de Sudamérica a lo largo de los años",
        autor="Tomas",
        figura=figura,
    )