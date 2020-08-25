nombre_usuario1 = input('Bienvenido usuario 1, Por favor introduce nombre: ')
edad_usuario1 = int(input('Por favor introduce tu edad: '))
nombre_usuario2 = input('Bienvenido usuario 2, Por favor introduce nombre: ')
edad_usuario2 = int(input('Por favor introduce tu edad: '))

if edad_usuario1 > edad_usuario2:
    print(f'{nombre_usuario1} es mayor que {nombre_usuario2}')
elif edad_usuario1 < edad_usuario2:
    print(f'{nombre_usuario2} es mayor que {nombre_usuario1}')
else:
    print(f'{nombre_usuario1} y {nombre_usuario2} tienen la misma edad')