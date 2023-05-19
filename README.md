# ds_ml_proyecto_final

# Clasificacion Automatica de Tickets con NLP

Ruth Daniela Villalobos (ruthdanivillalobos@gmail.com)

**TABLA DE CONTENIDO**
1. Introducción 
  - Objetivos de proyecto
2. Configuración e instalación
3. Cargado de Dataset
  - Text mining
4. Limpieza de los textos mediante transformaciones y lematización
  - Eliminación de caracteres innecesarios
  - Lematización
  - Definición de dataframe con información necesaria
5. Análisis exploratorio de datos
  - Visualización del largo de los textos
  - Visualización de las 50 palabras más frecuentes.
  - N-gramas
  - Top 10 de unigramas
  - Top 10 de bigramas
  - Top 10 de trigramas
6. Extracción de características
7. Modelado
  - Regresión logística
  - Árboles de decisión
  - Random forest
  - Naive Bayes
8. Conclusiones

#Introduction
En los últimos años, el Procesamiento del Lenguaje Natural (NLP) se ha convertido en un campo de alta demanda y de rápido avance en el ámbito de la informática y la inteligencia artificial.

#Methods Used
 Se obtuvieron 20.950 artículos de prensa con temática económica de los sitios web de https://www.la-razon.com/, https://www.paginasiete.bo/ y el https://eldeber.com.bo/  logrando abarcar los principales periódicos de la prensa boliviana para que posteriormente se realizara la clasificion de acuerdo a topicos de interes para un analisis economico con los siguientes algoritmos:

*Logistic regression
*Decision Tree
*Random Forest
*Naive Bayes

##Instalacion de Librerias
!pip install locales
!pip install spacy
!python -m spacy download en_core_web_sm
!pip install textblob
!pip install es-core-news-sm
!pip install selenium

##Importación de Librerias
json
numpy
pandas
re
nltk
spacy
seaborn
matplotlib
plotly
requests
locale
es_core_news_sm
time

#Download and Setup
Prerequisitos
Para lograr ver los resultados de este proyecto, se recomienda el uso de un Jupyter Notebook, en este caso se hizo uso de Google Colab Notebooks, los cuales vienen enlazados con una cuenta de gmail y no es necesario otro requisito para su uso.
Para el uso de selenium se debe cargar el driver del navegador que se utilizara en este proyecto se trabajo con Crome por lo que se adjunta en el proyecto.
Sin embargo, puede lograrse un normal funcionamiento con una instalación de Python y el uso de cualquier herramienta de edición (en algunos casos puede requerir la instalación de algunas librerias extra).

#How to Run
Se puede hacer uso de este proyecto con el siguiente procedimiento:

Clonar el repositorio desde GitHub
Copiar en url del repo y en una terminal de su preferencia seguir estos pasos:
Ubicar una carpeta para almacenar el proyecto
Escribir en la terminal: git clone
Abrir el archivo .ipynb y verificar que la base de datos este bien ruteada.
Empezar a correr los pasos propuestos.
Copiar el contenido en un Google Colab Notebook, verificando que la base de datos tambien se encuentren ahi.


#Most Significant Variables are:

Logistic Regression

score:0.8806796487208859

							precision    recall  f1-score   support

                Inversión       0.90      0.72      0.80       213
            Hidrocarburos       0.94      0.91      0.92       338
       Política Monetaria       0.84      0.91      0.88       386
               Producción       0.96      0.82      0.89       180
    Crecimiento Económico       0.81      0.86      0.83       251
                Impuestos       0.88      0.98      0.93       393
        Comercio exterior       0.89      0.90      0.90       237
    Servicios Financieros       0.94      0.85      0.89       222
              Contrabando       0.93      0.86      0.90       229
