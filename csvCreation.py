import csv, os
from dbOperations import *

def csvCreation():
    cursor.execute("SELECT provincia, localidad FROM localidades ORDER BY provincia")
    results = cursor.fetchall()

    folder = 'localidades_por_provincia'
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    for provincia in results:
        with open(f'localidades_por_provincia/{provincia[0]}.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['localidad'])
            cursor.execute(f"SELECT localidad FROM localidades WHERE provincia = '{provincia[0]}'")
            localidades = cursor.fetchall()
            for localidad in localidades:
                csv_writer.writerow([localidad[0]])
        
        print('Archivos creados exitosamente')
csvCreation()