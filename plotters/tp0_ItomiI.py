import seaborn.objects as so
from gapminder import gapminder


def plot():
    aa = gapminder.groupby(['year', 'continent'])['lifeExp'].mean()
    aaa = aa.reset_index()
    figura = (
        so.Plot(aaa, x="year", y = "lifeExp",color="continent")
        .add(so.Line())
        .label(
            title="expectiva promedio de vida por continente",
            x="años",
            y="expectativa de vida promedio",
        )
    )
    return dict(
        descripcion="expectativa de vida promedio por continente a lo largo de los años",
        autor="tomas mele",
        figura=figura,
    )
