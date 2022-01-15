### NOMBRE: DANIEL FELICIANO SANTILLAN ALFONSO
### DEBER 2
### CURSO: 3ER SEMESTRE-SOFTWARE-MAÑANA

import os
##############! video 1

### Ejercicio 1
print("""¡Caminante! En esta tumba yacen los restos 
de Diofanto, al terminar de leer este texto podrás 
saber la duración de su vida.
Su infancia ocupó la sexta parte de su vida.
Después transcurrió una doceava parte de su vida 
hasta que su mejilla se cubrió de vello.
A partir de ahí, pasó la séptima parte de su existencia 
hasta contraer matrimonio.
Pasó un quinquenio y le hizo dichoso el nacimiento 
de su primogénito.
Su hijo murió al alcanzar la mitad de los años que su 
padre llegó a vivir.
Tras cuatro años de profunda pena por la muerte 
de su hijo, Diofanto murió.
Dime, caminante, cuántos años vivió Diofanto.\n""")
# # 1/6(x) + 1/12(x) + 1/7(x) + 5 + 1/2(x) + 4 = x   =>84años
class Años_Diofanto:
    def cuanto_vivio(self):
        from fractions import Fraction
        print("¿Cuántos años vivió Diofanto?")  
        x=1
        a=Fraction (1,6) #(x)
        b=Fraction (1,12) #(x)
        c=Fraction (1,7) #(x)
        d=5
        e=Fraction (1,2) #(x)
        f=4

        paso1=a+b+c+e
        paso2=d+f
        denominador=paso1.denominator

        paso3= paso1*denominador
        paso4=paso2*denominador
        paso5=x*denominador

        paso6= paso5-paso3
        paso7= paso4/paso6

        print ("Diofanto vivió: {} años".format(paso7))
resultado1= Años_Diofanto()
resultado1.cuanto_vivio()
os.system('cls')




##############! video 2
## Ejercicio 1

# # ordenando la ropa 

# # las camisetas se deben ordenar en líneas horizontales segun las siguientes reglas:
# # * La camiseta que menos cículos tiene no debe quedar 
# # adyacente a la camiseta amarilla.
# # * Ninguna camiseta debe estar adyacente a otra que tenga el doble de círculos.
# # * la camiseta del extremo izquierdo tiene la mitad de círculos que la del extremo.
# # * en los extremos no puede haber una camiseta de color verde ni con círculos verdes.

## camisa verde- 5 circulos celeste :*:; camisa azul-8 círculos morados :::: ; camisa amarilla-4 círculos naranja °°°° ; camisa naranja-3 círculos verdes °+.
## print("Camiseta amarilla - Camiseta verde - camiseta naranja - camiseta azul.")

## Ejercicio 2

# # Verdadero ó false
print("""Indicá con V o F el valor de cada una de las siguientes proposiciones:
1. Todas las flechas de color aputan en la misma dirección.
2. Ningún rombo es de color rojo.
3. No todos los círculos tienen borde punteado.
4. Algunos cuadrados tienen borde de color azul.
5. No todas las lunas están rellenas de color verde.
6. Ningún cuadrado es de color rosado.
7. Algunas flecas que apuntan hacia abajo están rellenas de color violeta.
8. Todas las lunas tienen borde de color rojo.
9. Todas las figuras rellenas de color violeta son flechas.
10. No todas las flechas que aputan hacia arriba están rellenas de color rojo.
11. Algunas figuras de borde punteado con circulos.
12. No todos los cuadrados están rellenos con color.
13. Todas las figuras rellenas de color amarillo son rombos.\n
Respuesta:
1. V    2. V    3. V     4. F
5. F    6. V    7. V     8. F
9. V    10. F   11. V    12. V
13. F\n""")
os.system('cls')

## Ejercicio 3

## 1) RQP, ONM, LKJ,___, FED
##! a) IHG
## b) CAB
## c) JKL
## d) GHI
## Explicación: las letras siguen el alfabeto en orden inverso

## 2) 104, 109, 115, 122, 130, ___
## a) 119
## b) 125
##! c) 139
## d) 134
## Explicación: 104+5=109, 109+6=115, 115+7=122, 122+8=130, 130+9=139

## 3) KBJ, LCK, MDL, NEM, ___
## a) OEP
##! b) OFN
## c) MEN
## d) PFQ
## Explicación: la letra del medio sigue la secuencia BCDEF. La primera y la última letras siguen el alfabeto en orden

## 4) 15, 31, 63, 127, 255, ___
## a) 110
## b) 170
##! c) 511
## d) 181
## Explicación: 15x2+1=31, 31x2+1=63, 63x2+1=127, 127x2+1=255, 255x2+1=511


## Ejercicio 4

## Intenta descubrir qué regla(s) se utilizaron para codificar en cada uno de los siguientes puntos:
## 1) Si en un mensaje codificado la palabra "RESOLUCION' se escribe como "PFQPJVAJNN", ¿cómo se 
##    escribiría la palabra "VERDE"?
## 2) Si CASA=52, MESA=93, FOCA=62, TIZA=85, entonces ROSA=?
## 3) En un cierto idioma, "dugo hui mul zo" significa "trabajar es muy difícil"; 
## "hui dugo ba ki significa "Bingo es muy inteligente","nano mul dugo" significa "cantar es difícil" 
## y "mulki gu" significa "inteligente y difícil". ¿Cómo se escribe la palabra "Bingo" en ese idioma? a) jalu; b) dugo; c) ki; d) ba

## Soluciones:

## 1)) Si en un mensaje codificado la palabra "RESOLUCIÓN se escribe como "PFQPJVAJNÑ", entonces "VERDE" se escribe "TFPEC" <- Respuesta. 
## Explicación: el mensaje se cifró siguiendo el patrón -2, +1, -2, +1, etc. usando el alfabeto español ABCDEFGHIJKLMNOPQRSTUVWXYZ.
## Por eso: V=T, E=F, R=P, D=E, E=C.

## 2)) Si CASA=52, MESA=93, FOCA=62, TIZA=85, entonces ROSA=65 <- respiuesta. 
## Explicación: se suman las posiciones del alfabeto español y luego se invierte el número 19+16+20+1=56 
## A B C D E F G H I J  K  L  M  N  Ñ  O  P  Q  R  S  T  U  V  W  X  Y  Z
## 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27

## 3)) "dugo hui mul zo": "trabajar es muy difícil" 
## "hui dugo ba ki": "Bingo es muy inteligente" 
## "nano mul dugo":"cantar es difícil" 
## "mulki gu": "inteligente y dificil". 
## ¿Cómo se escribe la palabra "Bingo" en ese idioma? "ba" <-respuesta. 
## Explicación: la palabra "Bingo" sólo aparece en la segunda 
## oración. La palabra "ba" es la única de la segunda oración que no se repite en ninguna otra.


## Ejercicio 5

# # Para cada concepto dado, ¿cuál de las opciones es necesaria para él?
# # 1) DESIERTO 
# # a) árido; b) montaña; c) oasis; d) cactus

# # 2) IDIOMA 
# # a) escritura; b) jerga; c) palabras; d) voz
 
# # 3) MONOPOLIO 
# # a) internacional; b) éxito; c) corrupto; d) exclusivo
 
# # 4) RELÁMPAGO 
# # a) electricidad; b) lluvia; c) trueno; d) luminosidad

# # Soluciones
# # 1) DESIERTO - "árido" <-respuesta.
# # Explicación: un desierto es un territorio árido. No todos los 
# # desiertos tienen montañas y no necesariamente hay cactus ni oasis

# # 2) IDIOMA - "palabras" <-respuesta. 
# # Explicación: las palabras son una parte indispensable de un idioma. 
# # La escritura y la jerga no son necesarias para que exista un idioma. 
# # No todos los idiomas son escritos ni hablados mediante la voz.

# # 3) MONOPOLIO - "exclusivo" <-respuesta.
# # Explicación: lo esencial de un monopolio es la exclusividad de quien 
# # lo controla. No necesariamente será internacional, ni exitoso, 
# # ni estará involucrado en actos de corrupción.

# # 4) RELÁMPAGO - "electricidad" <-respuesta.
# # Explicación: los relámpagos son descargas eléctricas, por lo que 
# # la electricidad es indispensable. La lluvia o los truenos no son 
# # esenciales para la ocurrencia de relámpagos. La luminosidad puede 
# # ser un efecto de los relámpagos pero no es esencial.


## Ejercicio 6

## La limpieza del hogar

# # Cinco personas viven juntas: Lucas, Cintia, Luis, Ema y Vero. Se dividen las tareas domésticas para que 
# # cada uno sólo haga una tarea en un único dia a la semana (del lunes al viernes): baldear, barrer, lavar la 
# # ropa, comprar viveres, ordenar.
# # → Luis no compra viveres y no hace su tarea el martes. 
# # → Cintia ordena y no lo hace ni el lunes ni el viernes. 
# # → Baldearse hace el jueves. 
# # → Vero hace su tarea los miércoles y no es comprar viveres. 
# # → La ropa se lava el viernes y no lo hace Ema. 
# # → Lucas hace su tarea los lunes.

# # 1) ¿Qué tarea hace Vero los miércoles?
# # 2) ¿Qué tarea hace Luis? 
# # 3) ¿Qué dia hace su tarea Ema?
# # 4) ¿Cuándo se encarga Cintia de ordenar? 
# # 5) ¿Qué dia se compran viveres?

# # Soluciones

# # 1) ¿Qué tarea hace Vero los miércoles? "Barrer" <-respuesta. 
# # Explicación: Vero no ordena, baldea, lava la ropa ni compra viveres. La que resta es barrer. 

# # 2) ¿Qué tarea hace Luis ? "Lavar la ropa" <-respuesta.
# # Explicación: Luis no compra viveres, ordena ni barre. Quedan lavar la ropa y baldear. 
# # Como Ema no lava la ropa, entonces ella debe baldear y Luis lavar la ropa.

# # 3) ¿Qué dia hace sus tareas Ema? "Jueves" <-respuesta. 
# # Explicación: Ema baldea, y eso se hace los jueves.

# # 4) ¿Cuándo se encarga Cintia de ordenar? "Martes" <-respuesta. 
# # Explicación: se ordena los martes, miércoles o jueves. Pero los jueves se 
# # baldea y Vero hace su tarea los miércoles, entonces Cintia ordena los martes.

# # 5) ¿Qué dia se compran los viveres? "Lunes" <-respuesta. 
# # Explicación: se ordena los martes, se barre los miércoles, 
# # se baldea los jueves, se lava la ropa los viernes. Resta el lunes.

##############! video 3

## Explicacion sobre "Variables" que es un espacio en la memoria en el cual se puede guardar algun dato.
## a=15   #"a" guarda el valor de 15
## print(a)
## Se presenta por pantalla "15".

##############! video 4

## Sin usar el intérprete de Python, ¿Podría decir qué guarda la variable X en cada uno de los siguientes casos?
## 1
# X=46
# X=15
# x=30
# X guarda "15"

## 2
# X=10*2
# X-=5
# X guarda "15"

## 3
# X=10-2
# 10+2
# X guarda "8"

## 4
# Y=3*(4+2)
# X=Y+2
# Z=5
# X=Y-z
# X guarda 13

## 5
# X=25
# X+10
# X guarda 25

## 6
# X=3
# Y=x+6
# X=Y-1
# X guarda 8

##############! video 5

## Explica sobre los tipos de datos y operaciones.

## tipos de datos 
## 12, -321, 34.36, enteros (int), decimal(float)
## "hola","", cadena de caracteres (str)
## True, False, booleanos(bool)
## para conocer el dato se usa "type",ejemplo:
## x=150
## print(type (x))

## operaciones aritméticas:
## suma= +, resta=-, multiplicación= *, divición=/, divición entera= //, resto de división=%, potencia=**

## operaciones con strings:
## concatenas= +, carácter en determinado índice=[], longitud de cadena=len()

## operaciones de comparación:
## mayor= >, menor= <, mayor o igual= >=, menor o igual= <=, igual ==, distinto= !=

## operaciones lógicas:
## conjunción("y")= and, disyunción("o")= or, negación("no")= not

##############! video 6
class Video6_ejercicio1:
    def vide6_ejer(self):
        # # #? ¿De qué tipo es cada uno de los siguientes datos?
        print("""¿De qué tipo es cada uno de los siguientes datos?
• 100/5
• 7/2
• 7//2
• 7%2
• 'a'
• "tiza"+"."
• "hola"[1+1]
• len("hola")")
• int("145")
• float("145")
• float(145)
• str(32)
• 1+2 != 3 
• 177%2==0 
• len("nube")<=20

Respuesta: """)
        # # # • 100/5 
        # # # Respuesta: float
        a=100/5
        print(type(a))

        # # # • 7/2
        # # # Respuesta:  float
        b=7/2
        print(type(b))

        # # # • 7//2 
        # # # Respuesta: int
        c=7//2
        print(type(c))

        # # # • 7%2 
        # # # Respuesta: int
        d=7%2
        print(type(d))

        # # # • 'a' 
        # # # Respuesta: str
        e='a'
        print(type(e))

        # # # • "tiza"+"." 
        # # # Respuesta: str
        f="tiza"+"."
        print(type(f))

        # # # • "hola"[1+1] 
        # # # Respuesta: str
        g="hola"[1+1]
        print(type(g))

        # # # • len("hola")
        # # # Respuesta: int
        h=len("hola")
        print(type(h))

        # # # • int("145") 
        # # # Respuesta: int
        i=int("145")
        print(type(i))

        # # # • float("145") 
        # # # Respuesta: float
        j=float("145")
        print(type(j))

        # # # • float(145) 
        # # # Respuesta: float
        k=float(145)
        print(type(k))

        # # # • str(32) 
        # # # Respuesta: str
        l=str(32)
        print(type(l))

        # # # • 1+2 != 3 
        # # # Respuesta: bool
        n=1+2 != 3
        print(type(n))

        # # # • 177%2==0 
        # # # Respuesta: bool
        m=177%2==0
        print(type(m))

        # # # • len("nube")<=20
        # # # Respuesta: bool
        o=len("nube")<=20
        print(type(o))
resul6_1=Video6_ejercicio1()
resul6_1.vide6_ejer()
os.system('cls')



