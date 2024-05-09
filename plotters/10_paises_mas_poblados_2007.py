import seaborn.objects as so
from gapminder import gapminder


def plot():
    datosPoblados = gapminder[gapminder["pop"] > 100000000]
    datosPoblados2007 = datosPoblados[datosPoblados["year"] == 2007]
    
    figura = (
        so.Plot(
            datosPoblados2007,
            x="country",
            y="pop",
            color="country",
        )
        .add(so.Bars())
        .label(
            title="Los 10 países con más habitantes en el 2007",
            x="Países",
            y="Población",
            
        )
    )
    return dict(
        descripcion="Gráfico de barras que representa la población de los 10 países con más habitantes del mundo en el año 2007. En esta escala el 1.0 representa mil millones de habitantes.",
        autor="Paula Alvez",
        figura=figura,
    )