Servicios de Comunicación       0.84      0.93      0.88       207
                   Empleo       0.95      0.80      0.87       133
 Transporte de mercadería       0.83      0.83      0.83       300
                  Minería       0.99      0.82      0.89       195
        Política salarial       0.89      0.84      0.86       359
        Energía eléctrica       0.75      0.90      0.82       365
            Materia prima       0.92      0.93      0.92       297
               Jubilación       0.90      0.96      0.93       285
                Inflación       0.95      0.93      0.94       223
        Indutria Nacional       0.84      0.87      0.85       279
         Transporte aéreo       0.97      0.77      0.86       146

                 accuracy                           0.88      5238
                macro avg       0.90      0.87      0.88      5238
             weighted avg       0.89      0.88      0.88      5238
			 
Árboles de decisión
			 
score:0.618358256442889
							precision    recall  f1-score   support

                Inversión       0.58      0.56      0.57       290
            Hidrocarburos       0.67      0.65      0.66       367
       Política Monetaria       0.58      0.61      0.59       451
               Producción       0.75      0.76      0.75       192
    Crecimiento Económico       0.51      0.46      0.49       285
                Impuestos       0.76      0.77      0.77       519
        Comercio exterior       0.60      0.61      0.60       260
    Servicios Financieros       0.58      0.59      0.58       287
              Contrabando       0.56      0.55      0.56       296
Servicios de Comunicación       0.61      0.55      0.58       268
                   Empleo       0.74      0.67      0.71       164
 Transporte de mercadería       0.45      0.46      0.45       373
                  Minería       0.70      0.72      0.71       233
        Política salarial       0.60      0.65      0.62       437
        Energía eléctrica       0.52      0.50      0.51       460
            Materia prima       0.67      0.66      0.66       336
               Jubilación       0.73      0.77      0.75       313
                Inflación       0.79      0.78      0.79       268
        Indutria Nacional       0.47      0.51      0.49       312
         Transporte aéreo       0.66      0.62      0.64       175

                 accuracy                           0.62      6286
                macro avg       0.63      0.62      0.62      6286
             weighted avg       0.62      0.62      0.62      6286
			 
Random Forest

score:0.7914412981228126

							precision    recall  f1-score   support

                Inversión       0.87      0.45      0.59       290
            Hidrocarburos       0.82      0.90      0.86       367
       Política Monetaria       0.73      0.88      0.80       451
               Producción       0.82      0.85      0.83       192
    Crecimiento Económico       0.81      0.70      0.75       285
                Impuestos       0.70      0.98      0.82       519
        Comercio exterior       0.74      0.90      0.82       260
    Servicios Financieros       0.91      0.69      0.78       287
              Contrabando       0.94      0.79      0.86       296
Servicios de Comunicación       0.74      0.88      0.80       268
                   Empleo       0.85      0.75      0.80       164
 Transporte de mercadería       0.75      0.58      0.65       373
                  Minería       0.89      0.88      0.88       233
        Política salarial       0.80      0.61      0.69       437
        Energía eléctrica       0.73      0.76      0.74       460
            Materia prima       0.79      0.84      0.82       336
               Jubilación       0.77      0.98      0.86       313
                Inflación       0.88      0.94      0.91       268
        Indutria Nacional       0.82      0.73      0.77       312
         Transporte aéreo       0.91      0.65      0.76       175

                 accuracy                           0.79      6286
                macro avg       0.81      0.79      0.79      6286
             weighted avg       0.80      0.79      0.79      6286
			 
Naive Bayes

score:0.606108813235762

Los grupos identificados mediante la aplicación de los algoritmos citados en los puntos anteriores engloban todos los temas pertinentes para un correcto análisis económico desde una perspectiva sectorial. Cabe destacar que predominan los grupos relacionados con el sector real de la economía nacional, es decir, los temas de producción y recursos naturales principalmente.
En el presente documento se pone énfasis en la métrica de precisión por ser la más indicada en los problemas de clasificación. 
El cual seria regresion logistica con rendimineto del 0.8806796487208859
