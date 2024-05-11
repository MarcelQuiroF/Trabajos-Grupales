def ConversionVolumen(PrimerNumero, Unidad):
    Mililitro = 1
    Litro = 1000
    Galon = 3785411.784
    MetroCubico = 1000000
    
    PrimerConversion = 0
    SegundaConversion = PrimerNumero / Litro
    TerceraConversion = PrimerNumero / Galon
    CuartaConversion = PrimerNumero / MetroCubico
    
    if Unidad.lower() == "ml":
        PrimerConversion = PrimerNumero * Mililitro
    elif Unidad.lower() == "l":
        PrimerConversion = PrimerNumero * Litro
    elif Unidad.lower() == "gal":
        PrimerConversion = PrimerNumero * Galon
    elif Unidad.lower() == "m3":
        PrimerConversion = PrimerNumero * MetroCubico
    else:
        print("No coinciden las unidades de medida proporcionadas con el tipo de magnitud seleccionada")
    
    print("Las conversiones son:")
    print(PrimerConversion, "ml")
    print(SegundaConversion, "L")
    print(TerceraConversion, "gal")
    print(CuartaConversion, "m3")

def ConversionDistancia(PrimerNumero, Unidad):
    Metro = 1
    Kilometro = 1000
    Centimetro = 0.01
    Milimetro = 0.001
    Pie = 0.3048
    
    PrimerConversion = 0
    SegundaConversion = PrimerNumero / Kilometro
    TerceraConversion = PrimerNumero / Centimetro
    CuartaConversion = PrimerNumero / Milimetro
    QuintaConversion = PrimerNumero / Pie
    
    if Unidad.lower() == "m":
        PrimerConversion = PrimerNumero * Metro
    elif Unidad.lower() == "km":
        PrimerConversion = PrimerNumero * Kilometro
    elif Unidad.lower() == "cm":
        PrimerConversion = PrimerNumero * Centimetro
    elif Unidad.lower() == "mm":
        PrimerConversion = PrimerNumero * Milimetro
    elif Unidad.lower() == "ft" or Unidad.lower() == "pies" or Unidad.lower() == "pie":
        PrimerConversion = PrimerNumero * Pie
    else:
        print("No coinciden las unidades de medida proporcionadas con el tipo de magnitud seleccionada")
    
    print("Las conversiones son:")
    print(PrimerConversion, "m")
    print(SegundaConversion, "km")
    print(TerceraConversion, "cm")
    print(CuartaConversion, "mm")
    print(QuintaConversion, "pies")

def ConversionMasa(PrimerNumero, Unidad):
    Tonelada = 1000000
    Libra = 453.592
    Arroba = 11500
    Kilogramo = 1000
    Gramo = 1
    
    PrimerConversion = 0
    SegundaConversion = PrimerNumero / Arroba
    TerceraConversion = PrimerNumero / Kilogramo
    CuartaConversion = PrimerNumero / Libra
    QuintaConversion = PrimerNumero / Tonelada
    
    if Unidad.lower() == "g":
        PrimerConversion = PrimerNumero * Gramo
    elif Unidad.lower() == "kg":
        PrimerConversion = PrimerNumero * Kilogramo
    elif Unidad == "@":
        PrimerConversion = PrimerNumero * Arroba
    elif Unidad.lower() == "lb":
        PrimerConversion = PrimerNumero * Libra
    elif Unidad.lower() == "t":
        PrimerConversion = PrimerNumero * Tonelada
    else:
        print("No coinciden las unidades de medida proporcionadas con el tipo de magnitud seleccionada")
    
    print("Las conversiones son:")
    print(PrimerConversion, "g")
    print(SegundaConversion, "@")
    print(TerceraConversion, "kg")
    print(CuartaConversion, "lb")
    print(QuintaConversion, "t")

def Primeringo():
    PrimerNumero = float(input("Escribe su cantidad: "))
    return PrimerNumero

