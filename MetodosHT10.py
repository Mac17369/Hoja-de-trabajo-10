#Hoja de trabajo 10
#Integrantes:
#Rodrigo Urrutia
#Kevin Macario 17369
#Raul Monzon
#Clase de metodos
#

from neo4jrestclient.client import *
from neo4jrestclient import client

db = GraphDatabase("http://localhost:7474", username="neo4j", password="12345")

#Categorias de la base de datos
doctores = db.labels.create("Doctores")
pacientes = db.labels.create("Pacientes")
drogas = db.labels.create("Drogas")

#Metodos
def ingresarDoctor(nombre, telefono, especialidad):
    doctor = db.nodes.create(Nombre = nombre, Telefono = telefono, Especialidad = especialidad)
    doctores.add(doctor)
    print("Se ha ingresado un nuevo doctor\n")

def ingresarPaciente(nombre, telefono, sexo):
    paciente = db.nodes.create(Nombre = nombre, Telefono = telefono, Sexo = sexo)
    pacientes.add(paciente)
    print("Se ha ingresado un nuevo paciente\n")

def ingresarPacienteDoc():

def consultaEspecialidad():

def ingresarRelacion():

def recomendacionPersona():

def recomendacionDoctor():
