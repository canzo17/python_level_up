#se requieren protocolos de comunicacion para 
# frame woorks resuelven una serie de problemas unificando una 
# gran cantidad de librerias 
# los frameworks mas utilizados son wabe to pay, flask, django
# los ultimos dos son los mas utilizados 
# jango es un framework enfocado en ralizar monolitos que es donde 
# se tiene el backend y el frontend en un mismo servdor sin la necesidad
# de una aPI para la comunicacion 
# FLask es utilizada para servir como backen como una API utilizada
# de forma sencilla 
# backend rapido y sencillo se utiliza Flask 
# jango es mas para realizar backend y frontend seria un fullstack
# Flask no soporta cuestionarios django si
#  
# En el desarrollo de sofware se requiere que la tecnologia sea
# famosa para tener mayor documentacion y mantenimiento 
# 
from flask import Flask, request, redirect

app = Flask(__name__) 
#esto le sirve a flask para saber donde esta ubicado para importar 
#las librerias
#crear la aplicacion 
 
 #crear nuestro primer end point y definirle una ruta 
@app.route('/Hi') # /saludo es la ruta
#@ decorador, permite implementar funcionalidades sin tener que estar importandolas y mandarlas a llamar
def hello_world():
    return "Hello world"
#la funcion es creada a la vez que se crea la route y realizara la accion cuando
# la api llame a la direccion que se encuentra en los parentesis
# #

@app.route('/')
def index():
    return "Welcome"

@app.route('/healthcheck')
def health_check():
    return "Service healthy"

#se usa esta direccion ya que existen herramientas que se encargan de monitorear un APi
#y estas ingresan a esta direccion para asegurarse de que este estable o exista la conexion#

@app.route('/saludar/<nombre>') #pap paramet
def saludar(nombre):
    return f"hola {nombre}"

#los parametros pueden ser int, string, float, path(tipo de string que acepta / para escribir rutas)
#uuid un tipo de llave que se asegura de que sea un valor unico
@app.route('/Edad/<int:numero>') #pap paramet condicionado para solo ingresar int
def Edad(numero):
    return f"tienes {numero} años"

#flask asigna como metodo get siempre que utilizamos @app.route


@app.route('/helado', methods = ['POST','PUT'])
def helado():
    return 'toma tu helado'
#asignar varios metodos en especifico al route 

@app.post('/animal')
def animal():
    return 'bienvenido al zoo'

@app.put('/prue_put')
def prueba():
    return 'solo funciona con el motodo put'
#asignar un metodo en especifico

@app.post('/llave')
def llave_post():
    return 'Estas guardando llaves'

@app.get('/llave')
def llave_get():
    return 'Estas consultando las llaves'
#se puede usar la misma direccion para 2 metodos diferentes para distintas 
#acciones

@app.post('/registro')
def registro():
    return {
        'method' : request.method, #muestra el metodo que se esta utilizando
        'body' : request.form, #se obtiene info de un formulario form-data de body
        'date' : request.date
    }
#un diccionario es muy parecido a un json
#esta funcion se puede implementar al eportar de la libreria la funcion request

@app.errorhandler(404)
def not_found(error):
    return 'Endpoint not found', 404
#realizamos un endpoint que muestre el error 404 en vez de mostra el json de postman

@app.route('/redirect')
def redirect_endpoint():
    return redirect('/')
#con esta funcion se redirige una url a o otra de nuestra eleccion
#se debe tomar el cuenta con que metodo se quiere trabajar para la redireccion

#con esto tenemos nuestra primer API
#identificar version de flask -> flask --version
#para correr la api usamos 
#un json no tiene muchas diferencias contra un diccionario
#flask --app nombre_archivo run