class Video6_ejercicio2:
    def vide6_ejer2(self):

        # # #? ¿Qué guardan las variables luego de cada operación?
        print("""¿Qué guardan las variables luego de cada operación?
• n=167/10
• n=167//10
• n=167%10
• letra='a'
• saludo="hola"+letra 
• C=saludo[0]
• C=saludo [1+3]
• L=len( saludo)
• C=saludo [len( saludo)-1]
• menor="a"<"b"
• D=1!=1 
• D="cinta" >="canto"
• C="z"+"a"+"paz"[0]
• X=C[0] =="Z"
""")
        # # # • n=167/10 
        # # # Respuesta: 16.7
        n=167/10
        print(n)

        # # # • n=167//10 
        # # # Respuesta: 16
        n=167//10 
        print(n)

        # # # • n=167%10 
        # # # Respuesta: 7
        n=167%10  
        print(n)

        # # # • letra='a' 
        # # # Respuesta: a
        letra='a' 
        print(letra)

        # # # • saludo="hola"+letra 
        # # # Respuesta: holaa
        saludo="hola"+letra
        print(saludo)

        # # # • C=saludo[0] 
        # # # Respuesta: h
        C=saludo[0] 
        print(C)

        # # # • C=saludo [1+3]
        # # # Respuesta: a
        C=saludo [1+3]
        print(C)

        # # # • L=len( saludo) 
        # # # Respuesta: 5
        L=len( saludo) 
        print(L)

        # # # • C=saludo [len( saludo)-1] 
        # # # Respuesta: a
        C=saludo [len( saludo)-1] 
        print(C)

        # # # • menor="a"<"b" 
        # # # Respuesta: True
        menor="a"<"b" 
        print(menor)

        # # # • D=1!=1 
        # # # Respuesta: False
        D=1!=1 
        print(D)
        # # # • D="cinta" >="canto" 
        # # # Respuesta: True
        D="cinta" >="canto" 
        print(D)

        # # # • C="z"+"a"+"paz"[0] 
        # # # Respuesta: zap
        C="z"+"a"+"paz"[0] 
        print(C)
        # # # • X=C[0] =="Z"
        # # # Respuesta: False
        X=C[0] =="Z"
        print(X)
resul6_2=Video6_ejercicio2()
resul6_2.vide6_ejer2()
os.system('cls')



### Ejercicio 3
# #? ¿Cuáles de las siguientes operaciones arrojan error?

# # • 11-(4%2+10) 
# # Respuesta: 1

# # • "30"+2 
# # Respuesta: error

# # • "30"+"2" 
# # Respuesta: 302

# # • "hola"[len("hola")] 
# # Respuesta: error

# # • len(124) 
# # Respuesta: error

# # • "hola"[len("fin")] 
# # Respuesta: a

# # • "hola" [11-(4%2+10)]
# # Respuesta: o

# # • int("4") 
# # Respuesta: 4

# # • int(4) 
# # Respuesta: 4

# # • int("z") 
# # Respuesta: error

# # • int("4.") 
# # Respuesta: error

# # • 4<"f" 
# # Respuesta: error

# # • "palabra"="rama" 
# # Respuesta: error

# # • "palabra"=="rama"
# # Respuesta: False


##############! video 7

## Explica sobre "Tablas de verdad"
## conjunción("y")= and, disyunción("o")= or, negación("no")= not
class Video7_ejercicio1:
    def vide7_ejer1(self):

        print("Conjunción")
        edad=16
        cliente=True
        a=edad>10 and edad<20
        print(a)
        aa=cliente and edad>18
        print(aa)

        print("Disyunción")
        b=edad>20 or edad<30
        print(b)

        print("Negación")
        c=not cliente
        print(c)
resul7_1=Video7_ejercicio1()
resul7_1.vide7_ejer1()
os.system('cls')



##############! video 8
class Video8_ejercicio1:
    def vide8_ejer1(self):
        ## Ejercicio 1
        print("¿Qué resultado (True/False) dan las siguientes operaciones?")
        a=not True
        print(a)

        a=not(1+2!=3)
        print(a)

        X=(len("jugar") >5) and (len("jugar") <10)
        print(X)

        a="alto" [2]=="t" and X 
        print(a)

        a=842913%10!=3 and len("café")==3
        print(a)

        a=0!=0 or "a"<"y"
        print(a)

        a=True or int("50")>=50 
        print(a)

        edad=20 
        a=not(X) or edad%2==0 
        print(a)

        es_cliente=False 
        a=not (es_cliente and not(edad<18))
        print(a)
resul8_1=Video8_ejercicio1()
resul8_1.vide8_ejer1()
os.system('cls')




class Video8_ejercicio2:
    def vide8_ejer2(self):
    ## Ejercicio 2
        print("¿Qué errores tienen estas proposiciones? ¿Cómo deben corregirse? \n")
        print("""1) El número no puede ser menor que o ni mayor que 100:
número<0 and número> 100""")
        print("Respuesta: número>=0 and número<=100\n")

        print("""2) La edad debe estar entre 10 y 20:
edad> 10 and <20""")
        print("Respuesta: edad>10 and edad<20\n")

        print("""3) La longitud de la cadena no debe ser superior a 10 caracteres
len(cadena)<10""")
        print("Respuesta: len(cadena)<=10")
resul8_2=Video8_ejercicio2()
resul8_2.vide8_ejer2()
os.system('cls')


class Video8_ejercicio3:
    def vide8_ejer3(self):
        ## Ejercicio 3
        print("""¿Cómo expresarías las siguientes operaciones? 
    Suponer la existencia de variables conteniendo los datos necesarios\n""")
        print("""1) El número es múltiplo de 4 y también es negativo.
    Respuesta: número%4==0 and número<0\n""")

        print("""2) Decidiste comprar un auto usado, pero debe cumplir ciertas condiciones: 
    El kilometraje debe ser menor a 30000 y el modelo debe estar entre 2015 y 2017
    Respuesta: km<30000 and (modelo>=2015 and modelo<=2017)\n""")

        print("""3) Una agrupación académica tiene ciertos requisitos para cualquier estudiante que desea ingresar: 
    Debe tener más del 30% de sus estudios completos y no debe ser miembro de otra agrupación académica en la misma universidad.
    Respuesta: porcentaje_completo>30 and not (miembro_agrupación)\n""")

        print("""4) Una persona pasa frio si es invierno y además no tiene calefacción ni está abrigada.
    Respuesta: 
    es_invierno and not tiene_calefacción and not esta_abrigada 
    es_invierno and not (tiene_calefacción or está abrigada)\n""")
resul8_3=Video8_ejercicio3()
resul8_3.vide8_ejer3()
os.system('cls')


##############! video 9
## Explica el manejo de strings

# # Concatenación: cadena1+cadena2 
# # Longitud: len (cadena) 
# # Caracter: cadena [0] ó rebanada: cadena [0:10] ó con paso: cadena [0:10:2] 
# # Dónde empieza una subcadena: cadena. find (subcadena) 
# # Inclusión (resultado booleano): cadena1 in cadena2 
# # Conversión de cadena numérica a tipo numérico: int (cadena) 
# # Conversión a mayúsculas: cadena.upper() o a minúsculas: cadena.lower() 
# # Eliminar espacios al principio y final: cadena.strip () 
# # Contar ocurrencias de subcadena: cadena.count (subcadena) 
# # Reemplazar subcadena: cadena.replace (subcadena_ant, subcadena nueva)



##############! video 10

class Video10_ejercicio1:
    def vide10_ejer1(self):
    ### Ejercicio 1
        print("Ejercicios de strings.")
        print("""¿Cuál es el resultado:?
cadena="si, profe, es cierto... yo me comi la tarea"
1) cadena[10]
2) cadena[-1]
3) cadena[0:9]
4) cadena[:3]
""")

        cadena="si, profe, es cierto... yo me comi la tarea"
        a=cadena[10]
        print("1) ",a)

        a=cadena[-1]
        print("2) ",a)

        a=cadena[0:9]
        print("3) ",a)

        a=cadena[::3]
        print("4) ",a)

        print("""\n¿Cómo obtener...?
1) La cadena al revés: (aerat al imoc em oy ...otreic se ,eforp ,is)
2) La subcadena (profe)
""")
        a=cadena[::-1]
        print("1) ",a)

        a=cadena[4:9]
        print("2) ",a)
resul10_1=Video10_ejercicio1()
resul10_1.vide10_ejer1()
os.system('cls')



class Video10_ejercicio2:
    def vide10_ejer2(self):

        print("""Dada la variable s="   hola, ¿cómo estás?" con 3 espacios 
al inicio, ¿qué se obtiene en cada una de las siguientes operaciones?
1) s[::-1] 
2) s[len (s)] 
3) s.count("o") 
4) s.count("Hola") 
5) s[-4:] 
6) s [15:] 
7) s.find("o")
8) s.strip () 
9) x=s.upper()
x==s
10) s[14:].upper() 
11) len(s) %2!=0 
12) s.replace(" ", "*") 
13) s.replace("z", "Z")\n""")
        print("Respuesta: ")
        s="   hola, ¿cómo estás?"
        a=s[::-1] 
        print("1) ",a)

        #a=s[len (s)] 
        print("2) Error")

        a=s.count("o") 
        print("3) ",a)

        a=s.count("Hola") 
        print("4) ",a)

        a=s[-4:] 
        print("5) ",a)

        a=s [15:] 
        print("6) ",a)

        a=s.find("o")
        print("7) ",a)

        a=s.strip () 
        print("8) ",a)

        x=s.upper()
        b=(x==s)
        print("9) ",b)

        a=s[14:].upper() 
        print("10) ",a)

        a=len(s) %2!=0 
        print("11) ",a)

        a=s.replace(" ", "*") 
        print("12) ",a)

        a=s.replace("z", "Z")
        print("13) ",a)
resul10_2=Video10_ejercicio2()
resul10_2.vide10_ejer2()
os.system('cls')


class Video10_ejercicio3:
    def vide10_ejer3(self):
        ### Ejercicio 3
        print("""Algunas preguntas...
1) Dada la variable X de tipo string ¿cómo se puede hallar el indice del último carácter? 
2) Dada la variable cadena="hola" ¿qué retorna cadena.find("2") ? 
3) ¿Qué retorna? "a" in "dátiles"
4) ¿Qué operación retorna la posición del primer espacio en "me gusta programar"? 
5) ¿Qué operación retorna la cantidad de espacios de la cadena "me gusta programar"? 
6) ¿Por qué da error? cadena[0]="H"
7) ¿Qué almacena la siguiente variable? nueva="C"+cadena[1:] 
8) ¿Cómo reemplazar las vocales acentuadas por vocales no acentuadas en la cadena X? 
9) ¿Qué comparación podría hacerse para averiguar si la longitud de la cadena es par? 
10) ¿De qué forma se puede obtener la cantidad de vocales de la cadena X?\n
Respuestas: """)
        x="programar en python"
        x=x[-1]
        print("1) ",x)

        cadena="hola"
        c=cadena.find("2")
        print("2) ",c)

        a="a" in "dátiles"
        print("3) ",a)

        r= "me gusta programar".find(" ")
        print("4) ",r)

        b= "me gusta programar".count(" ")
        print("5) ",b)

        #cadena[0]="H"
        print("6) Los strin no soportan la asignación porque los string son inmutables, no podemos cambiarlo pero si podemos reemplazar.")

        nueva="C"+cadena[1:]
        print("7) ",nueva)

        X_="hoy es día miércoles"
        X=X_.replace("í", "i").replace("é", "e")
        print("8) ",X)

        X= len(X_)
        if X%2 ==0:
            print("9) Par")
        else:
            print("9) Imprar")

        z=X_.count("a")+X_.count("e")+X_.count("i")+X_.count("o")+X_.count("u")
        print("10) ",z)
resul10_3=Video10_ejercicio3()
resul10_3.vide10_ejer3()
os.system('cls')


##############! video 11
## Ejercicio 1
## Explica "Entrada y salida de datos por pantalla"

## print: imprimir- "mostrar caracteres en la consola"
## input: leer- "tomar datos del teclaso"
## Ejemplo:
# # pri=18
# # print(pri)

# # inp=input("Ingrese edad: ")
# # print(inp)

##############! video 12

class Video12_ejercicio1:
    def vide12_ejer1(self):
    ### Ejercicio 1

        print("""Ejercicios de entrada y salida de datos.
¿Qué problemas tienen las siguientes instrucciones? ¿Cómo los solucionarías?
1) A=input(nombre, "¿cuál es tu canción favorita?")
2) precio=input("Precio:")
total=precio+(precio*0.10)
3) edad=int (input("Edad:")) 
print(tu edad es, edad)
4) edad=int(input("Edad:")) 
print("Veamos si tu edad es 18...", edad=18)\n""")

        print("""Respuesta:
1) input no puede incluir mas de una cosa a imprimir.
nombre=input("¿cuál es tu canción favorita?")
print(nombre)
2) "precio" es una cadena de caracteres "str".
precio=float(input("Precio: "))
total=precio+(precio*0.10)
3) Dentro del print quiere imprimir un str y el problema es que le falta las comillas.
edad=int(input("Edad: ")) 
print("tu edad es", edad)
4) En print lo que quiere es comparar pero lo que hace es una asignación.
edad=int(input("Edad:")) 
print("Veamos si tu edad es 18...", edad==18)""")
resul12_1=Video12_ejercicio1()
resul12_1.vide12_ejer1()
os.system('cls')


class Video12_ejercicio2:
    def vide12_ejer2(self):
        ### Ejercicio 2
        print("""Solicitar al usuario que ingrese su nombre. 
El nombre se debe almacenar en una variable llamada N. 
A continuación se debe mostrar en pantalla el texto "Ahora estás
en la matrix, [usuario]", donde "[usuario]" se reemplazará por 
el nombre que el usuario haya ingresado.\n""")

        N=input("Ingrese su nombre: ")
        print("Ahora estás en la matrix,",N)
resul12_2=Video12_ejercicio2()
resul12_2.vide12_ejer2()
os.system('cls')


class Video12_ejercicio3:
    def vide12_ejer3(self):
        ### Ejercicio 3
        print("""Hacer un programa que solicite al usuario cuánto costó una cena en 
un restaurante. A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina. 
Imprimir en pantalla el monto final a pagar.\n""")

        costo=float(input("Costo de la cena: $"))
        servicio=costo*0.062
        propina=costo*0.1
        print("Costo total de la comida: $",round(costo+servicio+propina,2))
resul12_3=Video12_ejercicio3()
resul12_3.vide12_ejer3()
os.system('cls')


