#servidor usuario

from BD.conexion import DAO
import funciones

def menuPrincipal():
    continuar = True
    while continuar:
        opcionCorrecta = False
        while not opcionCorrecta:
            print("= Menú principal =")
            print("1. Listar cursos")
            print("2. Registrar curso")
            print("3. Actualizar curso")
            print("4. Eliminar curso")
            print("5. Salir")
            print("=")
            opcion = int(input("Seleccionar una opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 5:
                continuar = False
                print("Gracias por usar este sistema...")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dao = DAO()

    if opcion == 1:
        try:
            cursos = dao.ListarCursos()
            if len(cursos) > 0:
                funciones.ListarCursos(cursos)  # Llama a la función con la lista de cursos
            else:
                print("No se encontraron cursos...")
        except Exception as e:
            print("Ocurrió un error:", str(e))
    elif opcion == 2:
        print("Registro")
    elif opcion == 3:
        print("Actualización")
    elif opcion == 4:
        print("Eliminación")
    else:
        print("Opción no válida...")

menuPrincipal()

