# -*- coding: cp1252 -*-

#Hoja de trabajo 10
#Integrantes:
#Kevin Macario 17369
#Raul Monzon 17014
#Clase de metodos


from neo4jrestclient.client import GraphDatabase    
from neo4jrestclient import client

db = GraphDatabase("http://localhost:7474", username="neo4j", password="12345")

#Categorias de la base de datos
doctores = db.labels.create("Doctores")
pacientes = db.labels.create("Pacientes")
drogas = db.labels.create("Drogas")

#Metodos

#Método para agregar nuevo doctor, su información se pasa por referencia desde la clase principal
def ingresarDoctor(nombre, colegiado, especialidad, telefono):
    doctor = db.nodes.create(Nombre = nombre, Colegiado = colegiado, Especialidad = especialidad, Telefono = telefono)
    doctores.add(doctor)
    print("Se ha ingresado un nuevo doctor\n")
    
#Método para agregar nuevo paciente, su información se pasa por referencia desde la clase principal
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
                i[0].relationships.create("VISITS",k[0],fecha=fecha)
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
         print("Se encontro al Doctor(a) %s con numero de contacto %s" % (r[0]["name"],r[0]["telefono"]))
    if(len(results)==0):
        print("\nNo se encontro ningun doctor(a) con dicha especialidad")
    else:
        pass

#Se agrega una nueva relación entre personas (se conocen)
def ingresarRelacion():
    print("\nLas personas que se encuentran en la base de datos son: ")

    #tomamos los nombres de los pacientes
    print("Pacientes: ")
    x = 'MATCH (u: Pacientes) RETURN u'
    resultados = db.query(x, returns=(client.Node, str, client.Node))
    for r in resultados:
        print(" - " + "%s" % (r[0]["Nombre"]))
        
    #tomamos los nombres de los doctores
    print("Doctores: ")
    x = 'MATCH (u: Doctores) RETURN u'
    resultados = db.query(x, returns=(client.Node, str, client.Node))
    for r in resultados:
        print(" - " + "%s" % (r[0]["Nombre"]))

    p1 = raw_input("Ingrese el nombre de la primera persona: ")
    p2 = raw_input("Ingrese el nombre de la segunda persona: ")
    #se buscan los nombres en la lista
    q = 'MATCH (u: Doctores) WHERE u.name="'+p1+'" RETURN u'
    resultado1 = db.query(q, returns=(client.Node))
    largo1 = len(resultado1)
    q = 'MATCH (u: Pacientes) WHERE u.name="'+p1+'" RETURN u'
    resultado2 = db.query(q, returns=(client.Node))
    largo2 = len(resultado2)
    q = 'MATCH (u: Pacientes) WHERE u.name="'+p2+'" RETURN u'
    resultado3 = db.query(q, returns=(client.Node))
    largo3 = len(resultado3)
    q = 'MATCH (u: Doctores) WHERE u.name="'+p2+'" RETURN u'
    resultado4 = db.query(q, returns=(client.Node))
    largo4 = len(resultado4)
    #si el largo de los nombres es mayor a 0 se hace la conexión
    if(largo1>0 and largo3>0):
        fecha = raw_input("Ingrese el año desde que se conocen: ")
        for r in resultado1:
            for i in resultado3:
                r[0].relationships.create("KNOWS",i[0],since=fecha)
        print("La relacion fue ingresada correctamente")
    elif(largo1>0 and largo4>0):
        fecha = raw_input("Ingrese el año desde que se conocen: ")
        for r in resultado1:
            for i in resultado4:
                r[0].relationships.create("KNOWS",i[0],since=fecha)
        print("La relacion fue ingresada correctamente")
    elif(largo2>0 and largo3>0):
        fecha = raw_input("Ingrese el año desde que se conocen: ")
        for r in resultado2:
            for i in resultado3:
                r[0].relationships.create("KNOWS",i[0],since=fecha)
        print("La relacion fue ingresada correctamente")
    elif(largo2>0 and largo4>0):
        fecha = raw_input("Ingrese el año desde que se conocen: ")
        for r in resultado2:
            for i in resultado4:
                r[0].relationships.create("KNOWS",i[0],since=fecha)
        print("Se ingreso correctamente")
    else:
        print("No se encontraron los nombres")

