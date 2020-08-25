
def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        return 'No es posible dividir por 0'

lista = list(range(10))
divisor = 0 

print (divide_elementos_de_lista(lista, divisor))