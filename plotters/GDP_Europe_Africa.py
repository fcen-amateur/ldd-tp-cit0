import seaborn.objects as so
from gapminder import gapminder

def plot():

  gapminder_EU_AFR = gapminder[gapminder["continent"].isin(["Europe", "Africa"])]
  
  figura = (
    so.Plot(data=gapminder_EU_AFR, x="year")
    .add(so.Line(marker="o"), so.Agg("mean"), y="gdpPercap", color="continent")
    .add(so.Line(color="grey", marker="o"), so.Agg("mean"), y=gapminder["gdpPercap"], label="World")
    .label(title="PBI (nominal) per cápita anual promedio de Europa y África", x="Año", y="PBI per cápita", color="Continente")
)
  
  return dict(
    descripcion="PBI (nominal) per cápita anual promedio de Europa y África, comprendido entre años 1952 y 2007. Comparación con promedio global."
    autor="Jean Casaubon"
    figura=figura
  )
