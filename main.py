from ManejadorPlan import Planes
from ClaseMenu import Menu
from ClasePlanAhorro import PlanAhorro
import csv
if __name__=="__main__":
    unosPlanes=Planes()
    unosPlanes.inicializar()
    #print("Hola")
    #print(unosPlanes)
    #unosPlanes.mostrarDespuesValor()    
    #unosPlanes.mostrarValorLicitar()
    #unosPlanes.modificarCantCuotas()
    bandera = False
    while not bandera:
        print("MENU DE OPCIONES")
        print("0 Salir")
        print("1 ITEM 5.1: Actualizar valor  del vehiculo de cada plan")
        print("2 ITEM 5.2: Dado un valor, mostrar el codigo del plan, modelo y version del vehiculo cuyo valor de la cuota sea inferior al valor dado")
        print("3 ITEM 5.3: Mostrar el monto que se debe haber pagado para licitar el vehiculo ")
        print("4 ITEM 5.4: Dado el codigo de un plan, modificar la cantidad de cuotas que debe tener para licitar")

        opcion = int(input('Ingrese una opcion:'))
        unmenu=Menu()
        unmenu.opcion(opcion,unosPlanes)
        bandera = int(opcion)== 0