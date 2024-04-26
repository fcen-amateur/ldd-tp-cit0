import seaborn.objects as so
import pandas as pd
from gapminder import gapminder

df = gapminder
dfArgentina = pd.DataFrame(df[df["country"] == "Argentina"])
dfArgentina['referencia'] = "Argentina"
dfAsia = pd.DataFrame(df[df["continent"] == "Asia"])
dfAsia['referencia'] = "Asia"
dfEuropa = pd.DataFrame(df[df["continent"] == "Europe"])
dfEuropa['referencia'] = "Europe"
dfOceania = pd.DataFrame(df[df["continent"] == "Oceania" ])
dfOceania['referencia'] = "Oceania"
dfAfrica = pd.DataFrame(df[df["continent"] == "Africa" ])
dfAfrica['referencia'] = "Africa"
dfAmericaSinArgentina = df[(df["continent"] == "Americas") & (df["country"] != "Argentina")]
dfAmericaSinArgentina['referencia'] = "America Sin Argentina"

def plot():
    figura = (
        (
        so.Plot(
            data = df,
            x="year",
            y="lifeExp",
        )
        .add(so.Line(), color = "referencia",  data = dfArgentina,  y="lifeExp")
        .add(so.Line(), so.Agg("mean"),  color = "referencia", data = dfAmericaSinArgentina, y="lifeExp" )
        .add(so.Line(), so.Agg("mean"), color = "referencia", data = dfAsia, y="lifeExp" )
        .add(so.Line(), so.Agg("mean"), color = "referencia", data = dfAfrica, y="lifeExp" )
        .add(so.Line(), so.Agg("mean"), color = "referencia", data = dfEuropa, y="lifeExp" )
        .add(so.Line(), so.Agg("mean"),  color = "referencia", data = dfOceania, y="lifeExp" )
        .add(so.Line(), so.Agg("mean"),  color = "referencia", data = dfEuropa, y="lifeExp" )

        .label(
            title="Expectativa de vida en Argentina comparado al promedio de los demas continentes",
            x="Año",
            y="Expectativa de vida",
            color="Referencia",
        )
        )
    )
    return dict(
        descripcion="Expectativa de vida en Argentina comparado al promedio de los demas continentes a lo largo del tiempo",
        autor="Lautaro Saver",
        figura=figura,
    )
