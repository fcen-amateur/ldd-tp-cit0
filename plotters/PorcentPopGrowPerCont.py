import pandas as pd
import seaborn as sns
import seaborn.objects as so
from gapminder import gapminder

#Funciones auxiliares 
gm_preparado_sumado = gapminder.groupby(["continent","year"])["pop"].sum()
aux = pd.Series(gm_preparado_sumado).reset_index()
aux.columns = ['continent', 'year', 'population']
africaPct = (aux["population"].iloc[0:12])/(aux["population"].iloc[0])
americasPct = (aux["population"].iloc[12:24])/(aux["population"].iloc[12])
asiaPct = (aux["population"].iloc[24:36])/(aux["population"].iloc[24])
europePct = (aux["population"].iloc[36:48])/(aux["population"].iloc[36])
oceaniaPct = (aux["population"].iloc[48:60])/(aux["population"].iloc[48])
columnaDePctPop = (pd.concat([africaPct, americasPct , asiaPct , europePct , oceaniaPct], ignore_index=True)*100)-100
aux.insert(3, "Pop%", columnaDePctPop)
#Fin de funciones auxiliares

def plot():
    figura = (
        so.Plot(
            data= aux ,
            x="year",
            y="Pop%",
            color="continent",
        )
        .add(so.Line())
        .label(
            title="Aumento porcentual de la poblacion",
            x="Año",
            y="Poblacion%",
            color="Continente",
        )
    )
    return dict(
        descripcion="Grafico que muestra una comparativa el porcentaje de lo que incremento la poblacion de cada continente a lo largos de los años",
        autor="Alsina Juan Manuel",
        figura=figura,
    )
