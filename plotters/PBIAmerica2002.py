import seaborn.objects as so
from gapminder import gapminder
import matplotlib.pyplot as plt

def plot():
    datos_year=gapminder[gapminder['year']==2002]
    datos_year_continent=datos_year[datos_year['continent']=="Americas"]
    
    fig, ax = plt.subplots()
    ax.xaxis.set_tick_params(rotation=90)

    
    figura = (so.Plot(data=datos_year_continent, x='country', y='gdpPercap')
    .add(so.Bar())
    .label(
        title="PBI de todos los países de América en el año 2002",
        x="Países de América",
        y="PBI")
    .on(ax)
    )

    return dict(
        descripcion="Un sofisticado gráfico con el PBI de cada paíse de América durante el año 2001",
        autor="Antonella Rivano",
        figura=figura,
    )
