import time
def ListarCursos(cursos):
    print("Cursos: ")
    contador = 1
    for cur in cursos:
        datos = "{0}. Código: {1} | Nombre: {2} | Apellido: {3} "
        print(datos.format(contador, cur[0], cur[1], cur[2])) #Mide el tiemo de demora "1 segundo"
        contador += 1
        time.sleep(1)

  
