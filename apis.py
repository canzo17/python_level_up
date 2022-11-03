#  API REST 
#URL -  metods https://www.google.com/fotos
#metodos - GET POST/PATCH PUT DELETE - forma de digitar cuales son las intenciones de realizar con el servidor
#GET obtiene informacion de los servidores

#Body es un tipo de de mensaje que se envia en los metodos post y delete 
#se envia de forma de diccionario ejem {"name": "Gabriel Can", "birthday": "2000-4-26"}
    #encabezdos de AUTHENTICATION: Bearer xxx-123456, Content-Type: application/jpg Accept: text
# son un codigo que nos se utliza por todos los end points pueden utilizarse par autenticacion 
#Path parameters https://www.google.com/fotos/1  son numeros o codigo que se le pueden agregar a la url 
#para obtener distintos resultados de la API 
#Query params https://www.google.com/fotos?q=python  son parametros utilizados para definir un rango
#o un filtro de busqueda 
#se utiliza la libreria requests para comunicarse con una api 
#utilizar la aplicacion Postman para interactuar de mejor manera con una api 
import requests 

response  = requests.get('https://www.breakingbadapi.com/api/character/random')
#se obtiene el personaje 1 de la api esto nos viene en forma de diccionario 
personaje = response.json()[0]
#obtenermos el primer dato del diccionario que nos manda la api
print(personaje['name'])
print(personaje['birthday'])