class Video12_ejercicio4:
    def vide12_ejer4(self):
        ### Ejercicio 4
        print("""Solicitar al usuario que ingrese el día, mes y año de su nacimiento y 
almacenar cada uno de ellos en una variable numérica (en total, tres variables diferentes). 
Finalmente, mostrar la fecha en formato dd/mm/aaaa
Hacer otra versión del programa, pero esta vez almacenando todo en una única variable 
numérica, en la forma DDMMAAAA. ¿Y si la variable fuera de tipo string?\n""")
        print("Versión 1")
        dia=input("Día de tu nacimiento: ")
        mes=input("Mes de tu nacimiento: ")
        anio=input("Año de tu nacimiento: ")
        print(dia+"/"+mes+"/"+anio)
        ## vesión 2 
        # fecha=int(input("Fecha en formato DDMMAAA: "))
        # DD=fecha//1000000
        # MM=(fecha//10000)%100
        # AAA=fecha%10000
        # print(DD,"/",MM,"/",AAA)
        
        # # # 08121995%10=5 
        # # # 08121995%100=95 
        # # # 08121995%1000=995 
        # # # 08121995%10000=1995

        # # 081219951//10=812199 
        # # 081219951//100=81219 
        # # 081219951//1000-8121 
        # # 081219951//10000=812 
        # # 081219951//100000=81 
        # # 081219951//1000000=8

        print("\nVersión 2") #mejor
        ### si cambiamos la variable int a str nos daria error y no podriamos realizar esas operaciones, 
        ### entonces utilizariamos las rebanadas.
        fecha2=str(input("Fecha en formato DDMMAAA: "))
        DD=fecha2[:2]
        MM=fecha2[2:4]
        AAA=fecha2[4:]
        print(DD,"/",MM,"/",AAA)
resul12_4=Video12_ejercicio4()
resul12_4.vide12_ejer4()
os.system('cls')


class Video12_ejercicio5:
    def vide12_ejer5(self):
        ### Ejercicio 5
        print("""\nUna pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, 
para saber cuántos tanques de combustible consumirá el viaje entero.
Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, qué 
capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustible necesarios.\n""")

        capacidad=float(input("Capacidad del tanque (en litros): "))
        km_litro=float(input("Rendimiento (km por litro): "))
        recorrido=float(input("Km totales a recorrer: "))
        km_tanque=capacidad*km_litro
        print("Será necesario",round(recorrido/km_tanque,2),"tanques.")
resul12_5=Video12_ejercicio5()
resul12_5.vide12_ejer5()
os.system('cls')


##############! video 13

class Video13_ejercicio1:
    def vide13_ejer1(self):
        ### Ejercicio 1
        print("""\nUn empresario que se dedica al espectáculo necesita un programa que le ayude a hacer ciertos cálculos 
cada vez que organiza un concierto en un estadio deportivo. 
Lo primero que necesita saber es qué capacidad de público tendrá cada concierto, para saber cuántas entradas 
o boletos tienen que imprimirse. 
Para eso, cuando contrata un estadio deportivo, pregunta cuántos metros cuadrados tiene. El sabe que, por metro cuadrado, caben 4 
personas. También sabe que siempre hay un espacio con gradas y que normalmente estas ocupan un 20% de los metros cuadrados 
totales. En cada estadio las gradas pueden ser diferentes, asi que el empresario consulta cuánta gente cabe en ellas. 
Cuando contrata a la banda que dará el concierto, ésta le indica que porcentaje del espacio disponible necesitan ellos 
para montar su escenario. 
Con estos datos, debe calcularse cuánta gente va a caber en el estadio para un concierto determinado. El empresario, 
cada vez que use el programa, va a ingresar la cantidad de metros cuadrados que tiene el estadio que contrato, la cantidad 
de gente que cabe en las gradas y el porcentaje de espacio ocupado por el escenario. 
Luego, él quiere saber cuánto dinero ingresaria si vende todas las entradas disponibles, sabiendo que el 30% de 
las entradas vendidas serán a precio especial" y el resto son "a precio común". El empresario ingresa el precio 
de cada tipo de entrada cuando usa el programa\n.""")

    # # # datos del problema
    # # # Algunos datos son "fijos" o "constantes": el usuario ya sabe que no cambian. Estos son: 
    # # # • Que por metro cuadrado de espacio disponible caben 4 personas. 
    # # # • Que las gradas ocupan 20% del espacio total del estadio. 
    # # # • Que el 30% del total de entradas que venda van a ser a precio especial" y el resto (70%) van a ser a precio "común".

    # # # También hay datos que van a ir cambiando con cada ejecución del programa (dependiendo del estadio 
    # # # que consiga el empresario y la banda que contrate para dar el concierto): 
    # # # • La cantidad de metros cuadrados que mide el estadio. 
    # # # • El porcentaje de espacio que ocupa el escenario. 
    # # # • La cantidad de gente que cabe en las gradas.

        capaci_metro2=4
        porce_grada=0.2
        porce_especial=0.3
        porce_comunes=0.7

        dimensiones=float(input("Ingrese las dimensiones del estadio en m2: "))
        persona_grada=int(input("Ingrese la cantidad de personas que caben en las gradas: "))
        porce_escenario=int(input("Ingrese el porcentaje que ocupa el escenario: "))

        grada=dimensiones*porce_grada
        escenario=dimensiones*(porce_escenario/100)
        disponibles=dimensiones-grada-escenario
        total_persona=persona_grada+(disponibles*capaci_metro2)
        print("Caben {} personas.".format(round(total_persona,2)))

        precio_especial=float(input("Precio entrada especial: $"))
        precio_comun=float(input("Precio entrada común: $"))
        precio_total=(total_persona*porce_especial)*precio_especial+(total_persona*porce_comunes)*precio_comun
        print("Ingreso total de ventas es de: $", round(precio_total,2))
resul13_1=Video13_ejercicio1()
resul13_1.vide13_ejer1()
os.system('cls')


##############! video 14

### Ejercicio 1

### Bloque de código: es una o más instrucciones que tienen sentido juntas que están "agrupados", indicamos un bloue mediante la sangría o indentación.ejm:
### inicia un bloque:
###   cuerpo del bloque
###   inicia un bloque:
###       cuerpo del bloque

### condionales: if, va a tener una condición
### Permite tomar decisiones y van a estar basadas en una condición que no es más que un valor booleano(True/False).
### se puede realizar operaciones de comparar <,>=,==,!=, operaciones lógicas and, or, not.
### ejemplo:
### Ejemplo 1
### if (condición):
###     #hago algo

### Ejemplo 2
### if (condición):
###     #hago algo
### else:
###     #hago otra cosa
class Video14_ejercicio1:
    def vide14_ejer1(self):
        print("""\nCaso 1:
numero=int (input("N. de cliente:")) 
if numero==1000:
    print ("Ganaste un premio!")
o ¿Qué sucedería si la condición fuera 
if not numero==1000?

Respuesta:cuando ingrese 1000 no presentara nada y cuando ingrese cualquier otro número presentará el mensaje.""")

        numero=int (input("N. de cliente:")) 
        if numero==1000: #presentará el mensaje cuando el usuario ingrese 1000 caso contrario no presenta nada.
            print ("Ganaste un premio!")
        if not numero==1000: #cuando ingrese 1000 no presentara nada y cuando ingrese cualquier otro número presentará el mensaje.
            print ("Ganaste un premio!")

        print("""\nCaso2:
a=int (input ("Ingresa un número:")) 
b=int (input ("Ingresa un número:")) 
if a<b:
    print("el primero es menor") 
else:
    print("el segundo es menor")
o ¿Qué sucedería si el usuario ingresara
a=10 y b=10?

Respuesta: 10 es menor que 10, no, eso es falso por lo tanto imprime "el segundo es menor"_""")

        a=int (input ("Ingresa un número:")) 
        b=int (input ("Ingresa un número:")) 
        ### si a es menor imprimirá "el primero es menor"
        ### si a es mayor imprimirá "el segundo es menor"
        if a<b:
            print("el primero es menor") 
        else:
            print("el segundo es menor")
        ### Si el usuario ingresa a=10 y b=10 decimos:
        ### 10 es menor que 10, no, eso es falso por lo tanto imprime "el segundo es menor"



        print("\nSelección múltiple: if-elif-else")
        ### if (condición):  # blqoue 1
        ###     #hacer algo
        ### elif(condición):  # blqoue 2
        ###     #hacer algo
        ### else:             # blqoue 3
        ###     #hacer otra cosa

        # # # solo se ejecuta un bloque, no dos ni tampoco ninguno.
        # # # Si en el bloque 1 la condición es verdadero se ejecuta ese bloque, hace hago e ignora lo que esta acontinuación. 
        # # # Si el bloque 1 la condicion es falsa pasa a evaluar la sengunda condicion del bloque 2 y si es verdadera se ejecuta e ingora las otras.
        # # # Si el bloque 1 y 2 las condiciones son falsa se ejecuta el bloque 3 else 
        # # # Ejemplo: 
        a=int (input ("Un número:")) 
        b=int (input ("Otro número:")) 
        if a<b:
            print("El primero es menor") 
        elif b<a:
            print ("El segundo es menor") 
        else:
            print ("Son iguales")
resul14_1=Video14_ejercicio1()
resul14_1.vide14_ejer1()
os.system('cls')


##############! video 15

class Video15_ejercicio1:
    def vide15_ejer1(self):
        ### Ejercicio 1
        print("""\nEscribir un programa que, dado un número entero, muestre su valor absoluto.
Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), 
mientras que, para los negativos, su valor absoluto es el número multiplicado por - 1 (el valor absoluto de -52 es 52).\n""")

        numero= int(input("Ingrese un número: "))
        if numero<0:
            numero=numero*-1
        print("El número absoluto es: ", numero)



        ### Ejercicio 2
        print("""\nSolicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. 
A continuación, imprimir "coincidencia" si los nombres de ambas personas comienzan con la misma letra ó si 
terminan con la misma letra. Si no es así, imprimir "no hay coincidencia".\n""")

        nom1= input("Ingrese primer nombre: ")
        nom2= input("Ingrese segundo nombre: ")

        coin_nom1= len(nom1)-1
        coin_nom2= len(nom2)-1

        if nom1[0]==nom2[0] or nom1[coin_nom1]==nom2[coin_nom2]:
            print("Coincidencia.")
        else:
            print("No hay coincidencia")



        ### Ejercicio 3

        print("""\nCrear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: 
candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. 
Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje "Usted ha votado 
por el partido (color que corresponda al candidato elegido)". 
Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar "Opción errónea".\n""")

        candidato=input("Votar por A-B-C: ") 
        if candidato.upper()=="A":
            print("Usted ha votado por el partido rojo") 
        elif candidato.upper()=="B":
            print("Usted ha votado por el partido azul") 
        elif candidato.upper()=="C":
            print("Usted ha votado por el partido verde")
        else:
            print("opción errónea")



        ### Ejercicio 4
        print("""\nEscribir un programa que solicite al usuario una letra y si es una vocal, muestre el mensaje "es vocal". 
Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, 
informarle que no se puede procesar el dato.\n""")

        letra=input("Letra: ") 
        if len (letra)!=1:
            print("Debe ser sólo una letra.") 
        else:
            if letra.lower() in "aeiou":
                print("Es vocal.")


        ### Ejercicio 5
        print("""\nHacer un programa que permita saber si un año es bisiesto. 
Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible 
por 100, excepto que también sea divisible por 400.\n""")

        an=int(input ("Ingrese un año: ")) 
        if an%4!=0:
            print("No es bisiesto.") 
        else: 
            if an%100 !=0 or an%400==0: 
                print("Es bisiesto.")
            else:    
                print("No es bisiesto..")
resul15_1=Video15_ejercicio1()
resul15_1.vide15_ejer1()
os.system('cls')


##############! video 16

class Video16_ejercicio1:
    def vide16_ejer1(self):
        ### Ejercicio 1
        print("""\nUn instituto de enseñanza de inglés necesita un programa que le permita, cada día, procesar observaciones sobre las clases de ese 
día. El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases en un día de la semana diferente: los lunes se 
dicta el nivel inicial, los martes el nivel intermedio, los miércoles el nivel avanzado, los jueves son para práctica hablada y los viernes se dicta inglés para viajeros.

Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato "día, DD/MM", donde [día] es un día de la semana, DD es el 
número de día y MM es el número de mes. Si el usuario ingresa un día de la semana inexistente o una fecha cuyo día supere el número 31 o el 
mes supere el número 12, finalizar el programa indicando que se produjo un error. Debe permitirse que ingrese el día de la semana en minúsculas 
o mayúsculas indistintamente. Como precondición se tiene que lo ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.

Una vez indicada la fecha, el usuario necesita poder indicar si ese día se tomaron exámenes, pero eso sólo si se trata de los niveles inicial, 
intermedio o avanzado, ya que las prácticas habladas y el inglés para viajeros no tienen exámenes. Si hubo exámenes, el usuario ingresará 
cuántos alumnos aprobaron y cuántos no, y el programa le mostrará el porcentaje de aprobados.

Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el porcentaje de asistencia a clase y el programa le indicará 
"asistió la mayoría" en caso de que la asistencia sea mayor al 50% o "no asistió la mayoría" si no es así.

Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del mes 7, se deberá imprimir "Comienzo de nuevo ciclo" 
y solicitar al usuario que ingrese la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego imprimir el ingreso total en $.\n""")


        fecha=input("Ingrese la fecha en el siguiente formato ('día, DD/MM'): ")
        fecha=fecha.lower()
        diasemana=fecha[0:fecha.find(',')]
        dianro=int(fecha[fecha.find(',')+2:fecha.find('/')])
        mesnro=int(fecha[fecha.find('/')+1:])
        if dianro>31 or mesnro>12:
            print("Fecha incorrecta")
        else:
            if diasemana in "lunes,martes,miércoles":
                respuesta=input("¿Se tomaron exámenes? S/N: ")
                if respuesta.lower()=="s":
                    aprobados=int(input("Cantidad de aprobados: "))
                    reprobados=int(input("Cantidad de reprobados: "))
                    print("Porcentaje de aprobados:",round((aprobados*100)/(aprobados+reprobados),2), "%")
            elif diasemana=="jueves":
                asistencia=int(input("Porcentaje de asistencia: "))
                if asistencia>50:
                    print("Asistió la mayoría")
                else:
                    print("No asistió la mayoría")
            elif diasemana=="viernes":
                if dianro==1 and (mesnro==1 or mesnro==7):
                    print("Comienzo de nuevo ciclo")
                    alumnos=int(input("Cantidad de alumnos: "))
                    arancel=float(input("Arancel: $"))
                    print("Ingreso total: $",round(alumnos*arancel,2))
            else:
                print("Fecha incorrecta")
        print("Fin del programa")
resul16_1=Video16_ejercicio1()
resul16_1.vide16_ejer1()
os.system('cls')


