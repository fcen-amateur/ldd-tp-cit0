import seaborn.objects as so
from gapminder import gapminder


def plot():
    summary_by_continent_year = gapminder.groupby(['continent', 'year']).agg({'pop': 'sum', 'lifeExp': 'mean'}).reset_index()

    p =(
        so . Plot (
        summary_by_continent_year, x = "year" , y = "lifeExp" ,
        pointsize = "pop" , color = "continent"
        )
        .add(so.Line(), legend=False)
        . add ( so . Dot () )
        )
    p.label(x="Año", y="Expectativa de vida en años", color="Continente",title="Expectativa de vida promedio por continente y año", pointsize ="Población")

    return dict(
        descripcion="Expectativa de vida por continente a lo largo del tiempo",
        autor="Fernanda Villalba",
        figura=p,
    )
