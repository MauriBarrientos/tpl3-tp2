from csvCreation import *
from dbOperations import *

#Función que reúne la lógica general.
def app():
    csvCreation()
    dbCreation(db)

app()