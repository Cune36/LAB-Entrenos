import csv
import datetime
from collections import namedtuple
Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(tabla):
    with open(tabla, encoding = 'utf-8') as f:
       
        lector = csv.reader(f)
        next(lector)
        res = []
        for (tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido) in lector:
            tipo = str(tipo)
            fechahora =  datetime.datetime.strptime(fechahora, "%d/%m/%Y %H:%M")
            ubicacion = str(ubicacion)
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            if compartido == 'S':
                compartido = True
            else:
                compartido = False
            tupla = Entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido)
            res.append(tupla)
    return res

def tipos_entreno(lista_entrenos):
    ejercicios = set()

    for entrenamiento in lista_entrenos:
        ejercicios.add(entrenamiento.tipo)
    lista = list(ejercicios)
    lista.sort()
    return lista

def entrenos_duracion_superior(lista_entrenos, d):
    lista = []
    for entrenamiento in lista_entrenos:
        if entrenamiento.duracion > d:
            lista.append(entrenamiento)
    return lista

def suma_calorias(lista_entrenos, f_inicio, f_fin):
    total = 0

    #Conversión a tipo datetime
    f_inicio_c = datetime.datetime.strptime(f_inicio, "%d/%m/%Y %H:%M")
    f_fin_c = datetime.datetime.strptime(f_fin, "%d/%m/%Y %H:%M")
    for e in lista_entrenos:
        if f_inicio_c <= e.fechahora <= f_fin_c:
            total += e.calorias
    return total

if __name__ == '__main__':
    lista = lee_entrenos('data\entrenos.csv')
    print(lista)    

