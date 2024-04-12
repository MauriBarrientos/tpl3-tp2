import sys 
import MySQLdb
import csv 


def dbConnection():
    try:
        db = MySQLdb.connect("localhost", "root","","argentina")
    except MySQLdb.Error as e:
        print ("No se pudo conectar:",e)
        sys.exit(1)
    print ("Conectado a la base de datos")
    return db

db = dbConnection()
cursor = db.cursor()

def dbCreation(db):
    
    sql_delete = "DROP TABLE IF EXISTS localidades"
    cursor.execute(sql_delete)
    db.commit()
    sql_create = """CREATE TABLE IF NOT EXISTS localidades (
    provincia VARCHAR(255),
    id INT,
    localidad VARCHAR (255),
    cp INT,
    id_prov_mstr INT
    )"""
    cursor.execute(sql_create)

dbCreation(cursor)


def dbInsert():
    with open('localidades.csv', newline='', mode='r', encoding= 'utf-8') as archivo_csv:
        lectura_csv = csv.reader(archivo_csv, delimiter=',' , quotechar='"')
        next (lectura_csv)
        try:
            for row in lectura_csv:
                cursor.execute (f"INSERT INTO localidades, (provincia, id, localidad, cp, id_prov_mstr) VALUES ('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}')") 
        except csv.Error:
            print ("Error leyendo el archivo")
            sys.exit(1)
    try: 
        db.commit()
        print('Datos insertados exitosamente')
    except:
        db.rollback()

dbInsert(cursor)

def dbSelect():
    select = "SELECT * FROM localidades"
    cursor.execute(select)
    print(cursor.fetchall())

dbSelect(cursor)


def groupByPr():
    cursor.execute("""SELECT localidad, count(localidad) FROM localidades GROUP BY localidad""")
    results = cursor.fetchall()
    print(results)

groupByPr(cursor)

