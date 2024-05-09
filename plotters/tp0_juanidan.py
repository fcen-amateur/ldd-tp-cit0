import seaborn.objects as so
from gapminder import gapminder


def plot():
    paises = gapminder[gapminder["country"].isin(["Argentina", "Chile", "Bolivia",'Peru','Colombia','Venezuela'])]
    figura = (
        so.Plot(
            data=paises,
            x="year",
            y="lifeExp",
            color="country",
            linestyle='country'
        )
        .layout(size=(8,6))
        .add(so.Line(linewidth=3))
        .label(
            title="Expectativa de vida en países por donde pasa la Cordillera de los Andes",
            x="Año",
            y="Expectativa de vida",
            color="País",
        )
    )
    return dict(
        descripcion="Expectativa de vida en países por donde pasa la Cordillera de los Andes a través de los años",
        autor="Juan Ignacio DAngona",
        figura=figura,
    )
