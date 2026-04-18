print('---Ejercicio 1: Basico---')
for i in range(101):
    print(i)
print('\n--- Ejercicio 2: Multiplos de 2---')
for i in range(2, 501, 2):
    print(i)
print('\n--- Ejercicio 3: contando vanilla ice cream---')
for i in range(1,101):
    if i % 10 == 0:
        print('baby')
    elif i % 5 == 0:
        print('ice ice')
    else:
        print(i)
print('\n--- Ejercicio 4: wow. numero gigante a la vista---')
suma_total = 0 
for i in range(0,500001,2):
    suma_total += i
print(f'La suma total es: {suma_total}')
print('\n--- Ejercicio 5:  regresame al 3---')
for i in range(2024, 0, -3):
    print(i)
print('\n--- Ejercicio 6:  contador dinamico---')
numInicial = 3
numFinal = 10
multiplo = 2
for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)