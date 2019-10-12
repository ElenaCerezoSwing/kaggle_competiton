# KISS me, Data

Este proyecto es la resolución de una competición de Kaggle, en concreto la que aparece en el link de abajo:
https://www.kaggle.com/c/datamad0819-vehicles/data

En ella se nos pedía entrenar un modelo que predijera el precio de los coches correspondientes al dataset cars_train.csv.

## ¿Con qué datos contamos?
469992 registros con las siguientes columnas

Columnas:
* `Id`
* `city`
* `year`
* `manufacturer`
* `make`
* `condition`
* `cylinders`
* `fuel`
* `odometer`
* `title_status`
* `transmission`
* `drive`
* `size`
* `type`
* `paint_color`
* `lat`
* `long`
* `county_fips`
* `county_name`
* `state_fips`
* `state_code`
* `state_name`
* `weather`
* `price`

En principio se decidió contar con todos los datos posibles... Diógenes acapara al principio.
A continuación, se eliminaron una serie de columnas: `city`, `county_name`, `county_fips`, `make`, `manufacturer`, `paint_color`, `state_code`, `state_name`, `drive`, `title_status`
Porque tras intentar hacer varias transformaciones en los campos de tipo object no mejoraba el modelo.

Se genera un [ETL](https://github.com/ElenaCerezoSwing/kaggle_competiton/tree/master/src) para poder obtener los csv que necesitamos entregar. 

Sin embargo, a pesar de hacer varios modelos (no están puestos todos los que se generaron) no se mejoraba la predicción.
[Aquí podéis encontrar la lista de modelos disponibles en sklearn](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.linear_model)

### ¿Cuál fue la clave para mejorar la predicción?
[Principio KISS](https://es.wikipedia.org/wiki/Discusi%C3%B3n:Principio_KISS) 
Es un principio basado en el acrónimo *Keep it simple, Stupid!* (aunque a mí me gusta más la acepción de *Keep it simple, Sweetheart* o *Keep it simple and smile*)
Esto es:
#### Hazlo sencillo :)

1.- Se eliminaron más datos del dataset porque había gran cantidad de nulos y la transformación no mejoraba:
`Id`,`county_fips`, `county_name`, `state_fips`, `state_code`,`title_status`, `state_name`, `city`, `manufacturer`, `make`, `paint_color`, `drive`, `condition`

2.- Se dummificó menos.

3.- Se rellenaron los `NaN` con 0 porque era el valor que más aparecía sin tener que hacer grandes cálculos.

4.- Se estandarizaron y escalaron las columnas, gracias a [Jesús Rodríguez Álvarez](https://github.com/4thSword) que fue quien me lo explicó y se pudo integrar en el modelo.
Se predijo con el entrenamiento, pero no con la transformación.

5.- Se utilizó un modelo de regresión de RandomForest, ¿por qué? Porque, atendiendo a [Javier Luna Molina](https://github.com/JavierLuna), es un modelo que funciona muy bien.

6.- Se aplicaron los parámetros `max_depth=5`, `n_estimators=100`. [Alberto García Cobo](https://github.com/albertogcmr) nos aconsejó que, además de elegir bien el modelo, hay que setear parámetros adecuados, no incluír los que nos vienen por defecto siempre, aunque funcionen correctamente.


Y todo esto no hubiera sido posible sin la inestimable ayuda de mis compañeros y amigos: [Marina Pérez Muñoz](https://github.com/marinapm90) Y [Fernando Villanueva](https://github.com/fervillarce) que me explicaron cómo arrancar.
Y por supuesto, al resto de mis compañeras y compañeros de IronHack que siempre me están apoyando.

# Gracias :blush:

* Pd: Como conclusión se puede sacar que el precio de los coches es muy alto... independientemente del año, por lo tanto... usemos :bike::bike: :bike: es mejor para nuestra salud y la del planeta.



