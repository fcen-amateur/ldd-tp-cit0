import seaborn.objects as so
from gapminder import gapminder

def plot():
    figura = (
        so.Plot(
            data = gapminder[gapminder["country"].isin(["Argentina", "Chile"])],
            x="year",
            y="lifeExp",
            color="country",
        )
        .add(so.Line())
        .label(
            title="Expectativa de vida de Argentina y Chile",
            x="Año",
            y="Expectativa de vida",
            color="País",
        )
    )
    return dict(
        descripcion="Expectativa de vida de Chile contra Argentina a lo largo del tiempo",
        autor="Román Parisi",
        figura=figura,)
        