def numeroaRadicar():
    NumeroaRadicar = float(input("Escribe el número a radicar"))
    return NumeroaRadicar

def numeroIndice():
    NumeroIndice = float(input("Escribe el número que será su índice"))
    return NumeroIndice

def CantidadTipo():
    Unidad = input("Escribe su magnitud Ej: g, mg, ml, Km: ")
    return Unidad

def CalculadoraMassay():
    print("Escribe el modo de que función de la calculadora necesitas")
    print("1. Operaciones básicas (+, -, x, /)")
    print("2. Potenciación")
    print("3. Porcentaje")
    print("4. Conversiones (Masa, Volumen, Distancia)")
    print("5. Radicaciones")
    seleccion = int(input())
    
    if seleccion == 1:
        PrimerNumero = Primeringo()
        Signo = input("Escribe el signo de la operación (+, -, x, /): ")
        SegundoNumero = Primeringo()
        if Signo == "+":
            RespuestaNumero = PrimerNumero + SegundoNumero
        elif Signo == "-":
            RespuestaNumero = PrimerNumero - SegundoNumero
        elif Signo == "x":
            RespuestaNumero = PrimerNumero * SegundoNumero
        elif Signo == "/":
            RespuestaNumero = PrimerNumero / SegundoNumero
        print(RespuestaNumero)
    
    elif seleccion == 2:
        PrimerNumero = Primeringo()
        SegundoNumero = Primeringo()
        RespuestaNumero = PrimerNumero ** SegundoNumero
        print(RespuestaNumero)
    
    elif seleccion == 3:
        print("Escoja la letra de la opción de ejercicio de porcentaje")
        print("A. Calcular el porcentaje de una cantidad dada")
        print("B. Calcular el total conociendo el porcentaje")
        print("C. Calcular qué porcentaje del total es una cantidad")
        SegundaEleccion = input()
        if SegundaEleccion.lower() == "a":
            PrimerNumero = Primeringo()
            SegundoNumero = Primeringo()
            RespuestaNumero = PrimerNumero * SegundoNumero / 100
            print(f"El {SegundoNumero}% de {PrimerNumero} es {RespuestaNumero}")
        elif SegundaEleccion.lower() == "b":
            PrimerNumero = Primeringo()
            SegundoNumero = Primeringo()
            RespuestaNumero = SegundoNumero * 100 / PrimerNumero
            print(f"Si {PrimerNumero}% es {SegundoNumero}, el total es {RespuestaNumero}")
        elif SegundaEleccion.lower() == "c":
            PrimerNumero = Primeringo()
            SegundoNumero = Primeringo()
            RespuestaNumero = SegundoNumero * 100 / PrimerNumero
            print(f"{SegundoNumero} es el {RespuestaNumero}% de {PrimerNumero}")
    
    elif seleccion == 4:
        print("Escribe la letra de la opción")
        print("A. Transformar unidades de masa (g, @, kg, lb, t)")
        print("B. Transformar unidades de distancia (m, km, cm, mm, ft/pies)")
        print("C. Transformar unidades de volumen (ml, l, gal, m3)")
        SegundaEleccion = input()
        Unidad = CantidadTipo()
        PrimerNumero = Primeringo()
        if SegundaEleccion.lower() == "a":
            ConversionMasa(PrimerNumero, Unidad)
        elif SegundaEleccion.lower() == "b":
            ConversionDistancia(PrimerNumero, Unidad)
        elif SegundaEleccion.lower() == "c":
            ConversionVolumen(PrimerNumero, Unidad)
    
    elif seleccion == 5:
        PrimerNumero = numeroaRadicar()
        SegundoNumero = numeroIndice()
        RespuestaNumero = PrimerNumero ** (1 / SegundoNumero)
        print(f"La radicación de índice {SegundoNumero} de {PrimerNumero} es {RespuestaNumero}")

CalculadoraMassay()
