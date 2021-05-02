Esta carpeta contiene los archicos para carga de información
active_user.csv
- Descripcion reseñas.ipynb: contiene el análisis descripttivo de las reseñas de los negocios
- Descripcion_negocios.ipynb: contiene el análisis descriptivo de la base original de la base de los negocios
- load_active_users.py: carga los usuarios activos a base de datos para su inicio de sesión, un usuario activo es aquel que en la base de reseñas haya hecho al menos 5 reseñas.
- load_all_users.py: carga toda la base de usuarios de ser necesario
- load_business.py: carga toda la base de negecios a base de datos, pero únicamente aquellos negocios que se encuentran abiertos, es decir con is_open=true
- preprocesamiento.ipynb: contiene el preprocesamiento de las bases, es decir genera los archivos para que luego el modelo corra.