##############! video 17
class Video17_ejercicio1:
    def vide17_ejer1(self):
        ### Ejercicio 1

        ### Repetición fija: for
        ### Permite repetir un bloque de código una cantidad fija de veces.
        ### Caundo termina la repetición del bloque, continúa el resto del programa.

        ### variable: variable iteradora
        ### a la variable iteradora podemos darle cualquier nombre, o incluso reutilizar una variable existente(cuidado: cambiará su valor)
        ### secuencia: string, range, listas...
        ### Ejemplo:
        ### for variable in secuencia:
        ###     #bloque a repetir
        ### 
        ### for x in "aeiou":  ##x: variable iteradora
        ###     print(x)       ##x va a guardar cada una de las vocales y va imprimir cada una de las vocales una sola vez.
        print("\nEjemplo 1: ")
        for x in "aeiou":
            print(x)

        print("\nEjemplo 2: ")
        for x in range(10):
            print(x)    

        print("\nEjemplo 3: ")
        for x in range(100,200):
            print(x)

        print("\nEjemplo 4: ")
        for x in range(5,20,3): #### imprime del 5 al 19 saltando de 3 en 3
            print(x)

        print("\nEjemplo 5: ")
        n=int(input("Ingrese un número: "))
        for x in range(n, n*2):
            print(x)
        os.system('cls')

        print("\nEjemplo 6: ")
        c=int(input("Ingrese una cantidad de número: "))
        total=0
        for x in range(c):
            nume=int(input("Ingrese número a sumar: "))
            total=total+nume
        print("Total de la cuma: ", total)
        os.system('cls')
        
        print("\nEjemplo 7: ")
        # # # frase=input("Ingrese una frase: ")
        # # # for x in "aeiou":
        # # #     if x in frase:
        # # #         print(x)


        cantidad=0
        frase=input("Ingrese una frase: ")
        for x in frase:
            if x in "aeiou":
                cantidad+=1
        print("Cantidad de vocales: ",cantidad)
resul17_1=Video17_ejercicio1()
resul17_1.vide17_ejer1()
os.system('cls')


##############! video 18
class Video18_ejercicio1:
    def vide18_ejer1(self):
        ### Ejercicio 1
        print("""\nEscribir un programa que muestre la sumatoria de todos los números entre el O y el 100.
¿Qué modificación habría que hacer si ahora sólo se deben sumar los números que sean múltiplos de 3?\n""")
        print("Punto 1")
        total=0
        for i in range(101):
            total+=i
        print("La sumatoria es: ", total)

        print("\nPunto 2")
        total=0
        for i in range(101):
            if i%3 == 0:
                total+=i
        print("Sumatoria de los múltiplos de 3 es:", total)
        os.system('cls')

        ### Ejercicio 2

        print("""\nDado un número entero positivo, mostrar su factorial. 
El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número.
El factorial de 0 es 1.\n""")

        numero=int(input("Ingrese un número: "))
        f=1
        if numero!=0:
            for i in range(1,numero+1):
                f=f*i
        print("El factorial de {} es {}.". format(numero,f))
        os.system('cls')
    ### Ejercicio 3

        print("""\nCrear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. 
La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de 
los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…\n""")

        n1=0
        n2=1
        print(n1)
        print(n2)
        for i in range(8):
            n3=n1+n2
            print(n3)
            n1=n2
            n2=n3
        os.system('cls')
        
        ### Ejercicio 3

        print("""\nEscribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o 
negativos. Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.
No olvides que no es posible dividir por cero, por lo que es necesario evitar que el programa arroje un 
error si no se ingresaron números positivos.\n""")

        sumaPositivos=0
        cantidadPositivos=0
        sumaNegativos=0
        for i in range(6):
            nuro=int(input("Ingrese un número: "))
            if nuro>0:
                sumaPositivos=sumaPositivos+nuro
                cantidadPositivos=cantidadPositivos+1
            else:
                sumaNegativos=sumaNegativos+nuro
        print("Sumatoria de los negativos: ", sumaNegativos)
        if cantidadPositivos!=0:
            print("Promedio de los positivos: ",round(sumaPositivos/cantidadPositivos,2))
        else:
            print("No se ingresaron números positivos.")
resul18_1=Video18_ejercicio1()
resul18_1.vide12_ejer1()
os.system('cls')




##############! video 19
class Video19_ejercicio1:
    def vide19_ejer1(self):
        ### Ejercicio 1
        print("""\nUn grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6 integrantes cada uno, 
donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”. La regla más importante del juego es que sólo 
se comunicarán mediante un canal común, por lo que deben buscar la forma de ocultar el contenido de sus mensajes. Uno de los equipos 
decide utilizar un método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del mensaje 
–considerando la posición de cada una en el alfabeto– una determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 
lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.

Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales. Escribir un programa que permita encriptar los 5 
mensajes. El corrimiento (cantidad de lugares que se correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 
5 mensajes usarán el mismo corrimiento.

Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la letra “a”. Ejemplo: 
la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto español, de 27 letras, el siguiente cálculo matemático 
permite volver a comenzar por el principio una vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27

Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación.\n""")

        alfabeto="abcdefghijklmnñopqrstuvwxyz"
        corrimiento=int(input("Corrimiento: "))
        for i in range(5):
            mensaje=input("Mensaje a encriptar: ")
            encriptado=""
            for caracter in mensaje:
                if caracter.lower() in alfabeto:
                    indice=alfabeto.find(caracter.lower())
                    indice=(indice+corrimiento)%27
                    encriptado+=alfabeto[indice]
                else:
                    encriptado+=caracter
            print("Mensaje encriptado: ", encriptado)
resul19_1=Video19_ejercicio1()
resul19_1.vide19_ejer1()
os.system('cls')


##############! video 20
class Video20_ejercicio1:
    def vide20_ejer1(self):
        ### Ejercicio 1
        ### Repetición condicianal: while
        ### Permite repetir un bloque de código mientras una condición sea verdadera [el valor de la condición podría cambiar durante la repetición].
        ### Cuando la condición se vuelve fasa, termina la repetición del bloque y continúa ejecutándose el resto del problema.
        ### Ejemplo:
        ### while condición: ##condición: es un balor booleano
        ###     #bloque a repetir

        print("""\nEjemplo 1:
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, 
mostrar la sumatoria de todos los números ingresados.\n""")

        total=0 
        nro1=int (input ("Número: ")) 
        while nro1 != 0:
            total+=nro1 
            nro1=int (input ("Número: "))
        print("La suma es: ",total)
        os.system('cls')
        ###o ¿Por qué se debe repetir la instrucción input al final del bloque?
        ### Respuesta: Para que cambie la variable nro que interviene en la condición para que en un momento la condición se vuelva falsa

        ### o ¿Qué sucede si, en vez de leer con input, se asigna el valor 4 a la variable nro? 
        # # # total=0 
        # # # nro=4 ## Haría que entre en un blucle infinito ya que sólo va a evaluar 4!=0 y eso es verdadero y nunca salria del bucle.
        # # # while nro != 0:
        # # #     total+=nro 

        ### ¿Y si se asigna el 0?
        # # # total=0 
        # # # nro=0         ## la condición sería falsa y el bloque no se ejecutaria.
        # # # while nro != 0: 
        # # #     total+=nro 


        print("""\nEjemplo 2:
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, 
mostrar la sumatoria de todos los números positivos ingresados.\n""")

        positivos=0
        n=int(input("Ingrese un número (0 para terminar): "))
        while n!=0:
            if n>0:
                positivos+=1
            n=int(input("Ingrese un número (0 para terminar): "))
        print("Cantidad de positivos:", positivos)
        os.system('cls')

        print("""\nEjemplo 3:
Leer números enteros positivos de teclado, hasta que el usuario ingrese un número 
negativo (-1). Informar cuál fue el mayor número ingresado.\n""")

        mayor=-1
        n=int(input("Número positivo:"))
        while n>=0:
            if n>mayor:
                mayor=n
            n=int(input("Número positivo:"))
        print("Mayor número ingresado:", mayor)
        os.system('cls')

        print("""\n\Ejemplo 4:
Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.\n""")

        suma=0
        n=int(input("Número positivo:"))
        while n!=0:
            digito=n%10
            suma+=digito
            n=n//10
        print("Suma de los dígitos:", suma)
        os.system('cls')

        print("""\n\Ejemplo 5:
Solicitar al usuario que ingrese números enteros positivos y, por cada uno, 
imprimir la suma de los dígitos que lo componen. La condición de corte es 
que se ingrese el número -1. Al finalizar, mostrar cuántos de los números 
ingresados por el usuario fueron números pares.\n""")

        pares=0
        n=int(input("Ingrese un número (-1 para terminar el programa): "))
        while n!=-1:
            if n%2 == 0:
                pares+=1
            suma=0
            while n!=0:
                digito=n%10
                suma+=digito
                n=n//10
            print("Suma de sus dígitos:", suma)
            n=int(input("Ingrese un número (-1 para terminar el programa): "))
        print("Se ingresaron", pares, "números pares")
resul20_1=Video20_ejercicio1()
resul20_1.vide20_ejer1()
os.system('cls')


##############! video 21
class Video21_ejercicio1:
    def vide21_ejer1(self):
        ### Ejercicio 1
        print("""\nCrear un programa que permita al usuario ingresar los montos de las compras de un cliente 
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando 
el ingreso de datos cuando el usuario ingrese el monto 0.

Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al 
finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de 
$1000, se le debe aplicar un 10% de descuento.\n""")

    total=0
    monto=float(input("Ingrese monto de una venta: $"))
    while monto!=0:
        if monto<0:
            print("Monto no válido.")
        else:
            total+=monto
        monto=float(input("Ingrese monto de una venta: $"))
    if total>1000:
        total-=total*0.1
    print("Monto total a pagar: $", total)
resul21_1=Video21_ejercicio1()
resul21_1.vide21_ejer1()
os.system('cls')


class Video21_ejercicio2:
    def vide21_ejer2(self):
        ### Ejercicio 2
        print("""\nCrear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario 
ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.\n""")

        numero=int(input("Ingrese un número: "))
        totalPares=0
        totalImpares=0
        while numero!=0:
            pares=0
            impares=0
            while numero!=0:   
                ultimodigito=numero%10
                if ultimodigito%2==0:
                    pares+=1
                    totalPares+=1
                else:
                    impares+=1
                    totalImpares+=1
                numero=numero//10
            print("El número ingresado tiene ",pares," digitos pares y ",impares," digitos impares.")
            numero=int(input("Ingrese otro número (ingrese 0 si desea terminar el programa): "))
        print("Total de dígitos pares:", totalPares)
        print("Total de dígitos impares:", totalImpares)
resul21_2=Video21_ejercicio2()
resul21_2.vide21_ejer2()
os.system('cls')


class Video21_ejercicio3:
    def vide21_ejer3(self):
        ### Ejercicio 3
        print("""\nCrear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando 
el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 
1 que contenga sólo una barra (“/”) se considera que termina una línea. 

Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos 
los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.

**Ejemplo de ejecución:**
Libro: Los 3 mosqueteros
Libro: Historia de 2 ciudades
Libro: /
Línea completa. Aparecen 2 dígitos numéricos.
Libro: 20000 leguas de viaje submarino
Libro: El señor de los anillos
Libro: /
Línea completa. Aparecen 5 dígitos numéricos.
Libro: 20 años después
Libro: *
Fin. Se leyeron 2 líneas completas.\n""")

        lineas=0
        digitos="0123456789"
        cantidadDigitos=0
        cadena=input("Título del libro: ")
        while cadena!="*":
            for caracter in cadena:
                if caracter in digitos:
                    cantidadDigitos+=1
            if cadena=="/":
                lineas+=1
                print("Aparecen ", cantidadDigitos, " dígitos en la línea\n")
                cantidadDigitos=0
            cadena=input("Título del libro: ")
        print("Se leyeron ",lineas," líneas completas")
resul21_3=Video21_ejercicio3()
resul21_3.vide21_ejer3()
os.system('cls')


##############! video 22

class Video22_ejercicio1:
    def vide22_ejer1(self):
        ### Ejercicio 1
        print("""\nInterpretación de código
Analizar el código mostrado a continuación y, sin ejecutarlo previamente, describir qué hace.
¿Qué salida se mostraría en pantalla si se ejecuta el programa sucesivamente con los siguientes datos?
1) Frase: “ hola buen día"
2) Frase: ""
3) Frase: "1234" 
4) Frase: "hola ¡buen día!"\n""")

        frase=input("Frase: ").strip()
        cantidad=0
        len_p_mas_larga=0
        while len(frase) != 0:
            cantidad=cantidad+1
            i=frase.find(" ")
            if i != -1:
                palabra=frase[0:i]
                while i < len(frase) and frase[i] == " ":
                    i=i+1
                frase=frase[i:]
            else:
                palabra=frase
                frase=""
            if len(palabra) > len_p_mas_larga:
                len_p_mas_larga=len(palabra)
                p_mas_larga=palabra
        if cantidad > 0:
            print("Palabra más larga:", p_mas_larga)
        print("Cantidad de palabras:", cantidad)


        # # Respuesta:
        # # El programa solicita al usuario que ingrese una frase y luego informa cuál fue la palabra más larga 
        # # (en caso de haber más de una muestra la primera) y cuántas palabras había. 
        # # Se toma como separador de palabras al carácter (espacio), ya sea uno o más!
        # # 1) Frase: “ hola buen día"
        # # Palabra más larga: hola 
        # # Cantidad de palabras: 3

        # # 2) Frase: ""
        # # Cantidad de palabras: 0

        # # 3) Frase: "1234" 
        # # Palabra más larga: 1234 
        # # Cantidad de palabras: 1

        # # 4) Frase: "hola ¡buen día!"
        # # Palabra más larga: ¡buen 
        # # Cantidad de palabras: 3
resul22_1=Video22_ejercicio1()
resul22_1.vide22_ejer1()
os.system('cls')


##############! video 23
class Video23_ejercicio1:
    def vide23_ejer1(self):
        ### Ejercicio 1

        ### break: cortar # corta el ciclo de repeticiones.
        ### continue: continuar # saltea el resto del bloque y pasa a la siguiente iteración.
        ### Ejemplo
        ### se puede salir del bucle de forma "natural" o interrumpiéndolo 
        ### while condición 1: 
        ###     #bloque a repetir
        ###     if condición 2:
        ###         break
        ###     #resto del bloque
        ### #resto del bloque

        ### Sólo se sale del bucle de forma "natural"
        ### while condición 1: 
        ###     #bloque a repetir
        ###     if condición 2:
        ###         continue
        ###     #resto del bloque
        ### #resto del bloque


        print("""\nEjemplo 1:
Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, 
el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe 
volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un 
texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.\n""")

        while True:
            print("Opción 1 - comenzar programa")
            print("Opción 2 - imprimir listado")
            print("Opción 3 - finalizar programa")
            opcion=int(input("Opción elegida: "))
            if opcion==1:
                print("¡Comenzamos!")
            elif opcion==2:
                print("Listado:")
                print("Nadia, Esteban, Mariela, Fernanda")
            elif opcion==3:
                print("Hasta la próxima")
                break
            else:
                print("Opción incorrecta. Debe ingresar 1, 2 o 3")
