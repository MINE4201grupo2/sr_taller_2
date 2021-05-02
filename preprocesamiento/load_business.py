import pandas as pd
import mysql.connector
from mysql.connector import errorcode
import math
import sys
import csv
import os
import pandas as pd

#Configuración de la conexión a Mysql
try:
  cnx = mysql.connector.connect(user='user_taller2', password='taller2.', host='127.0.0.1', database='taller2')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

cursor = cnx.cursor()

#Lectura del dataframe
columns_data = ['business_id', 'name', 'address','city', 'state', 'categories']

df= pd.DataFrame(columns = ['business_id', 'name', 'address','city', 'state', 'categories'])

CURR_DIR = os.getcwd()
print(CURR_DIR)

chunksize = 10 ** 6

business_json_path = CURR_DIR+'/yelp_dataset/yelp_academic_dataset_business.json'
df_b = pd.read_json(business_json_path, lines=True)
#df_b
# Quitar columnas
df_b = df_b[df_b['is_open']==1]
drop_columns = ['hours','is_open','review_count']
df_b = df_b.drop(drop_columns, axis=1)
df_explode = df_b
#df_explode = df_b.assign(categories = df_b.categories
#                         .str.split(', ')).explode('categories')
#df_explode=df_explode.reset_index()
#df_explode

print("Finish reading file and dtaframes")

# Create a new record
sql = "INSERT INTO `business` (`business_id`, `name`, `address`,`city`,`state`,`latitude`, `longitude`,`categories`) VALUES (%s, %s, %s, %s, %s, %s,%s,%s)"


def isNaN(string):
    return string != string
print(df_explode.index)
for i in df_explode.index: 
  # Execute the query
  var1= df_explode['business_id'][i]
  var2= df_explode['name'][i]
  var3= df_explode['address'][i]
  var4= df_explode['city'][i]
  var5= df_explode['state'][i]
  var6= float(df_explode['latitude'][i])
  var7= float(df_explode['longitude'][i])
  var8= df_explode['categories'][i]


  try:
    #print(var1,var2,var3,var4,var5,var6,var7,var8)
    cursor.execute(sql, (var1,var2,var3,var4,var5,var6,var7,var8))
  except mysql.connector.errors.DataError as err:
    print("Track var 1: "+ var1+ " ")
    sys.exit(1)
  
  # the connection is not autocommited by default. So we must commit to save our changes.
  cnx.commit()


#print(df_artist)
cursor.close()
cnx.close()