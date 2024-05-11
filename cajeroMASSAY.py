def ConfirmarTransferenciaIngles(Dinero, NombreDeCuenta, Moneda, NumeroDeCuenta, Multiplicador, Saldo):
    Confirmacion=input((f"""Confirm transfer details
Account:          {NumeroDeCuenta}
Username:         {NombreDeCuenta}
Money:            {Dinero} {Moneda}
Is the data correct? (Yes/No)
""")).upper()
    if Confirmacion == "YES":
        Monto = Dinero * Multiplicador
        RetiroIngles(Saldo, Monto)
    else:
        print("The transaction has been canceled")

def ConfirmarTransferencia(Dinero, NombreDeCuenta, Moneda, NumeroDeCuenta, Multiplicador, Saldo):
    Confirmacion=input((f"""Confirme los datos de la transferencia
Cuenta destinada:   {NumeroDeCuenta}
Usuario:            {NombreDeCuenta}
Dinero:             {Dinero} {Moneda}
Los datos son correctos? (Si/No)
""")).upper()
    if Confirmacion == "SI":
        Monto = Dinero * Multiplicador
        Retiro(Saldo, Monto)
    else:
        print("Se ha cancelado la transaccion")
    
def TransferenciaIngles(Moneda, Multiplicador, Saldo):
    NumeroDeCuenta = input("""Enter the account number
""")
    NombreDeCuenta = input("""Enter the name
""")
    Dinero = int(input(f"""Enter the amount in {Moneda}
"""))
    ConfirmarTransferenciaIngles(Dinero, NombreDeCuenta, Moneda, NumeroDeCuenta, Multiplicador, Saldo)
    
def Transferencia(Moneda, Multiplicador, Saldo):
    NumeroDeCuenta = input("""Ingrese el numero de cuenta
""")
    NombreDeCuenta = input("""Ingrese el nombre del usuario
""")
    Dinero = int(input(f"""Ingrese el monto en {Moneda}
"""))
    ConfirmarTransferencia(Dinero, NombreDeCuenta, Moneda, NumeroDeCuenta, Multiplicador, Saldo)

def TipoDeTransaccionIngles(SubOpcionDeposito, TipoMoneda, Saldo):
    if TipoMoneda == "1":
        Moneda = "Bolivians"
        Multiplicador = 1
    elif TipoMoneda == "2":
        Moneda = "Dollars"
        Multiplicador = 7
    TransferenciaIngles(Moneda, Multiplicador, Saldo)

def TipoDeTransaccion(SubOpcionDeposito, TipoMoneda, Saldo):
    if TipoMoneda == "1":
        Moneda = "Bolivianos"
        Multiplicador = 1
    elif TipoMoneda == "2":
        Moneda = "Dolares"
        Multiplicador = 7
    Transferencia(Moneda, Multiplicador, Saldo)
    


def Retiro(Saldo, Monto):
    SaldoNuevo = max(Saldo - Monto, 0)
    if SaldoNuevo == 0:
        print(f"El saldo en la cuenta no es suficiente, cuentas con {Saldo}Bs")
    else:
        print(f"Has retirado/transferido {Monto}Bs, tu saldo actual es {SaldoNuevo}Bs")
        
def RetiroIngles(Saldo, Monto):
    SaldoNuevo = max(Saldo - Monto, 0)
    if SaldoNuevo == 0:
        print(f"The balance in the account is not enough, you have {Saldo}Bs")
    else:
        print(f"You have withdrawn/transferred {Monto}Bs, your current balance is {SaldoNuevo}Bs")

import random

RetiroRapido = {
    (1,100): 100,
    (2,250): 250,
    (3,500): 500,
    (4,700): 700}