def recomendacionPersona():
print("\nEstos son los pacientes disponibles en la base de datos: ")
    q = 'MATCH (u: Pacientes) RETURN u'
    resultado = db.query(q, returns=(client.Node, str, client.Node))
    for r in resultado:
        print(" - " + "%s" % (r[0]["name"]))
        
    pac1 = raw_input("¿Qué paciente necesita un doctor? ") 
    q = 'MATCH (u: Pacientes)-[r:KNOWS]->(m:Pacientes) WHERE u.nombre="'+pac1+'" RETURN u, type(r), m' 
    resultado_paciente = db.query(q, returns=(client.Node, str, client.Node))
    #lista con los pacientes que conocen al paciente ingresado
    amigos = []
    for r in resultado_paciente:        
        if(len(resultado_paciente)>0):
            amigo_nombre = r[2]["name"]
            amigos.append(amigo_nombre)  
    
    print("\nEspecialidades disponibles en la base de datos: ") 
    q = 'MATCH (u: Doctores) RETURN u'
    resultado = db.query(q, returns=(client.Node, str, client.Node))
    lista_especialidades = []
    for r in resultado:        
        if(len(resultado)>0):
            esp = r[0]["especialidad"]
            lista_especialidades.append(esp)

        
    especialidad_deseada = raw_input("¿Qué especialidad necesita?") #Se pide la especialidad del Dr que se recomendara
    q = 'MATCH (u: Doctores) WHERE u.especialidad="'+especialidad_deseada+'" RETURN u'
    resultado_doctores = db.query(q, returns=(client.Node, str, client.Node))
    #lista con los doctores que tienen la especialidad deseada
    Especialistas = []
    for r in resultado_doctores:         
        if(len(resultado_doctores)>0):
            doctor_especialidad = r[0]["name"]
            Especialistas.append(doctor_especialidad) 
    #lista con doctores recomendados
    dr_recomendados = []
    #se recorre la lista de personas que conocen al paciente
    for i in amigos: 
        q = 'MATCH (u: Pacientes)-[r:VISITS]->(m:Doctores) WHERE u.name="'+i+'" RETURN u, type(r), m'
        doctores_consultados = []
        resultadou = db.query(q, returns=(client.Node, str, client.Node))
        for r in resultadou:            
            if(len(resultadou)>0):
                DrVisitado = r[2]["nombre"]
                doctores_consultados.append(DrVisitado) 
        listaRepetidos = RepetidosEntreDosListas(doctores_consultados,Especialistas)
        if(len(listaRepetidos) > 0):
            for e in listaRepetidos:
                dr_recomendados.append(e)
    if(len(dr_recomendados) > 0):       
        print("\nSe recomiendan estos doctores.")
    else:
        print("\nIntente de nuevo.")

def recomendacionDoctor():
    
    print("\nDoctores en la base de datos: ")
    #se toman los doctores de la base de datos
    q = 'MATCH (u: Doctores) RETURN u'
    results1 = db.query(q, returns=(client.Node, str, client.Node))
    for r in results1:
        print(" - " + "%s" % (r[0]["name"]))
        
    doctor1 = raw_input("Ingrese nombre del doctor: ")    
    #se busca doctor ingresado
    q = 'MATCH (u: Doctores)-[r:KNOWS]->(m:Doctores) WHERE u.nombre="'+doctor1+'" RETURN u, type(r), m' 
    resultado = db.query(q, returns=(client.Node, str, client.Node))
    ConocidosDr = []
    for r in resultado:
        print (" - " + "%s" % (r[2]["name"]))
        if(len(resultado) > 0 ):
            conocidoDelDr = r[2]["name"]
            ConocidosDr.append(conocidoDelDr) 
    
    print("\nEspecialidades disponibles en la base de datos: ") 
    q = 'MATCH (u: Doctores) RETURN u'
    results = db.query(q, returns=(client.Node, str, client.Node))
    listaEsp = []
    for r in results:        
        if(len(results)>0):
            esp = r[0]["especialidad"]
            listaEsp.append(esp)
    

    especialidadDada = raw_input("Ingrese la especialidad que desea recomendar: ") 
    q = 'MATCH (u: Doctores) WHERE u.especialidad="'+especialidadDada+'" RETURN u'
    resultsD = db.query(q, returns=(client.Node, str, client.Node))
    Especialistas = []
    for r in resultsD:         
        if(len(resultsD)>0):
            DrEsp = r[0]["name"]
            Especialistas.append(DrEsp)

    DrsRecomendados = DosListas(ConocidosDr,Especialistas) 
    if(len(DrsRecomendados)>0):
        print ("Los doctores recomendados son los siguientes: ")
        for i in DrsRecomendados:
            print(" - " + i)
    else:
        print ("Intente de nuevo.")
    

#este método nos ayuda a saber que personas se encuentran en la lista de conocidos y posible recomendados
def RepetidosEntreDosListas(lista1,lista2):    
    if(len(lista1)>0 and len(lista2)>0):
        lista_nueva = []
        for i in lista1:
            if (i in lista2 and i not in lista_nueva):
                lista_nueva.append(i)
    return lista_nueva
