class Cajero:

    dinero_disponible = 10000

    limite = 500

    detalles_retiro = []

    cliente = None

    opciones = {

        "consulta": 1,

        "retiro": 2,

        "cancelar": 3

    }

    opcion_retiro = {

        "5": 10,

        "4": 50,

        "3": 100,

        "2": 200,

        "1": 500

    }

    billetes = [

        # billetes de : cantidad

        [100, 300],

        [50, 11],

        [20, 10],

        [10, 15]

    ]



    def existeOpcionRetiro(self, seleccion):

        if seleccion == '0': return True

        if self.opcion_retiro.get(seleccion) == None: return False

        return True;



    def procesarRetiro(self, seleccion, cliente):

        self.cliente = cliente

        if seleccion == '0':

            repetir = True

            while repetir:

                separador()

                print('- ¿Cuánto desea retirar?')

                monto_seleccionado = input();

                try:

                    monto_seleccionado = int(monto_seleccionado);

                    repetir = False

                except Exception as e:

                    print("- Por favor, seleccione un monto correcto")

        else:

            monto_seleccionado = self.opcion_retiro.get(seleccion)



        if not self.validacion(monto_seleccionado): return



        return self.retirar(monto_seleccionado)



    def reporteRetiro(self):

        separador()

        print('- Repote de Retiro:')

        for denominacion, cantidad in self.detalles_retiro:

            mensaje = '- - Billetes de {0}: {1} - total {2}'

            print(mensaje.format(denominacion, cantidad, denominacion*cantidad))   

    

    def validacion(self, monto):

        if monto > self.dinero_disponible:

            print('- Actualmente, no podemos dispensar esa cantidad de dinero')

            return False

        elif monto > self.limite:

            print('- Límite excedido')

            return False

        return True



    def retirar(self, monto_solicitado):

        monto_dispensado = 0

        restante = monto_solicitado

        for denominacion, cantidad in self.billetes:

            if (denominacion * cantidad) > restante: 

                cantidad_billetes = math.floor( restante / denominacion )

                monto_dispensado += cantidad_billetes * denominacion

                restante = monto_solicitado - monto_dispensado

                if cantidad_billetes > 0:

                    self.detalles_retiro.append([denominacion, cantidad_billetes])

                    

            if monto_dispensado == monto_solicitado: break



        if restante > 0:

            print('Ah ocurrido un error al momento de retirar. Por favor, intente de nuevo')

            return; False

        self.reporteRetiro()

        self.dinero_disponible -= monto_solicitado

        self.cliente.saldo -= monto_solicitado

        return True