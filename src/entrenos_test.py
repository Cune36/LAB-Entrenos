import entrenos

if __name__ == "__main__":
    datos_entrenos = entrenos.lee_entrenos("data\entrenos.csv")
    print(f"Tres primeros entrenos:{datos_entrenos[:3]}")
    ejercicios_tipos = entrenos.tipos_entreno(datos_entrenos)
    print(f"Tipos de entrenos: {ejercicios_tipos}")
    duracion_superior = entrenos.entrenos_duracion_superior(datos_entrenos, int(50))
    print("Entrenamientos que duran más de 50 minutos: ")
    for r in duracion_superior:
        print (r)
    calorias = entrenos.suma_calorias(datos_entrenos , "21/2/2021 2:13" , "21/2/2021 5:01")
    print(f"El total de calorias quemadas es de {calorias} calorias en total. ")
    