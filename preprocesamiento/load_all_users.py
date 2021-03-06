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
columns_data = ['user_id']

df_users= pd.DataFrame(columns = ['user_id'])

CURR_DIR = os.getcwd()
print(CURR_DIR)

chunksize = 10 ** 6

user_path = CURR_DIR+'/yelp_dataset/yelp_academic_dataset_user.json'
#user_path = CURR_DIR+'/yelp_dataset/yelp_user_5.json'
with  pd.read_json(user_path, lines=True,chunksize=chunksize) as reader:
    for chunk in reader:
        print(f"{chunk.shape[0]} out of {chunksize:,} ")
        df_users = df_users.append(chunk[['user_id']])
print(df_users)
print("Finish reading file and dtaframes")

# Create a new record
sql_users = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"

def isNaN(string):
    return string != string
var2 = 'fe3ce91a4a305670820fa708624a0f9f6c8c46770da510a5572c105dd0310333dfddfaaa29f76b76a4827bd0793896c5acad8d3240b1aaf7611ab224ff7a97d72c5e244e85af55af093f687af311dbcfcadccd460fe8610a6b1fee2386f323634d13604a'
for i in df_users.index: 
  # Execute the query
  var1= None if isNaN(df_users['user_id'][i]) else ''.join([c for c in df_users['user_id'][i].strip() if c not in ['\t', '\n', '\f', '\r','\u000B','\u0085','\u2028','\u2029','\u0022', '\u005C', '\u0027', '"']]) 

  try:
    cursor.execute(sql_users, (var1+'@email.com',var2))
  except mysql.connector.errors.DataError as err:
    print("Track var 1: "+ var1+ " ")
    sys.exit(1)
  
  # the connection is not autocommited by default. So we must commit to save our changes.
  cnx.commit()


#print(df_artist)
cursor.close()
cnx.close()