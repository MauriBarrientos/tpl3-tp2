import csv
import os
from dbOperations import *

#Funcion para crear csvs
def csvCreation():
    cursor.execute("SELECT provincia, localidad FROM localidades ORDER BY provincia")
    results = cursor.fetchall()

    folder = 'localidades_por_provincia'
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Preparar los datos para escribir en los archivos CSV
    data = {}
    for provincia, localidad in results:
        if provincia not in data:
            data[provincia] = []
        data[provincia].append(localidad)

  
    for provincia, localidades in data.items():
        with open(f'{folder}/{provincia}.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['localidad'])
            csv_writer.writerows([[localidad] for localidad in localidades]) 
        
        print(f'Archivo para {provincia} creado exitosamente')

csvCreation()