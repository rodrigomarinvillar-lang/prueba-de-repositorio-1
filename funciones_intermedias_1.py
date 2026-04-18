# 1. Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431

# 2. Iterar a través de una lista de diccionarios

cantantes_2 = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario(lista):
    for diccionario in lista:
        formato = []
        for llave, valor in diccionario.items():
            formato.append(f"{llave} - {valor}")
        print(", ".join(formato))

print("\n--- Resultado Tarea 2 ---")
iterarDiccionario(cantantes_2)

# 3. Obtener valores de una lista de diccionarios

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        print(diccionario[llave])
print("\n--- Resultado Tarea 3 (Nombres) ---")
iterarDiccionario2("nombre", cantantes_2)
print("\n--- Resultado Tarea 3 (Países) ---")
iterarDiccionario2("pais", cantantes_2)

# 4. Iterar a través de un diccionario con valores de lista

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    for llave, lista_valores in diccionario.items():
        print(f"{len(lista_valores)} {llave.upper()}")
        for valor in lista_valores:
            print(valor)
        print("") 
print("\n--- Resultado Tarea 4 ---")
imprimirInformacion(costa_rica)