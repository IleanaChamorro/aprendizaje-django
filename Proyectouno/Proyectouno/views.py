from django.http import HttpResponse
from django.template import Template, Context
import datetime
from django.template import loader
from django.shortcuts import render


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido


#Creacion Primera vista
def saludo(request):

    personauno=Persona('Profesor Ileana', 'xxxxx')

    #nombre = 'Juan'
    #apellido = 'Diaz'

    temasDelCurso =  ['Plantillas', 'Modelos', 'Formularios', 'Vistas', 'Despliegue app']

    fecha_actual=datetime.datetime.now()
    #Carga plantilla forma manual
    #doc_externo = open("/home/hernan/Escritorio/ProyectosDjango/Proyectouno/Proyectouno/plantilla/index.html")

    #carga de plantilla optima, solo permite pasar un diccionario
    #documento_externo = loader.get_template('index.html')
    #En el argumento lee el doc externo
    #plantilla=Template(doc_externo.read())

    

    #doc_externo.close()

    #Creacion contexto(se almacena informacional adicional como funciones o varibles)
    #ctx=Context({'nombre_persona':'Manuel', 'apellido_persona': personauno.apellido, "momentoactual": fecha_actual, 'temas':temasDelCurso})
    #documento=documento_externo.render({'nombre_persona':'Manuel', 'apellido_persona': personauno.apellido, "momentoactual": fecha_actual, 'temas':temasDelCurso})
    #documento=plantilla.render(ctx)
    #Devuelve una respuesta con ese mensaje
    #Metodo render, tiene dos parametros: request (obligatorio) y el template que debe ir entre comillas, el tercer argumento opcional es el contexto
    return render (request, "index.html", ({'nombre_persona':'Manuel', 'apellido_persona': personauno.apellido, "momentoactual": fecha_actual, 'temas':temasDelCurso}))
def cursoD(request):
    fecha_actual=datetime.datetime.now()

    return render(request, 'CursoD.html', {'dameunafecha': fecha_actual})
def despedida(request):

    return HttpResponse('Adios a la primera pagina')

def dameunafecha(request):
    fecha_actual = datetime.datetime.now()

    return render(request, "CursoD.html")