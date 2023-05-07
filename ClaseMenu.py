from ManejadorPlan import Planes
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            3:self.opcion4,
                            0:self.salir
                          }
    def opcion(self,op,lista):
        print(op)
        func=self.__switcher.get(op,lambda: print("Opción no válida"))
        func(lista)

    def salir(self,lista):
        print('Usted salio del programa')
    def opcion1(self,lista,):
        lista.ActualizarValor()


    def opcion2(self,lista):
        lista.mostrarDespuesValor()

    def opcion3(self,lista):
        lista.mostrarValorLicitar()

    def opcion4(self,lista):
        lista.modificarCantCuotas()