Idioma=input("""Escoje tu idioma // Choose your lenguaje
A.Ingles
B.Español
""").upper()
if Idioma == "B":
    ExistenciaTarjeta=input("""Cuentas con la tarjeta? (Si/No)
""").upper()
    if ExistenciaTarjeta == "SI":
        print("""Ingresa la tarjeta....

Ingresa el pin de la tarjeta...""")        
        PIN = random.randint(0,1000)
        Acceso = 1
    else:
        Correo = input("""Escribe tu corre electronico
""")
        print = ("Introduce el pin que llego a tu correo...")
        PINcorreo = random.randint(0,1000)
        Acceso = 1
    if Acceso == 1:
        Saldo = int(random.randint(0,10000))
        Opcion=int(input("""Elige una de las siguientes opciones
1. Retiro rápido (100-700)
2. Retiro
3. Servicios
4. Cambio de pin
5. Consulta de saldo
6. Extracto
7. Deposito
"""))
        if Opcion == 1:
            SubOpcion1=int(input("""Seleccione la opcion
1. 100Bs
2. 250Bs
3. 500Bs
4. 700Bs
"""))
            for Rango, Exigencia in RetiroRapido.items():
                if Rango[0] == SubOpcion1  or  Rango[1] == SubOpcion1:
                    Monto = int(Exigencia)
                    break
            Respuesta = Retiro(Saldo, Monto)
        elif Opcion == 2:
            Monto = int(input("""Escribe la cantidad a retirar:
"""))
            Respuesta = Retiro(Saldo, Monto)
        elif Opcion == 3:
            Servicio=input("""Escoja el servicio a pagar:
A. Agua
B. Luz
C. Internet
""")
            Monto = random.randint(100,1000)
            Pago = input(f"""El monto a pagar es {Monto}Bs
Desea pagarlo? (Si/No)
""").upper()
            if Pago == "SI":
                Respuesta = Retiro(Saldo, Monto)
            else:
                print("No se realizo el pago")
        elif Opcion == 4:
            PinActual = int(input("""Ingrese el pin actual
"""))
            NuevoPin = int(input("""Ingrese el nuevo pin
"""))
            ConfirmacionPin = int(input("""Ingrese nuevamente el nuevo pin
"""))
            if NuevoPin == ConfirmacionPin:
                print("Se cambio correctamente el pin")
            else:
                print("Error, el pin no coincide")
        elif Opcion == 5:
            print(f"Tu saldo es: {Saldo}Bs")
        elif Opcion == 6:
            print("Retire su extracto")
        elif Opcion ==7:
            SubOpcionDeposito = input("""Seleccione el tipo de deposito
A. Cuenta propia
B. Cuenta de terceros
C. Otros bancos
""").upper()
            if SubOpcionDeposito == "A":
                TipoMoneda = input("""Selecciona el tipo de moneda
1. Bolivianos
2. Dolares
""")
                TipoDeTransaccion(SubOpcionDeposito, TipoMoneda, Saldo)
            elif SubOpcionDeposito == "B":
                TipoMoneda = input("""Selecciona el tipo de moneda
1. Bolivianos
2. Dolares
""")
                TipoDeTransaccion(SubOpcionDeposito, TipoMoneda, Saldo)
            elif SubOpcionDeposito == "C":
                Banco=input("""Selecciona el banco:
1. BCR
2. BGA
3. BIE
4. BIS
5. BME
6. BNB
""")
                TipoMoneda = input("""Selecciona el tipo de moneda
1. Bolivianos
2. Dolares
""")
                TipoDeTransaccion(SubOpcionDeposito, TipoMoneda, Saldo)
                
                
elif Idioma == "A":
    ExistenciaTarjeta=input("""Do you have your card? (Yes/No)
""").upper()
    if ExistenciaTarjeta == "YES":
        print("""Enter the card....

Enter the card pin...""")        
        PIN = random.randint(0,1000)
        Acceso = 1
    else:
        Correo = input("""Write your email
""")
        print = ("Enter the pin that arrived in your email...")
        PINcorreo = random.randint(0,1000)
        Acceso = 1
    if Acceso == 1:
        Saldo = int(random.randint(0,10000))
        Opcion=int(input("""Choose one number of the following options
1. Quick withdrawal (100-700) Bs
2. Withdrawal
3. Services
4. Change of pin
5. Balance inquiry
6. Extract
7. Deposit
"""))
        if Opcion == 1:
            SubOpcion1=int(input("""Select the option
1. 100Bs
2. 250Bs
3. 500Bs
4. 700Bs
"""))
            for Rango, Exigencia in RetiroRapido.items():
                if Rango[0] == SubOpcion1  or  Rango[1] == SubOpcion1:
                    Monto = int(Exigencia)
                    break
            Respuesta = RetiroIngles(Saldo, Monto)
        elif Opcion == 2:
            Monto = int(input("""Enter the amount of money to withdraw (on Bs):
"""))
            Respuesta = RetiroIngles(Saldo, Monto)
        elif Opcion == 3:
            Servicio=input("""Choose the service to pay:
A. Water
B. Light
C. Internet
""")
            Monto = random.randint(100,1000)
            Pago = input(f"""The amount to pay is {Monto}Bs
Do you want to pay it? (Yes/No)
""").upper()
            if Pago == "YES":
                Respuesta = RetiroIngles(Saldo, Monto)
            else:
                print("Payment was not made")
        elif Opcion == 4:
            PinActual = int(input("""Enter current pin
"""))
            NuevoPin = int(input("""Enter the new pin
"""))
            ConfirmacionPin = int(input("""Re-enter the new pin
"""))
            if NuevoPin == ConfirmacionPin:
                print("Your pin was changed successfully")
            else:
                print("Error, pin does not match")
        elif Opcion == 5:
            print(f"Your balance is: {Saldo}Bs")
        elif Opcion == 6:
            print("Withdraw your statement")
        elif Opcion == 7:
            SubOpcionDeposito = input("""Select the type of account
A. Own account
B. Third-party account
C. Other banks
""").upper()
            if SubOpcionDeposito == "A":
                TipoMoneda = input("""Select the type of the transaction
1. Bolivians
2. Dollars
""")
                TipoDeTransaccionIngles(SubOpcionDeposito, TipoMoneda, Saldo)
            elif SubOpcionDeposito == "B":
                TipoMoneda = input("""Select the type of the transaction
1. Bolivians
2. Dollars
""")
                TipoDeTransaccionIngles(SubOpcionDeposito, TipoMoneda, Saldo)
            elif SubOpcionDeposito == "C":
                Banco=input("""Choose the bank:
1. BCR
2. BGA
3. BIE
4. BIS
5. BME
6. BNB
""")
                TipoMoneda = input("""Select the type of the transaction
1. Bolivians
2. Dollars
""")
                TipoDeTransaccionIngles(SubOpcionDeposito, TipoMoneda, Saldo)
            
