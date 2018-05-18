#Hoja de trabajo 10
#Integrantes:
#Rodrigo Urrutia
#Kevin Macario 17369
#Raul Monzon
#Clase de metodos
#

from neo4jrestclient.client import GraphDatabase    
from neo4jrestclient import client

db = GraphDatabase("http://localhost:7474", username="neo4j", password="12345")

#Categorias de la base de datos
doctores = db.labels.create("Doctores")
pacientes = db.labels.create("Pacientes")
drogas = db.labels.create("Drogas")

#Metodos
def ingresarDoctor(nombre, colegiado, especialidad, telefono):
    doctor = db.nodes.create(Nombre = nombre, Colegiado = colegiado, Especialidad = especialidad, Telefono = telefono)
    doctores.add(doctor)
    print("Se ha ingresado un nuevo doctor\n")

def ingresarPaciente(nombre, telefono):
    paciente = db.nodes.create(Nombre = nombre, Telefono = telefono)
    pacientes.add(paciente)
    print("Se ha ingresado un nuevo paciente\n")

def ingresarPacienteDoc():

def consultaEspecialidad():
    print("Especialidades existentes: ")
    q = "MATCH (u: Doctores) RETURN u"
    especialidades = db.query(q, returns=(client.Node, str, client.Node))
    listaEspecialidades = []
    final = len(especialidades)
    for i in especialidades:
        if(final>0):
            elemento = r[0]["especialidad"]
            listaEspecialidades.append(elemento)
    Consulta = raw_input("Que especialidad desea? ")
    q = "MATCH (u: Doctores) WHERE u.especialidad="' +Consulta+ '"RETURN u"
    especialidades = db.query(q, returns=(client.Node, str, client.Node))
    for j in especialidades:
         #print("Se encontro al Doctor(a) %s con numero de contacto %s" % (r[0]["name"],r[0]["telefono"]))
    #if(len(results)==0):
      #  print("\nNo se encontro ningun doctor(a) con dicha especialidad")
    #else:
        #pass


        
def ingresarRelacion():

def recomendacionPersona():

def recomendacionDoctor():
