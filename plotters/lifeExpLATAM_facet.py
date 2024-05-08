import seaborn.objects as so
from gapminder import gapminder


def plot():
    LATAM = ["Argentina","Brazil","Chile","Colombia","Peru","Uruguay"]
    gapminderLATAM = gapminder[gapminder.country.isin(LATAM)]
    figura = (
        so.Plot(gapminderLATAM, x = "year", y = "lifeExp")
        .facet("country", wrap = 3)
        .add(so.Line(alpha = 0.3), group = "country", col = None)
        .add(so.Line(linewidth = 3))
        .label(
                #title="Latinoamérica - Evolución de la expectativa de vida", <- AL ESTAR USANDO FACET APLICA EL TITULO A CADA SUBPLOT
                x="Año",
                y="Expectativa de vida"
            )
    )
    return dict(
        descripcion="Un gráfico que compara las evoluciones en expectativa de vida de algunos países de Latinoamérica",
        autor="Federico Brocca",
        figura=figura,
    )