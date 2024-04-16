import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(
            gapminder[gapminder.continent == "Oceania"],
            x="year",
            y="lifeExp",
            color="country",
        )
        .add(so.Line())
        .label(
            title="Expectativa de vida en Oceanía",
            x="Año",
            y="Expectativa de vida",
            color="País",
        )
    )
    return dict(
        descripcion="Expectativa de vida en países de Oceanía a lo largo del tiempo",
        autor="La cátedra",
        figura=figura,
    )
def plot():
    figura = (
        so.Plot(gapminder[["continent", "country"]].drop_duplicates(), x="continent")
        .add(so.Bar(), so.Hist())
        .label(
            title="Cantidad de países por continente",
            x="Continente",
            y="Cantidad de países",
        )
    )
    return dict(
        descripcion="Un sofisticado gráfico con el número de países en cada continente",
        autor="La cátedra",
        figura=figura,
    )
