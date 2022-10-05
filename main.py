import random
from os import system


def mezclar(): 
    numeros = [
            [i for i in range(1,8)],
            [i for i in range(8,15)],
            [i for i in range(15,22)]]    
    t = []
    numeros_mezclados = [[],[],[]]

    for fila in numeros:
        for numero in fila:
            t.append(numero)
    random.shuffle(t)
    for fila in numeros_mezclados:
        for i in range(7):
            fila.append(t.pop())

    return numeros_mezclados

def truco():
    #declarando y mezclando


    numeros_mezclados = mezclar()
    print(numeros_mezclados)
    reacomodo = [[],[],[]]
    seleccion: int

    #aqui empieza lo chido
    for i in range(3):
        for j, fila in zip(range(3), numeros_mezclados):
            print(f'{j+1}\t{fila}\n')

        if i == 0:
            seleccion = int(input('Escoja un numero, memorícelo, e indique la fila en la que se encuentra su numero: '))-1
        if i > 0:
            seleccion = int(input('Indique la fila en la que se encuentra su numero: '))-1

        numeros_mezclados.insert(1, numeros_mezclados.pop(seleccion))
        
        temp=[]
        temp_indx = 0
        
        
        for fila in numeros_mezclados:
            for numero in fila:
                temp.append(numero)

        print(temp) 
        for k in range(7):
            for l in range(3):
                reacomodo[l][k] = temp[temp_indx]
                temp_indx+=1

        numeros_mezclados = reacomodo

    print(f'Su numero es: {numeros_mezclados[1][3]}')
    
    

    for i in range(3):
        for i in range(7):
            pass




    # seleccion = int(input('Escribe un numero: '))

    # for list in reacomodo:






    print(numeros_mezclados[1][4])


    

def main():
    truco()
if __name__ == '__main__':
    main()