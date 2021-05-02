# sr_taller_2
Taller 2 sistemas de recomendación

## preprocesamiento
Esta carpeta contiene los archicos para carga de información
active_user.csv
- Descripcion reseñas.ipynb: contiene el análisis descripttivo de las reseñas de los negocios
- Descripcion_negocios.ipynb: contiene el análisis descriptivo de la base original de la base de los negocios
- load_active_users.py: carga los usuarios activos a base de datos para su inicio de sesión, un usuario activo es aquel que en la base de reseñas haya hecho al menos 5 reseñas.
- load_all_users.py: carga toda la base de usuarios de ser necesario
- load_business.py: carga toda la base de negecios a base de datos, pero únicamente aquellos negocios que se encuentran abiertos, es decir con is_open=true
- preprocesamiento.ipynb: contiene el preprocesamiento de las bases, es decir genera los archivos para que luego el modelo corra.

## modelo
Esta carpeta contiene los modelo y las bases preprocesadas para que este corra.
Cabe resaltar que la última sección del python que hace el insert de todas las recomendeciones toma casi unas 5 horas en correr.
- modelo.ipynb: contiene el modelo con el cual se calcularon las recomendaciones, e inserta a base de datos.
- yelp_reviews_restaurantes.csv: contiene la información de reseña-negocio de los restaurantes en la ciudad de Bristol
- yelp_reviews_restaurantes_top20ciudadycategoria.csv: contiene la información de las reseñas-negocio del top 20 de categorias y del top 20 de ciudades según el análisis descriptivo realizado previamente.

## sql
Contiene la información de la creación de la base de datos y las tablas requeridas para el funcionamiento del modelo.
- contiene los procedimientos almacenados para las queries que realiza el front

## run node
- La pagina web no maneja excepciones por lo tanto si se presenta una excepción de sql el servicio se cae y toca volverlo a subir. Para subir el servicio se ingresa al servidor y se corre el siguiente comando forever start bin/www.
- Correr en desarrollo: npm run dev