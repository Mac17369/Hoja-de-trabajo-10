#Hoja de trabajo 10
#Integrantes:
#Rodrigo Urrutia
#Kevin Macario
#Raul Monzon
#Clase principal
#

from MetodosHT10 import *
from neo4jrestclient.client import GraphDatabase    
from neo4jrestclient import client

#Menu
opcion = 0
while opcion != 8:
    print("1. Ingresar doctor\n 2. Ingresar paciente\n 3. Ingresar que un paciente dado, visita un doctor\n 4. Consultar especialidad de doctor\n 5. Ingresar que una persona conoce a otra\n 6. Recomendacion dado una persona\n 7. Recomendacion dado un doctor especifico\n 8. Salir")
    opcion = input("Ingresar numero de opcion\n")

    if(opcion == 1):
        nombreD = raw_input("Ingrese nombre de doctor: ")
        colegiadoD = raw_input("Ingrese colegiado de doctor: ")
        especialidadD = raw_input("Ingrese especialidad de doctor: ")
        telefonoD = raw_input("Ingrese telofono de doctor: ")
        ingresarDoctor(nombreD, colegiadoD, especialidadD, telefonoD)

    if(opcion == 2):
        nombreP = raw_input("Ingrese nombre de paciente: ")
        telefonoP = raw_input("Ingrese telefono de paciente: ")
        ingresarPaciente()

    if(opcion == 3):
        ingresarPacienteDoc()

    if(opcion == 4):
        consultaEspecialidad()

    if(opcion == 5):
        ingresarRelacion()

    if(opcion == 6):
        recomendacionPersona()

    if(opcion == 7):
        recomendacionDoctor()

    if(opcion == 8):
        print("Usted ha salido del programa")
