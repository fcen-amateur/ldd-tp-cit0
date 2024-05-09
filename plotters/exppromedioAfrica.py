import seaborn.objects as so
from gapminder import gapminder
import numpy as np

def plot():
    datosx = gapminder[gapminder['continent']=='Africa']['year'].drop_duplicates().values
    # Datosx es un array con los años que se toman en cuenta en el eje x para el gráfico, más precisamente todos los años de los cuales se tomo "censo" de los países.
    datosybeta = []
    for year in datosx:
        lifeExpAvg = np.mean(gapminder [gapminder['continent']=='Africa'][gapminder['year']==year]['lifeExp'])
        datosybeta.append(lifeExpAvg)
    datosy = np.array(datosybeta)
    #datosy es un array con la expectativa de vida promedio africana por cada año en el array de datosx.
    figura = (
        so.Plot(x = datosx, y = datosy)
        .add(so.Line())
        .label(
            title="Expectativa de vida promedio de paises africanos a lo largo del tiempo",
            x="Año",
            y="Promedio de expectativa de vida en ese año",
        )
    )
    #figura.show()
    #Si descomentas la linea anterior en un IDE adecuado, la figura se muestra cuando corres la función.
    return dict(
        descripcion="Un gráfico que representa la expectativa de vida promedio de los paises africanos en funcion del tiempo.",
        autor="Gonzalo Nicolas Moreira Valdez",
        figura=figura,
    )

# Hice este gráfico porque me parecía interesante ver como cambió la expectativa de vida de los países africanos teniendo en cuenta que muchos de ellos venían de ser
# colonias de países europeos y atravesaron tragedias historicas en tiempos no extremadamente lejanos al comienzo de los censos que utilizó el gapminder como
# información para este dataframe.
