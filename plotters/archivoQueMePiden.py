import seaborn.objects as so
from gapminder import gapminder

def plot():
    figura = (
        so.Plot(
            gapminder[gapminder["pop"]<1000000],
            x="lifeExp",
            y="gdpPercap",
        )
        .add(so.Line(color='red', linewidth=3), so.PolyFit(1))
	.add(so.Dot()).scale(y="log")
        .label(
            title="Expectativa de vida respecto a los ingresos en paises pequeños",
            x="Expectativa de Vida",
            y="Ingresos Per Capita",
        )
              )
    return dict(
        descripcion="Expectativa de vida respecto a los ingresos en paises pequeños durante los años",
        autor="Bruno Festa",
        figura=figura,
    )
