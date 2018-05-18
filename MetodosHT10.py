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
    print("\nEstos son los pacientes disponibles en la base de datos: ")
    q = 'MATCH (u: Pacientes) RETURN u'
    paciente = db.query(q, returns=(client.Node, str, client.Node))
    for k in paciente:
        print(" - " + "%s" % (k[0]["nombre"]))
    nombreP = raw_input("Ingrese el nombre del Paciente que desea relacionar: ")
    print("\nEstos son los doctores disponibles en la base de datos: ")
    q = 'MATCH (u: Doctores) RETURN u'
    paciente = db.query(q, returns=(client.Node, str, client.Node))
    for k in paciente:
        print(" - " + "%s" % (k[0]["nombre"]))
    nombreD = raw_input("Ingrese el nombre del Doctor que desea relacionar: ")
    q = 'MATCH (u: Doctores) WHERE u.nombre="'+nombreD+'" RETURN u'
    obtenidos = db.query(q, returns=(client.Node))
    final = len(obtenidos)
    q = 'MATCH (u: Pacientes) WHERE u.nombre="'+nombreP+'" RETURN u'
    nodo = db.query(q, returns=(client.Node))
    finalL = len(nodo)
    if(final>0 and finalL>0):
        fecha = raw_input("Fecha en la que visito al DOctor: ")
        nombre = raw_input("Medicina preescribida: ")
        inicio = raw_input("Inicio de tratamiento ")
        concluye = raw_input("Final de tratamiento: ")
        cantidad = raw_input("Dosis preescribida: ")
        medicinaNueva = db.nodes.create(nombre=nombre,Inicio=inicio,Final=concluye,Cantidad=cantidad)
        Drogas.add(medicinaNueva)
        for k in obtenidos:
            for i in nodo:
                i[0].relationships.create("VISITS",k[0],fecha=fecha
                i[0].relationships.create("TAKE",medicinaNueva)
                k[0].relationships.create("PRESCRIBE",medicinaNueva)              
        print("Relacion creada\n")
    else:
        print("No existe nombre")



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
    q = 'MATCH (u: Doctores) WHERE u.especialidad="'+Consulta+'" RETURN u'
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
