import seaborn.objects as so
from gapminder import gapminder

def plot():
    figura = (
        so.Plot(
            gapminder[gapminder.continent == "Americas"],
            x="year",
            y="pop",
            color="country",
        )
        .add(so.Line())
        .label(
            title="Población en America",
            x="Año",
            y="Población",
            color="País",
        )
    )
    return dict(
        descripcion="Cantidad de habitantes en los países de América a lo largo del tiempo",
        autor="Sofia Mezzadra",
        figura=figura,
    )
