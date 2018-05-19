#Hoja de trabajo 10
#Integrantes:
#Kevin Macario 17369
#Raul Monzon 17014
#Clase principal

from MetodosHT10 import *
from neo4jrestclient.client import GraphDatabase    
from neo4jrestclient import client

#Menu
opcion = 0
print ("************Bienvenidio************")
while opcion != 8:
    print ("______________MENU______________")
    print ("1. Ingresar doctor")
    print ("2. Ingresar paciente")
    print ("3. Ingresar que un paciente dado, visita un doctor")
    print ("4. Consultar especialidad de doctor")
    print ("5. Ingresar que una persona conoce a otra")
    print ("6. Recomendacion dado una persona")
    print ("7. Recomendacion dado un doctor especifico")
    print ("8. salir")
    opcion = input("Ingresar numero de opcion\n")

    if(opcion == 1):
        nombreD = raw_input("Ingrese nombre de doctor:\n ")
        colegiadoD = raw_input("Ingrese colegiado de doctor: \n")
        especialidadD = raw_input("Ingrese especialidad de doctor: \n")
        telefonoD = raw_input("Ingrese telofono de doctor: \n")
        MetodosHT10.ingresarDoctor(nombreD, colegiadoD, especialidadD, telefonoD)
    else:
        if(opcion == 2):
            nombreP = raw_input("Ingrese nombre de paciente: \n")
            telefonoP = raw_input("Ingrese telefono de paciente: \n")
            ingresarPaciente()
        else:
            if(opcion == 3):
                ingresarPacienteDoc()
            else:
                if(opcion == 4):
                    consultaEspecialidad()
                else:
                    if(opcion == 5):
                        ingresarRelacion()
                    else:
                        if(opcion == 6):
                            recomendacionPersona()
                        else:
                            if(opcion == 7):
                                recomendacionDoctor()
                            else:
                                print("Usted ha salido del programa")
