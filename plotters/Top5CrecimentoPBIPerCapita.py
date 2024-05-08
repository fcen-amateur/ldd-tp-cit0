import seaborn.objects as so
from gapminder import gapminder

def plot():
    MayorCrecimiento = gapminder[gapminder['country'].isin(['Singapore',
                                                        'Taiwan',
                                                        'Korea, Rep.',
                                                        'Botswana',
                                                        'Equatorial Guinea'])]
    MayorCrecimiento = MayorCrecimiento.sort_values(by = 'gdpPercap', ascending=False)
    MayorCrecimiento = MayorCrecimiento.rename(columns= {'country' : 'Top 5 Paises'})
    figura = (
    so.Plot(MayorCrecimiento, x = 'year', y = 'gdpPercap')
    .add(so.Line(), color = 'Top 5 Paises')
    .add(so.Line(color='gray', linestyle=(4, 3)), so.Agg(), data=gapminder, x = 'year', y = 'gdpPercap')
    .label(title='Top 5 paises con el mayor creciento periodo 1952-2007', y = 'PBI per Capita', x = 'Year')
    .show()
    )
    return dict(
        descripcion="""Comparacion entre los 5 paises con el mayor crecimiento en el periodo 1952-2007.
        Estos paises fueron seleccionados segun el indice:  PBIPerCap2007 / PBIPerCap1952.
        En gris, y linea punteada, se puede apreciar el promedio mundial anual de PBI per capita.
        """,
        autor="Bautista Gilardon",
        figura=figura,
    )