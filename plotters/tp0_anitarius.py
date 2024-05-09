import seaborn as sns
import pandas as pd
from gapminder import gapminder


def plot():
   df = pd.DataFrame(gapminder)
   paises = ['Argentina','Brazil','Bolivia','Chile','Colombia','Paraguay','Peru','Uruguay','Venezuela']
   df = df[df['country'].isin(paises)]

   sns.set_theme(style="dark")

   g = sns.relplot(
        data=df,
        x="year", y="lifeExp", col="country", hue="country",
        kind="line", palette="crest", linewidth=4, zorder=5,
        col_wrap=3, height=3, aspect=1.5, legend=False,
        )
   for year, ax in g.axes_dict.items():
        ax.text(.4, 1, year, transform=ax.transAxes, fontweight="bold")

        sns.lineplot(
            data=df, x="year", y="lifeExp", units="country",
           estimator=None, color=".8", linewidth=1, ax=ax,
       )

   g.set_titles("")
   g.set_axis_labels("", "LifeExp")
   g.tight_layout()
   return dict(
        descripcion="Evolucion de la espectativa de vida en paises de Sur America",
        autor="Ana Rius",
        figura=g,
    )