resul23_1=Video23_ejercicio1()
resul23_1.vide23_ejer1()
os.system('cls')


class Video23_ejercicio2:
    def vide23_ejer2(self):
        print("""\nEjemplo 2:
Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar 
en la frase). Recorrer la frase, carácter a carácter, comparando con la letra 
buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa 
posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, 
indicar en qué posición se encontró y finalizar la ejecución.\n""")

        frase=input("Frase: ")
        l=input("Letra para buscar su posición: ")
        i=0
        while i!=len(frase):
            if l!=frase[i]:
                print("No se encontró en la posición", i)
                i+=1
                continue
            print("Se encontró en la posición", i)
            break
resul23_2=Video23_ejercicio2()
resul23_2.vide23_ejer2()
os.system('cls')


##############! video 24

class Video24_ejercicio1:
    def vide24_ejer1(self):
        ### Ejercicio 1
        print("""\nEscribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.\n""")

        cantidad=0
        n=int(input("Ingrese un número: "))
        while n!=0:
            primo=True
            for i in range(2,n):
                if n%i==0:
                    primo=False
                    break
            if primo:
                cantidad+=1
            n=int(input("Ingrese un número(0 finalizar el programa): "))
        print("Primos: ", cantidad)
resul24_1=Video24_ejercicio1()
resul24_1.vide22_ejer1()
os.system('cls')


class Video24_ejercicio2:
    def vide24_ejer2(self):
        print("""\nEscribir un programa que permita al usuario ingresar dos años y luego 
imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10. 
Nota: para que un año sea bisiesto debe ser divisible por 
4 y no debe ser divisible por 100, excepto que también sea divisible por 400.\n""")

        anioInicio=int(input("Año inicial: "))
        anioFin=int(input("Año final: "))
        for anio in range(anioInicio, anioFin+1):
            if not anio%10==0:
                continue
            if not anio%4==0:
                continue
            if anio%100!=0 or anio%400==0:
                print(anio)
resul24_2=Video24_ejercicio2()
resul24_2.vide24_ejer2()
os.system('cls')



##############! video 25
### Ejercicio 1

### Explicación sobre "Funciones"
### Funciones: pueden recibir datos para procesarlos y devolver un resultado
### Una función es un "módulo" de código que realiza una tarea específica. 
### Las funciones "encapsulan" una tarea: reúnen varias líneas de código que pueden ejecutarse como una sola.

###             ¿Para qué sirven? 
### • Reutilizar código en vez de reescribirlo. 
### • Dividir un problema en partes más pequeñas ("modularizar") para quitarle complejidad y poder resolver cada parte por separado (incluso otros programadores). 
### • Probar cada parte de nuestro programa de forma individual (para verificar que funcione correctamente).

### Ejemplo:
### Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo. 
### Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). 
### Al finalizar el programa, mostrar el factorial del mayor número ingresado.

### mayor=0 
### Leer número 
### Mientras !número sea primo:
###       Mostrar !suma dígitos de número 
###       Leer digito 
###       Mostrar !frecuencia de dígito en número 
###       Si número > mayor:
###            mayor=número 
###       Leer número 
### Mostrar !factorial de mayor

###             Partes de una función
### • def (palabra clave para definir una función) 
### • Nombre 
### • Parámetros (ninguno o más - cantidad ilimitada) 
### • Cuerpo (bloque de código] 
### • Valor de retorno (ninguno ó uno)

### def nombre(parámetros):
###     #cuerpo de la función 
###     #valor de retorno

### Por fuera de la función: "llamada" o "invocación" (para que la función se ejecute]

###              Nombre ["identificador“)
### Las mismas reglas que se usan para identificadores de variables:
### • Sólo puede contener letras, digitos numéricos o guión bajo. 
### • No puede empezar con un número.
### • No puede ser igual a alguna palabra reservada del lenguaje.
###             Representativo de lo que hace la función
###
### nombre: validar
### def validar (email):
###     #cuerpo de la función
###     #retorno

###             Parámetros
### Datos que se "mandan" a la función.
### • Pueden ser de cualquier tipo. 
### • Si hay más de un parámetro, se separan con coma (la cantidad de parámetros y de argumentos debe ser la misma) 
### • Dentro de la función actúan como variables. 
### • La función puede modificarlos sólo dentro de su ámbito. 
### • Se puede indicar un valor por defecto (se usará sólo si al llamar a la función no se manda ningún valor para ese parámetro).

### dónde ouede usarse cada variable: ámbito de las variables --(variables se guarda en un espacio de la menoria) en la memoria

###             Cuerpo de una función
### • Bloque de código como cualquier otro (se pueden crear variables, incluir bucles, decisiones, anidar estructuras, etc.). 
### • Si incluye variables locales, su ámbito se restringe a la función. 
### • Los parámetros se pueden utilizar como variables dentro del cuerpo de la función. Si su valor cambia, no se modifica fuera de la función.

###             Valor de retorno
### • Es el "resultado" de la operación que realiza la función. 
### • Puede ser de cualquier tipo de dato. 
### • Puede no estar, si la función no necesita retornar nada. 
### • Si la función retorna algo, sólo puede retornar una cosa por vez. 
### • Donde aparece la instrucción return, la función corta su ejecución.

###             "Llamar“ a una función
### • Desde cualquier parte del código (incluso otra función).
### • Poniendo el nombre y los argumentos (la cantidad de parámetros y de argumentos debe coincidir, 
###   no así el nombre de los argumentos con el nombre de los parámetros). 
### • Puede llamarse varias veces, pasándole distintos argumentos. 
### • La llamada a la función "se reemplaza" por su valor de retorno. Como con cualquier otra 
###   operación, se puede asignar este valor a una variable, usarse en una operación, imprimirlo, etc.

###             Cómo crear una función
### • Dentro del mismo archivo donde está el resto del programa 
### • En un archivo diferente y luego importarlo desde el programa: from archivo import *
### 1) Definir exactamente que operación realizará (nombre adecuado) 
### 2) Definir qué datos necesitará recibir al llamarla (parámetros) 
### 3) Definir si hay un valor de retorno y cuál será 
### 4) Crear el algoritmo que realizará la tarea 
### 5) Colocar el valor de retorno (instrucción return)

### Una función debe ser atómica
### • Una única tarea indivisible
### • Que tenga sentido y contenga todos los pasos 
### • Tarea genérica que pueda reusarse



##############! video 26
class Video26_ejercicio1:
    def vide26_ejer1(self):
        ### Ejercicio 1
        print("""\nEjemplo 1:
Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, 
valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".\n""")

        def validar(email):
            caracterBuscado="@"
            emailValido=False
            for c in email:
                if c==caracterBuscado:
                    return True
            return False

        ### programa principal
        direccion=input("Tu email: ")
        if validar(direccion):
            print("Dirección válida")
        else:
            print("Dirección inválida")
resul26_1=Video26_ejercicio1()
resul26_1.vide26_ejer1()
os.system('cls')


class Video26_ejercicio2:
    def vide26_ejer2(self):
        print("""\nEjemplo 2:
Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos.\n""")

        def sumaDigitos(numero):
            suma=0
            while numero!=0:
                digito=numero%10
                suma=suma+digito
                numero=numero//10
            return suma

        ### programa principal
        num=int(input("Ingrese un número a procesar: "))
        while num!=0:
            print("Suma:",sumaDigitos(num))
            num=int(input("Ingrese un número a procesar (0 para finalizar el programa): "))
resul26_2=Video26_ejercicio2()
resul26_2.vide26_ejer2()
os.system('cls')


class Video26_ejercicio3:
    def vide26_ejer3(self):     
        print("""\nEjemplo 3:
Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. 
Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos.\n""")
            
        def sumaDigitos(numero):
            suma=0
            while numero!=0:
                digito=numero%10
                suma=suma+digito
                numero=numero//10
            return suma

        ### programa principal
        sumatoria=0
        num=int(input("Ingrese un número a procesar: "))
        while num!=0:
            print("Suma:",sumaDigitos(num))
            sumatoria=sumatoria+num
            num=int(input("Ingrese un número a procesar (0 para finalizar el programa): "))
        print("La sumatoria es: ", sumatoria)
        print("Dígitos: ", sumaDigitos(sumatoria))    
resul26_3=Video26_ejercicio3()
resul26_3.vide26_ejer3()
os.system('cls')            


class Video26_ejercicio4:
    def vide26_ejer4(self):  
        print("""\nSolicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo. 
Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). 
Al finalizar el programa, mostrar el factorial del mayor número ingresado.\n""")
            
        def primo(num):
            for i in range(2,num):
                if num%i==0:           
                    return False
            return True

        def frecuencia(numero,digito):
            cantidad=0
            while numero!=0:
                ultDigito=numero%10
                if ultDigito==digito:
                    cantidad+=1
                numero=numero//10
            return cantidad

        def factorial(numero):
            f=1
            if numero!=0:
                for i in range(1,numero+1):
                    f=f*i
            return f

        def sumaDigitos(numero):
            suma=0
            while numero!=0:
                digito=numero%10
                suma=suma+digito
                numero=numero//10
            return suma

        ### programa principal
        mayor=0
        numero=int(input("Número primo: "))
        while primo(numero):
            print("Suma de los dígitos:",sumaDigitos(numero))
            digito=int(input("Dígito: "))
            print("El",digito,"aparece",frecuencia(numero,digito),"veces")
            if numero > mayor:
                mayor=numero
            numero=int(input("Número primo: "))
        print("Factorial de",mayor,"es:",factorial(mayor))
resul26_4=Video26_ejercicio4()
resul26_4.vide26_ejer4()
os.system('cls')        


##############! video 27
class Video27_ejercicio1:
    def vide27_ejer1(self):
        ### Ejemplo incorrectos [qué no hacer]
        ### Ejemplo 1

        ### USAR VARIABLES DEL ÁMBITO GLOBAL DENTRO DE LAS FUNCIONES.
        ### inconvenientes al usar variables globales
        ### • Se "pierde la cuenta" de qué dato tendría que contener cada variable.
        ### • Se "ensucia" el espacio de nombres.
        ### • Mayor acoplamiento en el código.
        ### NO
        # # def primo():
        # #         for i in range(2,numero):  ## <= numero  NO
        # #             if numero%i==0:        ## <= numero  NO   
        # #                 return False
        # #         return True

        # # #programa principal
        # # numero=int(input("Número: "))
        # # if primo():
        # #     print("Es primo")
        # # else:
        # #     print("No es primo")

        # ### SI      correcto pasaje de párametros
        print("""\nRequerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.\n""")

        def primo(numero):       ## numero  si
                for i in range(2,numero):  
                    if numero%i==0:          
                        return False
                return True

        ###programa principal
        numero=int(input("Número: "))
        if primo(numero):         ### numero   si
            print("Es primo")
        else:
            print("No es primo")
resul27_1=Video27_ejercicio1()
resul27_1.vide27_ejer1()
os.system('cls')


class Video27_ejercicio2:
    def vide27_ejer2(self):
        # ### Ejemplo 2

        # ### FUNCIONES QUE HACEN MÁS DE UNA TAREA [CALCULAR ALGO E IMPRIMIR EL RESULTADO]


        # # # ### NO
        # # # def frecuencia(numero,digito):
        # # #     cantidad=0
        # # #     while numero!=0:
        # # #         ultDigito=numero%10
        # # #         if ultDigito==digito:
        # # #             cantidad+=1
        # # #         numero=numero//10
        # # #     print(digito,"aparece",cantidad,"veces")    ###<=   NO
        # # #     ##ó
        # # #     return cantidad           ###Error común: invocar a una función que retorna un valor, pero no hace nada con ese valor.
        # # # ###programa principal
        # # # num=int(input("Número: "))
        # # # un_digito=int(input("Dígito: "))
        # # # frecuencia(num,un_digito)                       ###<=   NO

        # ### SI 

        print("""\nSolicitar al usuario un número entero y luego un dígito. Informar la cantidad de 
        ocurrencias del dígito en el número, utilizando para ello una función que calcule la frecuencia.\n""")

        def frecuencia(numero,digito):
            cantidad=0
            while numero!=0:
                ultDigito=numero%10
                if ultDigito==digito:
                    cantidad+=1
                numero=numero//10
            return cantidad                     ###SI

        ###programa principal
        num=int(input("Número: "))
        un_digito=int(input("Dígito: "))
        print("Frecuencia del dígito en el número:",frecuencia(num,un_digito))  ###SI
resul27_2=Video27_ejercicio2()
resul27_2.vide27_ejer2()
os.system('cls')


class Video27_ejercicio3:
    def vide27_ejer3(self):
        ### ejemplo 3

        # Funciones que hacen más de una tarea (solicitar datos al usuario, procesarlos y contabilizar)

        # Programa que pide números al usuario, muestra el factorial de cada uno y luego la cantidad total de números leidos

        # Debe poder identificar qué tarea concreta realiza una función.

        #### NO
        # # # def factorial():
        # # #     cantidad=0 
        # # #  [[[n=int(input ("Número: ")) 
        # # #     while n!=-1:
        # # #         f=1 
        # # #         if n!=0: 
        # # #             for i in range (1,n+1):         ### NO - parece correcto pero esta función no es atómica
        # # #                 f=f*i                       ### hace muchas cosas
        # # #         print("Factorial:", f) 
        # # #         cantidad+=1
        # # #         n=int (input ("Número: ")) ]]]
        # # #     return cantidad
        # # # ####programa principal 
        # # # cantidad=factorial()
        # # # print("Se leyeron", cantidad, "números")

        # ### SI
        print("""\nEscribir un programa que pida números al usuario, motrar el factorial 
        de cada uno y, al finalizar, la cantidad total de números leídos en total.\n""")

        def factorial(numero):
            f=1
            if numero!=0:
                for i in range(1,numero+1):         #### Tienen una función que ahora es atómica
                    f=f*i
            return f

        ####programa principal
        cantidad=0
        num=int(input("Número (-1 para cortar): "))
        while num!=-1:
            print("Factorial:", factorial(num))      #### Todo el resto del procesamiento dentro del programa principal.
            cantidad+=1
            num=int(input("Número (-1 para cortar): "))
        print("Se leyeron",cantidad,"números.")
resul27_3=Video27_ejercicio3()
resul27_3.vide27_ejer3()
os.system('cls')


