[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ztnPvLsL)
# TPcit0 - Una galería gráfica colaborativa con Gapminder
Trabajo Práctico: Consigna Integradora Temática Nro. 0, AKA "tepecito"

Un acercamiento amigable al TP #1

## Intro

[Streamlit](https://streamlit.io/) es un _framework_ de Python para crear aplicaciones web de manera rápida y sencilla (para quienes lo conocen, piensen en Shiny, de R). En este TP0, crearemos colaborativamente una galería de visualizaciones del dataset de Gapminder. Pueden ver cómo va quedando aquí:

### [**TPcit0: una galería de _gapminder_**](https://tpcit0.streamlit.app/)

## Consigna

A partir del dataset `gapminder` en el paquete homónimo, y usando la interfaz `objects` del paquete `seaborn`, **la tarea central de este TP es generar una visualización que resalte algún aspecto de interés en `gapminder`**. Asegúrese de seguir buenas prácticas: dé nombre a los ejes y título al gráfico, no codifique información innecesaria en canales superfluos, et cetera. Acompañe el gráfico de un sucinto párrafo descriptivo para el mismo.

**Este gráfico y el párrafo auxiliar pueden ser hechos con su herramienta predilecta**: en un notebook de Jupyter local, en Google Colab, usan la terminal o un editor de código (VS Code, Pycharm, Spyder, et cetera), su imaginación es el límite. Ahora bien, para incorporar su aporte a la [app]((https://tpcit0.streamlit.app/)) ya mencionada, **deberá registrar su trabajo bajo control de versiones**. Hete aquí una secuencia posible de acciones para conseguirlo:

1. _Forkee_ este repositorio a su cuenta personal de GitHub.
2. Comience una rama con el mismo nombre que su usuario de dicha plataforma.
3. En la carpeta `plotters`, cree un nuevo archivo de Python.
4. Copie los contenidos de la plantilla `paisesPorContinente.py` o `lifeExpOceania.py` al archivo recién creado. 
   Este archivo deberá contener una única función sin argumentos, de nombre `plot`, y que devuelva un diccionario (`dict`) con exactamente tres claves y sus respectivos valores:
  - "figura", cuyo valor sea un objeto `seaborn.objects.Plot` con el gráfico realizado,
  - "autor", cuyo valor sea una _cadena_ (`str`, "string") de caracters con el nombre del autor de la `figura` y
  - "descripcion" (sin tilde), cuyo valor sea un breve párrafo describiendo los aspectos relevantes del gráfico presentado.
6. Vaya _commiteando_ los cambios que realiza a su rama, hasta estar satisfecho/a con el resultado.
7. Publique la rama a su _fork_ remoto del repositorio actual, y cree un Pull Request (PR) contra el repositorio original. En la descripción del PR, mencione a alguno de los miembros de la cátedra (`slap, nz-angel, capitantoto`) para llamar su atención. Esté atento a los comentarios de revisión en su PR hasta que sea incorporado a la rama `main`.
8. _Mergeado_ su PR, vaya de nuevo a la app a ver el resultado. ¡Felicitaciones! Es Ud. un científico/a de datos publicado (en la web).


## OPCIONAL: Desarrollo local

Aunque el desarrollo del TP se puede realizar en cualquier plataforma, recomendamos ampliamente que intenten desarrollar _localmente, desde el repositorio_, para que vean cómo se va construyendo la app en vivo.

### Creación del entorno virtual de desarrollo
En la consola, desde la raíz del repo (cf.: comando `cd` para `c`ambiar de `d`irectorio, y `pwd` para ver el _present working directory_):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Con esto, quedará creado un entorno virtual con las librerías necesarias
- para crear la visualizacion (`seaborn, pandas, gapminder`),
- para correr la aplicación (`streamlit, watchdog`) y
- (opcionalmente) para usar el entorno virtual creado (`.venv`) como _kernel_ de Jupyter

### Levantar la aplicación localmente

_Con el entorno activado_, lo único que hay que hacer es usar `streamlit run app.py` y navegar a `http://localhost:8501/`

```bash
source .venv/bin/activate
streamlit run app.py
```

Si no lo hace solo, abrir el navegador e ir a http://localhost:8501/

Cada vez que guarde los archivos, los cambios se verán reflejados en la _app_ automágicamente. Basta con refrescar el sitio (Ctrl+R, F5) para ver los cambios más recientes.