class Video27_ejercicio4:
    def vide27_ejer4(self):
        ### ejemplo 4

        ### Llamar a una función sin argumentos. No usar el valor de retorno.

        ### Programa que pide números positivos al usuario. Muestra el
        ### número cuya sumatoria de digitos fue mayor, y la cantidad 
        ### de números cuya sumatoria de digitos fue menor que 10.

        #### NO
        # # # def sumaDigitos(numero):
        # # #     suma=0
        # # #     while numero!=0:
        # # #         digito=numero%10
        # # #         suma=suma+digito
        # # #         numero=numero//10
        # # #     return suma

        # # # ###programa principal
        # # # cantidad=0 
        # # # mayor=-1 
        # # # numero=int(input ("Número positivo: ")) 
        # # # while numero > 0:
        # # #     sumaDigitos (numero) 
        # # #     if sumaDigitos > mayor:         #### NO(sumaDigitos) # no se puede usar entre una función y un entero.
        # # #         mayor=sumaDigitos
        # # #         n_mayorsuma=numero 
        # # #     if sumaDigitos< 10:            #### No (sumaDigitos)
        # # #         cantidad+=1 
        # # #     numero=int(input("Número positivo: "))
        # # # print("Sumatoria de digitos de", n_mayorsuma,":",mayor)
        # # # print("Cantidad con sumatoria menor a 10: ",cantidad) 


        #### SI
        print("""\nEscribir un programa que pida números positivos al usuario. Mostrar el número cuya sumatoria de dígitos fue mayor y la 
        cantidad de números cuya sumatoria de dígitos fue menor que 10.\n""")

        def sumaDigitos(numero):
            suma=0
            while numero!=0:
                digito=numero%10
                suma=suma+digito
                numero=numero//10
            return suma

        ###programa principal
        cantidad=0
        mayor=-1
        numero=int(input("Número positivo: "))
        while numero>=0:
            suma=sumaDigitos(numero)
            if suma > mayor:
                mayor=suma
                n_mayorsuma=numero
            if suma < 10:
                cantidad+=1
            numero=int(input("Número positivo (número negativo para finalizar el programa): "))
        print("Sumatoria de dígitos de",n_mayorsuma,":",mayor)
        print("Cantidad con sumatoria menor a 10:",cantidad)
resul27_4=Video27_ejercicio4()
resul27_4.vide27_ejer4()
os.system('cls')



##############! video 28

class Video28_ejercicio1:
    def vide28_ejer1(self):
        ### Ejercicio 1
        print("""\nSin ejecutar el siguiente programa, determinar cuál es la salida en pantalla si se ingresan los valores x=6, y=7:

def coordenadaZ(x,y):
    x=x+10
    y=y+15
    return x+y

###programa principal
x=int(input("Coordenada eje x: "))
y=int(input("Coordenada eje y: "))
for i in range(3):
    z=coordenadaZ(x,y)
    x=x+1
    y=y+1
print(x," . ",y)

Respuesta: Imprime: 9 . 10

¿Qué sucede si los nombres de los parámetros dentro de la función se 
cambian, y ahora se utilizan los nombres a, b en lugar de los nombres x, y?

Respuesta: cambiar el nombre de los parámetros no afecta en nada, porque el 
valor retornado por la función no se ésta usando en el programa principal.\n""")

        def coordenadaZ(x,y):
            x=x+10
            y=y+15
            return x+y

        ###programa principal
        x=int(input("Coordenada eje x: "))
        y=int(input("Coordenada eje y: "))
        for i in range(3):
            z=coordenadaZ(x,y)
            x=x+1                            ## en cada iteración x suma uno 6+1=7 7+1=8 8+1=9 
            y=y+1                            ## lo mismo para y
        print(x," . ",y)
resul28_1=Video28_ejercicio1()
resul28_1.vide28_ejer1()
os.system('cls')


class Video28_ejercicio2:
    def vide28_ejer2(self):
        print("""\nEl siguiente programa debería imprimir el número 2 si se le ingresan como 
    valores x=5, y=1 pero en su lugar imprime 5. ¿Qué hay que corregir?

    def maximo(a,b):
        if x>y:
            return x
        else:
            return y

    def minimo(a,b):
        if x<y:
            return x
        else:
            return y

    #programa principal
    x=int(input("Un número: "))
    y=int(input("Otro número: "))
    print(maximo(x-3, minimo(x+2, y-5))) 

    Respuesta: Las funciones no utilizan sus parámetros a, b sino las variables globales x, y. Para 
    corregir el error se deben utilizar los parámetros dentro del cuerpo de ambas funciones.
    \n""")

        def maximo(a,b):
            if a>b:
                return a
            else:
                return b

        def minimo(a,b):
            if a<b:
                return a
            else:
                return b

        ###programa principal
        x=int(input("Ingrese un número para x: "))
        y=int(input("Ingrese un número para y: "))
        print(maximo(x-3, minimo(x+2, y-5)))
resul28_2=Video28_ejercicio2()
resul28_2.vide28_ejer2()
os.system('cls')


##############! video 29

class Video29_ejercicio1:
    def vide29_ejer1(self):
        ### Ejercicio 1
        print("""\nEscribir una función que, dado un número de DNI, retorne True si el número es válido y 
False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.\n""")

        def validarDNI(dni):
            cantidad=0
            while dni!=0:
                cantidad+=1
                dni//=10
            return cantidad==7 or cantidad==8
        ## Probamos que funciones
        print(validarDNI(340))
        print(validarDNI(2531723))
resul29_1=Video29_ejercicio1()
resul29_1.vide29_ejer1()
os.system('cls')


class Video29_ejercicio2:
    def vide29_ejer2(self):
        ### Ejercicio 2
        print("""\nEscribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras 
están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro.\n""")

        def lenUltimaPalabra(frase):
            if len(frase)==0:
                return 0
            cantidad=0
            for i in range(len(frase)):
                if frase[i]!=' ':
                    cantidad+=1
                else:
                    if i<len(frase)-1 and frase[i+1]!=' ':
                        cantidad=0
            return cantidad
        ### Probamos
        print(lenUltimaPalabra("hola     "))
        print(lenUltimaPalabra("¿Cómo estás?"))
        print(lenUltimaPalabra("Hola mundo! buen día"))
resul29_2=Video29_ejercicio2()
resul29_2.vide29_ejer2()
os.system('cls')


class Video29_ejercicio3:
    def vide29_ejer3(self):
        ### Ejercicio 3
        print("""\nEscribir un programa que permita al usuario obtener un identificador para cada uno de los socios de 
un club. Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el 
procesamiento mediante el ingreso de un nombre vacío.

Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en 
cuyo caso será: nombre1 nombre2 apellido. Si un socio tuviera más de un apellido, el usuario sólo ingresará uno.

Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario 
en un bucle hasta que ingrese un DNI correcto.

Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad 
de letras del apellido y los primeros 3 dígitos de su DNI. Ejemplo:
Nombre: Alba María Linares
DNI: 25834910
Alba7258\n""")

        def lenUltimaPalabra(cadena):
            longitud=len(cadena)
            if longitud==0:
                return 0
            cantidad=0
            for i in range(longitud):
                if cadena[i]!=' ':
                    cantidad+=1
                else:
                    if cadena[i]==' ' and i<(longitud-1) and cadena[i+1]!=' ':
                        cantidad=0
            return cantidad

        def DNIvalido(dni):
            cantidad=0
            while dni!=0:
                cantidad+=1
                dni//=10
            return cantidad==7 or cantidad==8

        def primerosTresDigitos(numero):
            while numero >= 1000:
                numero = numero // 10
            return numero

        def obtenerIdentificador(nombre, dni):
            nombre=nombre.strip()
            id=nombre[:nombre.find(" ")]
            id=id+str(lenUltimaPalabra(nombre))
            id=id+str(primerosTresDigitos(dni))
            return id

        #programa principal
        nombre=input("Nombre del socio: ")
        while nombre!="":
            dni=int(input("DNI del socio: "))
            while not(DNIvalido(dni)):
                print("Número inválido.")
                dni=int(input("DNI del socio: "))
            print(obtenerIdentificador(nombre,dni))
            nombre=input("Nombre del socio: ")
resul29_3=Video29_ejercicio3()
resul29_3.vide29_ejer3()
os.system('cls')


##############! video 30
####                 PUEBAS
### casos de prueba: diferentes casos que pueden darse al ejecutar un programa.
### Funciones: test unitarios: se deberían ejecutarse cada vez que se modifica el códio.
### Responsabilidad del desarrolador.
### Garantizar la integridad del código y ayudan a advertir posibles errores.
### 
### Ejemplo:

### title()


###                 Disttintas ormas de probar
### 1) Ejecutar función e invocarla con distintos argumentos
### 2) Doctest
### 3) Tests unitarios ("unit tests")


# ###?                        PYTHON DOCTEST    ###Para funciones sencillas
# ###         Son partes de la documentación de la función ["docstring"]

# # • Antes de la implementación, incluir un string multilínea. Opcionalmente, colocar la documentación de la función (qué hace, parámetros, que retorna). 
# # • Colocar a continuación los casos de prueba en el formato usado por el intérprete interactivo. Usar comillas simples para los datos de tipo string.
# #       def titulo(cadena):
# #           '''                               ### comentamos los casos de pruebas
# #           >>> titulo('esto es una frase')   ### se ejecuta -- invocar la función 
# #           'Esto Es Una Frase'               ### valor que esperamos que retorne
# #           '''
# # • Al final del archivo:
# #       if __name__ == "__main__": 
# #           import doctest
# #           doctest.testmod()

##         La documentación de una función puede verse con: help(función)
class Video30_ejercicio1:
    def vide30_ejer1(self):

        ## Ejemplo de PYTHON DOCTEST
        print("""\nEjemplo 1:
Función titulo(): recibe un string y lo retorna convirtiendo la primera letra de cada palabra a mayúscula y las demás 
letras a minúscula, dejando inalterados los demás caracteres. Precondición: el separador de palabras es el espacio: " ".\n""")

        def titulo(cadena):
            print('''
            Recibe una cadena de caracteres y retorna una copia que tiene la
            primera letra de cada palabra en mayúsculas y el resto de las letras
            en minúsculas.
            >>> titulo('esto es una frase')
            'Esto Es Una Frase'
            >>> titulo('ESTO ES UNA FRASE')
            'Esto Es Una Frase'
            >>> titulo('palabra')
            'Palabra'
            >>> titulo('   esto es una frase')
            '   Esto Es Una Frase'
            >>> titulo('esto es una frase   ')
            'Esto Es Una Frase   '
            >>> titulo('esto   es   una   frase')
            'Esto   Es   Una   Frase'
            >>> titulo('')
            ''
            >>> titulo(' ')
            ' '
            >>> titulo('123')
            '123'
            >>> titulo('-1esto 2es 3una 4frase')
            '-1Esto 2Es 3Una 4Frase'
            >>> titulo('esto1 es2 una3 frase4---')
            'Esto1 Es2 Una3 Frase4---'
            ''')
            nueva=""
            inicioPalabra=True              #indica el inicio de una palabra
            for caracter in cadena:
                if not caracter.isalpha():
                    nueva=nueva+caracter
                    inicioPalabra=True
                else:
                    if inicioPalabra:
                        nueva=nueva+caracter.upper()
                        inicioPalabra=False  #ya no es el inicio de una palabra 
                    else:
                        nueva=nueva+caracter.lower()
            return nueva
        print(help(titulo))

        ###probamos
        print(titulo("esto es una frase"))
resul30_1=Video30_ejercicio1()
resul30_1.vide30_ejer1()
os.system('cls')



##?                    Tests unitarios: unittest
# # • Al principio del archivo importamos: import unittest 
# # • Implementar la función normalmente. 
# # • Agregar el siguiente código, con los casos de prueba:
# #           class Pruebas (unittest. Test Case): 
# #               def tests_titulo(self):
# #               self.assertEqual(titulo('esto es una frase'), 'Esto Es Una Frase') 
# #               self.assertEqual(titulo('ESTO ES UNA FRASE'), 'Esto Es Una Frase')
# # • Al final del archivo:
# #           if __name__ == "__main__":
# #               unittest.main()

###* [es a parte:
###* otros "Fremeworks" de tests unitarios en Python: • unittest •pytest • nose 
###* frameworks o bibliotecas para "mocking" en Python: • mock • minimock • mochito]

### Hay diferentes "assert" que pueden usarse: assertNotEqual, assertTrue, assertin, etc.

import unittest
class Video30_ejercicio2:
    def vide30_ejer2(self):

        def titulo(cadena):
            nueva=""
            inicioPalabra=True              #indica el inicio de una palabra
            for caracter in cadena:
                if not caracter.isalpha():
                    nueva=nueva+caracter
                    inicioPalabra=True
                else:
                    if inicioPalabra:
                        nueva=nueva+caracter.upper()
                        inicioPalabra=False  #ya no es el inicio de una palabra 
                    else:
                        nueva=nueva+caracter.lower()
            return nueva
        class Puebas(unittest.TestCase):
            def tests_titulo(self):
                    #que sea igual ##lo retorna esta función con este argumento y string, si no son iguales vamos a mostrar estre error
                self.assertEqual(titulo('esto es una frase'), 'Esto Es Una FrasE', 'Error al convertir cadena minúscula')    ### es opcional
                self.assertEqual(titulo('ESTO ES UNA FRASE'),'Esto Es Una Frase')
                self.assertEqual(titulo('palabra'),'Palabra')
                self.assertEqual(titulo('   esto es una frase'),'   Esto Es Una Frase')
                self.assertEqual(titulo('esto es una frase   '),'Esto Es Una Frase   ')
                self.assertEqual(titulo('esto   es   una   frase'),'Esto   Es   Una   Frase')
                self.assertEqual(titulo(''),'')
                self.assertEqual(titulo(' '), ' ')
                self.assertEqual(titulo('123'),'123')
                self.assertEqual(titulo('-1esto 2es 3una 4frase'),'-1Esto 2Es 3Una 4Frase')
                self.assertEqual(titulo('esto1 es2 una3 frase4---'),'Esto1 Es2 Una3 Frase4---')
        if __name__=="__main__":
            unittest.main()
            
        ### si da OK es que no hubo error.    
        ### si hay una falla nos mostrará donde es que hubo ese error  
resul30_2=Video30_ejercicio2()
resul30_2.vide30_ejer2()
os.system('cls')

##############! video 31
## Explicación de listas y tuplas
## ?                contenedores

## agrupan elementos 
## son tipos de datos- se pueden crear variabes ue sean "contenedores" y guardan más de un elemento en una misma variable.
## strings, listas, tuplas, conjuntos, diccionarios.

##?             listas
# # • Elementos ordenados por índice correlativo (empezando en 0) 
# # • Los elementos pueden estar repetidos 
# # • Elementos heterogéneos (incluso otros contenedores) 
# # • Admiten rebanadas 
# # • Mutables (los valores almacenados pueden cambiarse)
# #|   104   |  "hola"   |   0.8   |  True    |    [1,2,3] |
# #|    0    |    1      |    2    |    3     |       4    | 

# #           Creación de una lista
# # Lista literal: elementos encerrados entre corchetes, separados porcoma.
# # lista_vacía = [] 
# # lista_vacía2 = list() 
# # lista_con_elementos = [104, "hola", 0.8, True] 
# # lista_desde_string = list("palabra") 
# # lista_desde_rango = list(range(5))

# #           Iterar por elementos de una lista
# # Iteración por el indice, con for: 
# # for i in range(len(lista)):
# #      print(lista[i])
# # • Iteración por el indice, con while: 
# # i=0 
# # while i<len(lista):
# #      print(lista[i]) 
# #      i+=1
# # • Iteración por los elementos: 
# # for elemento in lista:
# #       print(elemento)

#         # for elemento in contenedor:
#         #      ###bloque


# #           algunas operaciones con listas
# # Crear lista a partir de otro contenedor: list (contenedor) 
# # Concatenación: listal+lista2 
# # Longitud: len (lista) 
# # Elemento: lista[0] ó rebanada: lista[0:10] ó con paso: lista[0:10:2] 
# # Modificar elemento: lista [posición]=nuevo_valor 
# # Indice (posición de un elemento: lista.index (elemento) 
# # Inclusión (resultado booleano): elemento in lista
# # Contar ocurrencias de elemento: lista.count(elemento) 
# # Agregar elemento al final: lista.append(elemento) 
# # Agregar elemento en posición determinada: lista.insert (posición, elemento) 
# # Eliminar elemento: del lista[posición] ó: lista.remove (elemento) 
# # Vaciar lista: lista.clear()
# # ?dir(list) muestratodas las operaciones posibles con listas 


##?                    Tuplas
## Muy similares a las listas:
## • Elementos ordenados por índice correlativos
## • Los elementos pueden repetirse
## • Elementos
## • Admiten rabanadas
## • Se iteran de la misma forma
## • Casi las mismas operaciones que se pueden acer con las listas
## Las tuplas tienen algunas ventajas sobre las listas, en cuanto a eficiencia

##|     "5"  |   5   |    (9,6,1)   |  True    |    ["x", "y"]  |
##|      0   |   1   |        2     |    3     |        4       |

## Diferencia: Las tuplas son inmutables.

# #           Creación de una tupla
# # Tupla literal: elementos encerrados entre paréntesis opcionales, separados por coma.

# # tupla_vacía= () 
# # tupla_vacía2 = tuple() 
# # tupla_con_elementos = 104, "hola", 0.8, True 
# # tupla_desde_string = tuple("palabra") 
# # tupla_desde_rango = tuple(range(5))

##############! video 32

class Video32_ejercicio1:
    def vide32_ejer1(self):
        ### Ejercicio 1
        print("""\nDada la siguiente lista: 
L = ["almacenar", 8, "a", [1,2,3], True, (0,0,1), 85.7]

1) ¿Cuáles de estos elementos pertenecen a ella? 
85.7        0       True        [True]      [(0,0,1)]        85      "a"     [1,2,3]
2) ¿Cómo obtener la posición en que se encuentra el elemento (0,0,1)?
3) ¿Cómo eliminar el último elemento, independientemente de cuántos elementos haya en la lista? 
4) Utilizar una operación para contar cuántas veces aparece el string "a". ¿Cuál será el resultado?

Respuesta:
1) 85.7     True    "a"     [1,2,3]""")

        L = ["almacenar", 8, "a", [1,2,3], True, (0,0,1), 85.7]

        c=L.index((0,0,1))
        print("2) Se encuentra en la posición ",c)

        del L[len(L)-1]
        print("3)",L)

        x=L.count("a")
        print("4) Veces que se repite: ",x)
resul32_1=Video32_ejercicio1()
resul32_1.vide32_ejer1()
os.system('cls')


class Video32_ejercicio2:
    def vide32_ejer1(self):
        ## Ejercicio 2
        print("""\n1) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.
2) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
3) Recorrer la lista para imprimir la sumatoria de todos los elementos.
4) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
5) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que 
aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]\n""")

        def sumatoria(lista):
            suma=0
            for n in lista:
                suma+=n
            return suma

        def numerosMenores(lista, limite):
            nueva=[]
            for n in lista:
                if n<limite:
                    nueva.append(n)
            return nueva

        def frecuencias(lista):        ### Error común: if n not in nueva
            nueva=[]
            for n in lista:
                if [n, lista.count(n)] not in nueva:
                    nueva.append([n, lista.count(n)])
            return nueva

        ### 1
        numeros=[]
        nro=int(input("Ingrese un número (0 finalizar programa): "))
        while nro!=0:
            numeros.append(nro)
            nro=int(input("Ingrese un número (0 finalizar programa): "))
        ### 2
        ### print("Sumatoria de los números:", sumatoria(numeros))
        eliminar=int(input("Número a eliminar: "))
        ### 3
        if eliminar in numeros:
            numeros.remove(eliminar)
        else:
            print("Ese número no está entre los ingresados")
        print("La sumatoria de los números es:", sumatoria(numeros))
        ### 4

        limite=int(input("Filtrar números menores a: "))
        for n in numerosMenores(numeros, limite):
            print(n)
        ### 5
        print("Frecuencias:")
        for tupla in frecuencias(numeros):
            print(tupla[0],"aparece",tupla[1],"veces.")
resul32_2=Video32_ejercicio2()
resul32_2.vide32_ejer2()
os.system('cls')


##############! video 33

class Video33_ejercicio1:
    def vide33_ejer1(self):
        ### Ejercicio 1
        print("""\nEscribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). Ejemplo: 
[("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")] 

Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo: 
[("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")] 

Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
-Agregar pasajeros a la lista de viajeros.
-Agregar ciudades a la lista de ciudades.
-Dado el DNI de un pasajero, ver a qué ciudad viaja.
-Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
-Dado el DNI de un pasajero, ver a qué país viaja.
-Dado un país, mostrar cuántos pasajeros viajan a ese país.
-Salir del programa.\n""")

        def agregarPasajeros(pasajeros):
            nombre=input("Nombre -x para cortar: ")
            while nombre!="x":
                dni=int(input("DNI: "))
                destino=input("Ciudad destino: ")          ###6    nombre|dni|destino      
                pasajeros.append((nombre,dni,destino))     ###7 posición 0 1 2 
                nombre=input("Nombre -x para cortar: ")
            return pasajeros

        def agregarCiudades(ciudades):
            ciudad=input("Ciudad -x para cortar: ")
            while ciudad!="x":
                pais=input("País: ")
                ciudades.append((ciudad,pais))
                ciudad=input("Ciudad -x para cortar: ")
            return ciudades

        def buscarCiudad(pasajeros, dni):
            for viaje in pasajeros:          ###5 si coincide el dni de ese pasajero con el dni que tengo por parametro entonces retorno la ciudad
                if viaje[1]==dni:            ###8 si viaje de 1 coincide con el dni que me dan por parámetro---- retornamos la ciudad
                    return viaje[2]
            return ""

        def cantidadPasajerosCiudad(pasajeros, ciudad):
            cantidad=0
            for viaje in pasajeros:
                if viaje[2]==ciudad:          ###9 buco por ciudad y no por dni lo mismo que se hizo anteriormente
                    cantidad+=1
            return cantidad

        def buscarPaisDestino(pasajeros, ciudades, dni):
            buscada=buscarCiudad(pasajeros, dni)
            for ciudad in ciudades:
                if ciudad[0]==buscada:
                    return ciudad[1]
            return ""

        def cantidadPasajerosPais(pasajeros, ciudades, pais):
            cantidad=0                           ###11 ciudad va a contener siempre tuplas
            for viaje in pasajeros:              ###10 ver si coincide el nombre de la ciudad con la ciudad buscada___ ciudad va a ir iterando por cada elemento de ciudades
                if pais==buscarPaisDestino(pasajeros, ciudades, viaje[1]):
                    cantidad+=1                   ### 12 dada una tabla que representa un viaje ue contiene esos 3 datos y esos 3 datos representa un viaje puedo tomar el destino que es una ciudad 
                                                ### y buscar a qué país pertenece esa ciudad, si ese país es el mismo que nos dieron por parámetros sumo uno en cantidad
            return cantidad

        ### programa principal
        pasajeros=[]
        ciudades=[]
        while True:
            print("1. Agregar pasajeros")
            print("2. Agregar ciudades")
            print("3. Buscar ciudad destino mediante el DNI")
            print("4. Cantidad de pasajeros que viajan a una ciudad")
            print("5. Buscar país destino mediante DNI")
            print("6. Cantidad de pasajeros que viajan a un país")
            print("7. Salir del programa")
            opcion=int(input("Acción a ejecutar: "))
            if opcion==1:                               ###1 leer nombre, dni, destino, agregar tuplas a la lista
                print("AGREGAR PASAJEROS")
                pasajeros=agregarPasajeros(pasajeros)
            elif opcion==2:
                print("AGREGAR CIUDADES")
                ciudades=agregarCiudades(ciudades)      ###2 voy a recorrer sus elementos que son tuplas y en cada elemento voy a tener sus datos de un viaje: nombre, dni, destino
        ##                                              ###3 voy a tener que buscar dni por dni y cuando encuentre el que el usuario quiere retorno cual es la ciudad a la que ese pasajero viaja     
            elif opcion==3:                             ###4 nombre|dni|destino ||  nombre|dni|destino ||  nombre|dni|destino ||  nombre|dni|destino
                dni=int(input("DNI: "))
                print("El pasajero viaja a", buscarCiudad(pasajeros, dni))
            elif opcion==4:
                ciudad=input("Ciudad a buscar: ")
                print("Viajan", cantidadPasajerosCiudad(pasajeros, ciudad), "pasajeros")
            elif opcion==5:
                dni=int(input("DNI: "))
                print("Viaja a", buscarPaisDestino(pasajeros, ciudades, dni))
            elif opcion==6:
                pais=input("País: ")
                print("Viajan", cantidadPasajerosPais(pasajeros, ciudades, pais), "pasajeros")
            elif opcion==7:
                break
            else:
                print("Opción inválida")
resul33_1=Video33_ejercicio1()
resul33_1.vide33_ejer1()
os.system('cls')


##############! video 34

##?                    Conjuntos

## -Elementos sin orden (no ay índice)
## -Los elementos no pueden repetirse
## -Elementos heterogéneos, pero sólo de tipos inmutables
## -No admiten rebanadas(no tienen índice)
## -Mutables (pueden agregarse o eliminarse elementos)

## Concepto equivalente al de "conjunto" en matemáticas.
## | 104  |  "hola"  |   0.8 |   True    |   (1,2,3) |

##              Creación de un conjunto
# # conjunto_vacío = set()
# # conjunto_con_elementos = {104, "hola", 0.8, True} 
# # conjunto desde_string = set("palabra")
# # conjunto_desde_rango = set (range(5))
# # conjunto_desde_lista = set([10,20,30,40]) 
# # conjunto_desde_tupla = set(("a", "b", "c"))

# # No existe literal para el conjunto vacío. Para el conjunto con elementos, el literal se escribe
# # con los elementos separados por comas, encerrados entre llaves.

##             Iterar por elementos de un conjunto
## for elemento in conjunto:
##     print(elemento)
## 
## for elemento in contenedor:
##     #bloque

## no tienen índice por lo que sólo se pueden iterar de esta forma. 
class Video34_ejercicio1:
    def vide34_ejer1(self):
        print("Ejemplo de conjuntos: ")
        A=set()
        print(type(A))

        X=(1,2,3)
        print(set(X))

        B=(1,2,3,1,2,3,1,2,3) ### crea una sola copia de cada elemento
        print(set(B))

        C=set(X)==set(B)
        print(C)

        M=[1,2,3,1,2,3,1,2,3,1,2,3]
        print(set(M))
resul34_1=Video34_ejercicio1()
resul34_1.vide34_ejer1()
os.system('cls')
# #           Algunas operaciones con conjuntos
# # Crear conjunto a partir de otro contenedor: set(contenedor) 
# # Longitud: len(conjunto) 
# # Pertenencia: elemento in conjunto 
# # Agregar elemento: conjunto.add(elemento) o conjunto update (contenedor) 
# # Eliminar elemento: conjunto remove (elemento) o conjunto discard (elemento) 
# # Vaciar conjunto: conjunto.clear() 
# # Igualdad: conjuntol==conjunto2 
# # Unión de conjuntos: conjuntol | conjunto2
# # Intersección de conjuntos: conjuntol & conjunto2
# # Inclusión: conjuntol<conjunto2 , conjunto1>conjunto2
# # Diferencia: conjuntol-conjunto2 
# # Diferencia simétrica: conjuntol conjunto2
# # dir(set) muestra operaciones posibles con conjuntos.


##############! video 35
class Video35_ejercicio1:
    def vide35_ejer1(self):
        ### Ejercicio 1
        print("""\nDados los siguientes conjuntos: 
A = {"z", 8, "9", (10,20,30), 8, 9, 8} 
B = {7, 8, 9} 
1) ¿Cuántos elementos tiene el conjunto A? 
2) ¿Cómo se podrían agregar en el conjunto B los números 1, 2, 3, en una única operación? 
3) ¿Es A menor que B (A<B) o B menor que A (B<A)?

Respuesta:""")

        A = {"z", 8, "9", (10,20,30), 8, 9, 8} 
        print("1) ",len(set(A)))

        B = {7, 8, 9}
        B.update([1,2,3])
        print("2) ",set(B))

        ## A no es subconjunto de B ni B de A
        print("3) Ninguna de las dos. Cada uno tiene elementos únicos.")
resul35_1=Video35_ejercicio1()
resul35_1.vide35_ejer1()
os.system('cls')


class Video35_ejercicio2:
    def vide35_ejer2(self):
        ### Ejercicio 2
        print("""\nSolicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar 
“x”. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar “x”.
- Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.<>
- Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
- Informar qué nombres de nivel primario no se repiten en los de nivel secundario.\n""")

        def cargarNombres(alumnos):
            nombre=input("Ingrese un nombre (x finalizar programa): ")
            while nombre!="x":
                alumnos.add(nombre)
                nombre=input("Ingrese un nombre (x finalizar programa): ")
            return alumnos

        primaria=set()
        secundaria=set()
        print("ALUMNOS DE PRIMARIA")
        primaria=cargarNombres(primaria)
        print("ALUMNOS DE SECUNDARIA")
        secundaria=cargarNombres(secundaria)

        print("NOMBRES DE TODOS LOS ALUMNOS:")
        for nombre in primaria|secundaria:
            print(nombre)

        print("NOMBRES COMUNES:")
        for nombre in primaria&secundaria:
            print(nombre)

        print("NOMBRES DE PRIMARIA QUE NO SE REPITEN EN SECUNDARIA:")
        for nombre in primaria-secundaria:
            print(nombre)
resul35_2=Video35_ejercicio2()
resul35_2.vide35_ejer2()
os.system('cls')


class Video35_ejercicio3:
    def vide35_ejer3(self):
        ### Ejercicio 3
        print("""\nSuponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, 
la cual contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:
[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 
532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y retorne los domicilios 
de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente puede haber hecho más de una compra 
en el mes, por lo que la función debe retornar una estructura que contenga cada domicilio una sola vez.\n""")

        def direcciones(ventas):
            domicilios=set()
            for venta in ventas:            ## iterar
                domicilios.add(venta[3])    ## por cada venta agg el domicilio
            return domicilios

        print(direcciones([("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), 
        ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, 
        "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), 
        ("Jorge Russo", 15, 958, "Mirasol 218")]))
resul35_3=Video35_ejercicio3()
resul35_3.vide35_ejer3()
os.system('cls')



##############! video 36
## ?                       diccionarios
# # • Los elementos son “pares", formados por clave y valor 
# # • Sin orden 
# # • Las claves no pueden repetirse, los valores si 
# # • Claves heterogéneas, pero sólo de tipos inmutables 
# # • Valores heterogéneos (incluso otros contenedores) 
# # • No admiten rebanadas 
# # • Mutables (pueden agregarse o eliminarse elementos) 
# # • Las claves hacen las veces de "indice", permitiendo acceder a los valores mediante corchetes

## CLAVE    |   VALOR           |||CLAVE    |        VALOR
## "hola"   |   "hello"         |||  8      |     ["melina",16] 
## "adiós"  |   "bye"           |||  2      |     ["lucía",14]
## "día"    |   "day"           |||  6      |     ["karen",15]
## "noche"  |   "night"         |||  9      |     ["sonia",16]


# #                   Creación de un diccionario
# # Diccionario literal: pares encerrados entre llaves separados por coma.Clave y  valor se separan con dos puntos.

# # diccionario_vacío = {}
# # diccionario_vacío2 = dict() 
# # diccionario_con_elementos = {"hola": "hello", "adiós": "bye"} 
# # desde_contenedor = dict([("hola", "hello"), ("adiós", "bye")])


# #                        Iterar por pares de un diccionario
# #"keys":"clave"(keys en ingles significa clave)

# # • Iteración por las claves:
# # for clave in diccionario.keys():                  for clave in diccionario:
# #     print(clave)                                      print(clave)

# # • Iteración por los valores: 
# # for valor in diccionario.values():                for clave in diccionario:
# #     print(valor)                                      print(diccionario[clave])

# # • Iteración por clave y valor a la vez:
# # for clave, valor in diccionario.items():          for par in diccionario.items():
# #     print(clave, valor)                               print(par[o], par[1])

class Video36_ejercicio1:
    def vide36_ejer1(self):
        print("""Ejemplo "Diccionario".""")
        traducciones={"hola":"hello", "adiós": "bye", "día":"day", "noche":"night"}
        print(type(traducciones),
            "Diccionario: ", traducciones) ### imprime el diccionario
        print("")

        print("Claves: ",traducciones.keys()) ## lo que esta dentro es una lista que contiene string ---- imprime las claves 
        print("")

        for clave in traducciones.keys(): ## imprime las claves
            print("Clave: ",clave)
        print("")

        for valor in traducciones.values(): ## imprime los valores
            print("Valor: ",valor)
        print("")

        for clave,valor in traducciones.items():
            print(clave,"==>", valor)
        print("")  
        
        for dicc in traducciones.items():
            print(dicc[0],"===", dicc[1])
resul36_1=Video36_ejercicio1()
resul36_1.vide36_ejer1()
os.system('cls')            
    
# #               algunas operaciones con diccionarios

# # Longitud (cantidad de pares): len (diccionario) 
# # Inclusión de clave (resultado booleano): clave in diccionario (keys() opcional) 
# # Inclusión de valor (resultado booleano): valor in diccionario.values() 
# # Obtener valor: diccionario[clave] ó diccionario.get(clave [, valor]) 
# # Modificar valor: diccionario[clave]=nuevo_valor 
# # Agregar elemento: diccionario[clave)=valor 
# # Agregar elementos: diccionario.update((cl:vi, c2:v2, c3:v3)) 
# # Eliminar elemento: del diccionario[clave] 
# # Vaciar diccionario: diccionario.clear()

# # dir(dict) muestra operaciones posibles con diccionarios.    
    
    

##############! video 37

class Video37_ejercicio1:
    def vide37_ejer1(self):
        ### Ejercicio 1
        print("""\nDado el siguiente diccionario: 
        E = { 1:"a", "prueba":[1,2,3,5], (4,5):3 }
        1) ¿Es el 1 un elemento de E? 
        2) ¿Cuántos elementos tiene E? 
        3) ¿Por qué da error la instrucción E[0]? 
        4) ¿Qué retorna la instrucción 1 in E.values()? 
        5) ¿Qué retorna E["prueba"][2] y por qué?
        Respuesta: \n""")

        E = { 1:"a", "prueba":[1,2,3,5], (4,5):3 }
        print("1) No. Los elementos sólo pueden ser pares formados por clave:valor.")

        print("2) Tiene {} elementos (pares).".format(len(E)))

        print("3) Porque la clave 0 no existe en E")

        c=1 in E.values()
        print("""3) {}. El número 1 existe como clave y también existe dentro de la lista E["prueba"] pero no existe entre los valores del ciccionario E""".format(c))

        d=E["prueba"][2]
        print("""3) Retorna {} porque E["prueba"] es una lista, y su posición [2] almacena al número 3""".format(d))
resul37_1=Video37_ejercicio1()
resul37_1.vide37_ejer1()
os.system('cls')


class Video37_ejercicio2:
    def vide37_ejer2(self):
        ### Ejercicio 2
        print("""\nEscribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 
strings. Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. Ejemplo: 
"r":5
"%":3
"a":8
"9":1.

¿Cómo se podrían informar las ocurrencias de las letras del alfabeto únicamente, incluyendo el valor 0 para las letras que no aparecieron?\n""")

        contadores={}
        for i in range(50):
            cadena=input("Cadena de caracteres: ")
            for caracter in cadena:
                if caracter not in contadores:
                    contadores[caracter]=1
                else:
                    contadores[caracter]+=1
        print("Frecuencia de cada carácter")
        for caracter, cantidad in contadores.items():
            print(caracter, ": ", cantidad)     #</code></pre>
resul37_2=Video37_ejercicio2()
resul37_2.vide37_ejer2()
os.system('cls')

## Para contabilizar sólo letras (mayúsculas y minúsculas por separado):
# contadores={}
# alfabeto="abcdefghijklmnñopqrstuvwxyz"
# for letra in alfabeto+alfabeto.upper():  ### un nuevo string convertido a mayúscula y como valor 0
#     contadores[letra]=0
# for i in range(3):
#     cadena=input("Cadena de caracteres: ")
#     for caracter in cadena:
#         if caracter.lower() in alfabeto:   ### "e" in alfabeto ===> True
#             contadores[caracter]+=1        
# print("Frecuencia de cada letra")
# for caracter, cantidad in contadores.items():
#     print(caracter, ": ", cantidad)


class Video37_ejercicio3:
    def vide37_ejer3(self):
        ### ejercicio 3
        print("""\nSuponer un diccionario con pacientes atendidos en un hospital, con el siguiente formato: 
-Clave: DNI (int). 
-Valor: lista con los datos en el siguiente orden: nombre (str), edad (int), si ya ha sido 
atendido previamente (bool), código de su médico de cabecera (int).

1) Qué representa el dato que retorna la siguiente función, si el parámetro es el diccionario?
def funcion1(pacientes):
    e=0
    t=0 
    for datos in pacientes.values(): 
        if datos[2]:
            e+=datos[1]
            t+=1 
    if t>0:
        return e/t 
    else:
        return 0

2) Suponer también una lista compuesta por tuplas que contienen: código y nombre de cada médico. La 
siguiente función recibe el diccionario, la lista y el dni de un paciente. ¿Qué representa el dato retornado?

def funcion2(pacientes, medicos, dni): 
    for medico in medicos: 
        if medico[0]==pacientes[dni][3]:
            return medico[1] 
    return ""\n""")

        def funcion1(pacientes):
            e=0
            t=0 
            for datos in pacientes.values(): 
                if datos[2]:
                    e+=datos[1]
                    t+=1 
            if t>0:
                return e/t 
            else:
                return 0
        a={10267489:["Martha Ramos",68,True,829], 22819922:["Lucas Pérez",47, False,437], 40526671:["Facundo Lucero",29, True,829]}
        print("1) Retorna la edad promedio de los pacientes que han sido atendidos alguna vez: ",funcion1(a))


        def funcion2(pacientes, medicos, dni): 
            for medico in medicos: 
                if medico[0]==pacientes[dni][3]:
                    return medico[1] 
            return ""
        b={10267489:["Martha Ramos",68,True,829], 22819922:["Lucas Pérez",47, False,437], 40526671:["Facundo Lucero",29, True,829]}
        c={(829,"Gabriela Ríos"), (437,"Pedro Calle"),(561,"Soledad Fuentes")}
        x=22819922
        print("2) Retorna el nombre del médico de cabecera del paciente cuyo DNI recibe por parámetro: ",funcion2(b,c,x))
resul37_3=Video37_ejercicio3()
resul37_3.vide37_ejer3()
os.system('cls')


##############! video 38
class Video38_ejercicio1:
    def vide38_ejer1(self):
        ### Ejercicio 1
        print("""\nCrear un programa para gestionar datos de los socios de un club, permitiendo:

-Cargar información de los socios en un diccionario para acceder por número de socio. Los datos a almacenar son: número, nombre 
y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n). El programa debe iniciar con los datos de los socios fundadores ya cargados:
Socio nº1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
Socio nº2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
Socio nº3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
-Informar cantidad de socios del club.
-Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
-Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad ingresaron el 14/03/2018.
-Solicitar el nombre y apellido de un socio y darlo de baja (eliminarlo del listado).
-Imprimir el listado de socios completo.\n""")

        def cargarSocios(socios):
            numero=int(input("Número de socio (0 para cortar): "))
            while numero!=0:
                nombre=input("Nombre y apellido: ")
                fecha=input("Fecha de ingreso (DDMMAAAA): ")
                cuota=input("¿Cuota al día? s/n: ")
                socios[numero]=[nombre,fecha,cuota.lower()=="s"]
                numero=int(input("Número de socio (0 para cortar): "))
            return socios

        def modificarFecha(socios, fecha_anterior, fecha_nueva):
            for datos in socios.values():
                if datos[1]==fecha_anterior:
                    datos[1]=fecha_nueva
            return socios

        def numeroSocio(socios, nombre):
            for numero,datos in socios.items():
                if datos[0].lower()==nombre.lower():
                    return numero
            return 0

        def formatoFecha(fecha):
            return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]

        def imprimirListado(socios):
            for numero,datos in socios.items():
                print("-Número:",numero)
                print("-Nombre:",datos[0])
                print("-Fecha de ingreso:", formatoFecha(datos[1]))
                if datos[2]:
                    print("-Cuota al día")
                else:
                    print("-En deuda")
                print("-----------------------")


        socios_activos={1:["Amanda Núñez","17032009",True], 2:["Bárbara Molina","17032009",True], 3:["Lautaro Campos","17032009",True]}

        print("***Cargar socios")
        socios_activos=cargarSocios(socios_activos)

        print("El club tiene", len(socios_activos), "socios")

        print("***Registrar pago de cuotas")
        numero=int(input("Número de socio: "))
        socios_activos[numero][2]=True     ### un contenedor dentro de otro
        ### esto es una lista
        ### dato bool

        print("***Modificando fecha de ingreso...")
        socios_activos=modificarFecha(socios_activos, "13032018", "14032018")   ### podré modificar cualquier fecha

        print("***Eliminar socio")
        nombre=input("Nombre y apellido: ")
        numero=numeroSocio(socios_activos, nombre)
        if numero in socios_activos:
            del socios_activos[numero]     ### necesito una clave para poder borrar

        imprimirListado(socios_activos)
resul38_1=Video38_ejercicio1()
resul38_1.vide38_ejer1()
os.system('cls')

##############! video 39 ###\n
##                         ?Errores comunes con estructuras de datos
## concatenar una lista con un dato de otro tipo
class Video39_ejercicio1:
    def vide39_ejer1(self):
        lista=[1,2,3,4]
        ##lista=lista+5     ## nos dará error

        lista=lista+[5]   ##concatenamos y la lista tendra un valor adicional
        print(lista)

        otra=[9,8,7]

        lista=lista+otra   ### ponemos una lista dentro de otra
        print(lista)

        a=lista+[otra]  ## contiene la lista anterior más "otra"
        print(a)

        ##                 errores comunes con estructura de datos
        ## imprimir una estructura directamente, sin iterar
        ## lista=[1,2,3]
        ## print(lista)

        ## 1
        lista=[1,2,3]
        ### print(lista)  ## esto no#
        for i in lista: ##primero iterar
            print("Números: ",i)

        ## 2
        articulos={154:["jabón en polvo","limpieza", True],
                    248:["talco", "cosmética", False],
                    199:["cera para pisos","limpieza", True]} ##diccionario
        ### print (articulos)  ## este print no
        for clave,valor in articulos.items():   ## iterar    3manera correcta
            print("Código: ",clave)
            print("Descripción: ",valor[0])
            print("Rubro",valor[1])
            if valor[2]:
                print("Hay stock")
            else:
                print("Agotado")
            print("---------------")

        # 3
        # for clave, valor in articulos.items():   ### no nos da error, pero esta no es la manera correcta
        #     print(clave, valor)



        ##                  Errores comunes con estructuras de datos
        ## Modificar la cantidad de elementos de la estructura que se está iterando
        ## ejemplo 1
        # a=[1,2,3,4]
        # for i in range(len(a)):   ## evitar modificar los elementos de una estructura que se esta iterando
        #     if i==2:
        #         del a[3]
        #     print (a[i])   ## nos da error en uno de los elementos, cuando va a imprimir el 4


        ## ejemplo 2
        # mal
        # b={"a": [1,2,3], "b":[], "c": [8,6], "d":[], "e":[4]}
        # for clave in b.keys(): ### nos da error porque hemos cambiado el tamaño del diccionario durante la iteración
        #     if b[clave]==[]:
        #         del b[clave]

        # bien
        b={"a": [1,2,3], "b":[], "c": [8,6], "d":[], "e":[4]}
        claves=list(b.keys())
        for clave in claves:    ## ni agregango ni eliminando 
            if b[clave]==[]:
                del b[clave]
        print(b)
resul39_1=Video39_ejercicio1()
resul39_1.vide39_ejer1()
os.system('cls')