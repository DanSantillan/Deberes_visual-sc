### NOMBRE: DANIEL FELICIANO SANTILLAN ALFONSO
### DEBER 1
### CURSO: 3ER SEMESTRE-SOFTWARE-MAÑANA

######### Tipos de datos y acciones elementales
###########################################################
###########################################################

#### ejercicio 3
### no se ve las expresiones matemáticas
#### ejercicio 4

# Dados dos (2) números calcule 
# la suma, resta, multiplicación, división y módulo.

class Calcular:
    def calcular_var(self):
        a= int (input("Ingrese un número:"))
        b= int(input("Ingrese otro número:"))

        sum=(print("La suma es:",a + b))
        res= (print("La resta es: ", a-b))
        multi= (print("La multiplicación es: ", a*b))
        dvs= print("La división es: ", a/b)
        modulo= print("El módulo es: ", a%b)
calcular=Calcular()
calcular.calcular_var()

#### ejercicio 5

# Dados tres (3) números, 
# Hacer una aplicación que calcule la resolvente.

class Resolvente:
    def calcular_res(self):
        print("Forma genérica de la cuación = ax^2 + bx + c = 0")
        a=int(input("ingrese un número para a: "))
        b=int(input("ingrese un número para b: "))
        c=int(input("ingrese un número para c: "))

        if a!=0:
            x1=(-b+(((b**2)-(4*a*c))**0.5))/(2*a)
            x2=(-b-(((b**2)-(4*a*c))**0.5))/(2*a)
            print("El valor de x1 es: ","{:.2f}".format(x1))
            print("El valor de x2 es: ","{:.2f}".format(x2))
        if a==0:
            print("Error, no puede valer 0")
resolvente=Resolvente()
resolvente.calcular_res()

################## ejercicio 6               ### sqrt=modulo para calcular la raiz cuadrada

# Dados dos (2) lados de un triángulo en cm, calcular la hipotenusa del mismo.

from math import sqrt
class Hipotenusa:
    def cal_hipo(self):
        cate1= float(input("Ingrese el cateto 1: "))
        cate2= float(input("Ingrese el cateto 2: "))

        hipotenusa= sqrt(cate1**2 + cate2**2)
        print("La hipotenusa es: ", (format(hipotenusa,'.2f')) )
calcular_hipo=Hipotenusa()
calcular_hipo.cal_hipo()

################## ejercicio 7

#Dado un (1) número, imprimir 0 si es par y 1 si es impar.

class Numero_par_impar:
    def calcular_par_impar (self):
        a= int(input("Ingrese un número: "))
        if a%2==0:
            print("0")
        else:
            print("1")
resultado=Numero_par_impar()
resultado.calcular_par_impar()

###a%2==0  = divir el numero entre 2 y sacando el residuo de la division y si el residuo es igual a
### o entonces es par

################# ejercicio 9  ###### si ingresa mas de 4 digitos imprimira que es par :(

#Dado un (1) número binario de cuatro (4) dígitos imprimir su bit da paridad.
#El bit de paridad es 1 si el número de bits 1 es impar y 0 en caso contrario.

class Paridad:
    def cal_binario(self):        
        num=(input("Ingrese un número binario de 4 dígitos: "))
        convert= int(num,base=2)
        print(convert)

        a=int(num[0])
        b=int(num[1])
        c=int(num[2])
        d=int(num[3])

        suma=(a+b+c+d)
        if int(suma)%2==0:
            print("Bit de paridad par.")
        elif int(suma==1):
            print("Bit de paridad impar.")
        else:
            print("Bit de paridad impar.")
paridad_bin= Paridad()
paridad_bin.cal_binario()

################# ejercicio 10

#Dado un (1) número binario de cuatro (4) dígitos imprimir su valor.

class Valor_bina:
    def valor_binario(self):       
        num= (input("Ingrese un número binario de 4 dígitos : "))
        ente= int(num,base=2)
        print(ente)
valor= Valor_bina()
valor.valor_binario()

################ ejercicio11

# Dado un (1) número de cuatro (4) dígitos imprimirlo por 
# separado en unidades, decenas, centenas y unidades de mil.
# Entrada:
# 1234
# Salida:
# Unidades: 4
# Decenas: 3
# Centenas: 2
# Unidades de mil: 1

class Separar_u_s_c_m:
    def u_d_c_m(self):
        num = int (input ("Ingresa un número entero de 4 dígitos: "))
        while num>=10000 or num<=999:
            print("Error, ingrese un número de 4 dígitos, ejm=9999")
            num= int(input("Ingresa un número entero de 4 dígitos: "))
        unidad=num%10
        decena=(num%100-num%10)//10
        centena=(num%1000-num%100)//100
        mil=(num%10000-num%1000)//1000
        if (centena+unidad)%2==0:
            resultado=mil*4-decena*3+centena*2-unidad
        else:
            resultado=decena//2+centena*3-unidad//5
        print ("Unidad: " + repr (unidad))
        print ("Decena: " + repr (decena))
        print ("Centena: " + repr (centena))
        print ("Unidad en mil: " + repr(mil))
valor_dar=Separar_u_s_c_m()
valor_dar.u_d_c_m()

###########################################################
###########################################################
######### Estructuras de control de flujo de datos #######
###########################################################
###########################################################
###########################################################

################ ejercicio1

# # # ttodos los años que se dividen exactamente entre 400, o que son divisibles
# # # exactamente entre 4 y no son divisibles exactamente entre 100 son años bisiestos.
# # # Usando estas premisas crea un algoritmo que lea una fecha como un número entero
# # #  con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si el mismo es un año bisiesto o no.


class Año_bisiesto:
    def verificar_año(self):
        print("Ingrese una fecha para verificar si es un año bisiesto.")
        print("Primero ingrese el día, despúes el mes y por ultimo el año(31/8/2020).")
        print("_______________________________________")
        dia = int(input("Ingrese el día: "))
        while dia>=32 or dia<=0:
            print("Error tiene que estar entre 1-31")
            dia=int(input("Ingrese el día: "))

        mes=int(input("Ingrese el mes: "))
        while mes>=13 or mes<=0:
            print("Error tiene que estar entre 1-12: ")
            mes=int(input("Ingrese el mes: "))

        año= int(input("Ingrese el año: "))
        print(dia,"/",mes,"/", año)
        if año % 4==0:
            print("El año",año, "es bisiesto.")
        elif año % 100==0:
            print("El año",año, "no es bisiesto.")
        elif año % 400==0:
            print("El año ",año," no es bisiesto.")
        else:
            print("El año",año," no es bisiesto.")
año_bis= Año_bisiesto()
año_bis.verificar_año()

######ejercicio 2         [::-1] sig= leer de izquierda a derecha    %i tal numero

##Dado un número entero cuya cantidad de dígitos es igual a 5, determine si es capicúa.
##Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás.

class Capicúa:
    def numero_cap(self):
        numero=int(input("Ingrese un número positivo y máximo de 5 dígitos:"))
        while numero>=100000 or numero<=0:
            print("Error, máximo 5 dígitos: ")
            numero=int(input("Ingrese un número máximo de 5 dígitos:"))

        if numero>=0:
            if str(numero)==str(numero)[::-1]:
                print("%i es capicúa."% numero)
            else:
                print("%i no es capicúa."% numero)
resp_capicua= Capicúa()
resp_capicua.numero_cap()

############ ejercicio 3

## Cree un algoritmo que tome por entrada las horas y minutos de un día 
## y dé como resultado su equivalente en segundos.

class Cal_segundos:
    def segundos(self):
        horas= int(input("Ingrese las horas: "))
        minutos=int(input("Ingrese los minutos: "))

        hor= 60*horas*60
        segu= hor
        minutos= 60*minutos
        segun= minutos
        suma=segu+segun

        print("los segundos son: ",suma)
calcular_seg= Cal_segundos()
calcular_seg.segundos()

############ ejercicio4

## Para un valor entero positivo que representa una cantidad en 
## segundos, indicar su equivalente en minutos, horas y días.

class Segundos:
    def calcular_seg(self):
        segundos=int(input("Ingrese los segundos: "))
        dias= segundos // (24*60*60)
        segundos= segundos% (24*60*60)
        horas= segundos// (60*60)
        segundos= segundos% (60*60)
        minutos= segundos// 60
        segundos=segundos%60

        print(dias,"días//",horas,"horas//",minutos,"minutos.")
segundoss= Segundos()
segundoss.calcular_seg()

################ ejercicio5

# Dados tres números enteros positivos A, B y C, determine 
# ¿cuál de ellos es el mayor? y ¿cuál es el segundo mayor?

class Mayor_2m:
    def mayor_2(self):
        print("____Ingrese 3 números____")
        print("_________________________")

        a= int(input("Número 1: "))
        b= int(input("Número 2: "))
        c= int(input("Número 3: "))

        if a>b and a>c:
            print("El mayor es: ",a)
        elif b>a and b>c:
            print("El mayor es: ",b)
        elif c>a and c>b:
            print("El mayor es: ",c)
        else:
            print("Números iguales")

        d = [a, b, c ]
        print( "El segundo mayor es:",sorted(set(d), key=int, reverse=True)[1])
num_mayor=Mayor_2m()
num_mayor.mayor_2()


# #sorted= devuelve una lista de forma ordenada
# # ordena los elementos de un iterable y lo devuelve como un lista
# #tiene 3 parametros= iterable= secuencia(cadena,tupla,lista).coleccion(conjunto,diccionario)o cualquier
# #otro iterador.
# #reverse(opcional)=si true, la lista ordenada se invierte(o se ordena de forma descendente)
# # predeterminado false si no se porporciona
# # clave=una funcion que sirve para la comparacion de clasificacion, por defecto none
# #
# #set= se utilizan para almacenar varios elementos en una sola variable set es un dato integrado
# # como list tuple diccionario
# # keys= devuelve un objeto de vista que muestra una lista de todas las claves

############# ejercicio #6

# En un estacionamiento el monto a pagar se calcula multiplicando el número de horas que permaneció el 
# automóvil dentro del estacionamiento por Bs. 4 y se incrementa esta cantidad en Bs. 2,50 por cada media hora adicional.
# Ahora se desea que usted elabore un algoritmo que a partir de la hora de entrada y la hora de salida de 
# un vehículo (las mismas corresponden a un mismo día) calcule el monto a pagar por el dueño del vehículo.
# La entrada vendrá dada por dos enteros positivos el primero representa las horas y el segundo los minutos, 
# además por último se debe leer un carácter (A o P) que indica si la hora es AM o PM.

from datetime import date, datetime, time, timedelta
class Pagar_estacionamiento:
    def pagar_e(self):
        cada_hora=4
        pas_30min=2.50

        print("Cobro de estacionamiento.")
        print("\nPrimero ingrese la hora y después los minutos.")
        entrada=int(input("Hora de entrada: "))
        while entrada>24 or entrada<0:
            print("Error, el día solo tiene 24 horas.")
            entrada=int(input("Hora de entrada: "))
        min_entr=int(input("Minutos: "))
        while min_entr>60 or min_entr<0:
            print("Error: ")
            min_entr=int(input("Minuto: "))
        def tiempo(num1):
            if entrada<12:
                return("AM")
            else:
                return("PM")
        num1=entrada
        print("Entró a las",entrada,":",min_entr,tiempo(num1))

        dato1= timedelta(hours=entrada, minutes=min_entr)


        salida=int(input("Hora de salida: "))
        while salida>24 or salida<0:
            print("Error, el día solo tiene 24 horas.")
            salida=int(input("Hora de salida: "))
        min_salida=int(input("Minutos: "))
        while min_salida>60 or min_salida<0:
            print("Error: ")
            min_salida=int(input("Minuto: "))
        def tiempo(num2):
            if salida<12:
                return("AM")
            else:
                return("PM")
        num2=salida
        print("Salió a las",salida,":",min_salida,tiempo(num2))

        ###### algo no esta bien
        horas_extras=float(input("Ingrese las minutos extras que dejo el outomóvil: "))
        hor_ex= (horas_extras/30)*pas_30min

        dato2= timedelta(hours=salida, minutes=min_salida)
        res= (dato2- dato1) ### no es lo que esperaba
        total= (res*cada_hora)

        print("\nEjemplo: los dos primeros números (11:00:00) representa la cantidad en dolar. ")
        print("Ejemplo: los dos números en medio(00:11:00) representa la cantidad en centavos. ")
        print("\nTotal a pagar: $",total)
        print("\nTotal a pagar por horas extras: $", round(hor_ex,2))

total_estaci=Pagar_estacionamiento()
total_estaci.pagar_e()


##############ejercicio 7

# El IMC resulta de la división de la masa del individuo (en kilogramos) entre 
#el cuadrado de la estatura (en metros). El índice de masa corporal es un 
#indicador del peso de una persona en relación con su altura.
# Clasificación del IMC de acuerdo con la OMS de la ONU:
# a. Menor a 16: Criterio de ingreso.
# b. 16 a 16.9: infra peso.
# c. 17 a 18.4: bajo peso.
# d. 18.5 a 24.9: peso normal.
# e. 25 a 29.9: sobrepeso.
# f. 30 a 34.9: obesidad pre-mórbida.
# g. 40 a 45: obesidad mórbida.
# h. Mayor a 45: obesidad híper-mórbida.
# Dado el peso de una persona en libras (1 libra = 0,453592 Kg) y su estatura en 
#centímetros, calcule su IMC e indique como salida el peso en kilogramos, el valor
# de IMC de la persona y la categoría en la cual fue clasificado.

class Imc:
    def cal_imc(self):
        print("""Clasificación del IMC de acuerdo con la OMS de la ONU:
        a. Menor a 16: Criterio de ingreso.
        b. 16 a 16.9: infra peso.
        c. 17 a 18.4: bajo peso.
        d. 18.5 a 24.9: peso normal.
        e. 25 a 29.9: sobrepeso.
        f. 30 a 34.9: obesidad pre-mórbida.
        g. 40 a 45: obesidad mórbida.
        h. Mayor a 45: obesidad híper-mórbida.""")
        print("")
        peso=float(input("Ingrese su peso en libras: "))
        kilog=peso*0.453592
        estatura=float(input("Ingrese su estatura en centímetros: "))
        metro= estatura/100
        imc=float(kilog/metro**2)
        print("Su peso es de: ",format(kilog,"0.2f"),"Kg")
        print("Su IMC es de:", format(imc, "0.2f"))
        print("Usted pertenece al grupo: ")
        if imc<16:
            print("A. Criterio de ingreso")
        elif 16<=imc and imc<16.9:
            print("B. Infra peso")
        elif 17<imc and imc<18.4:
            print("C. Bajo peso")
        elif 18.5<imc and imc<24.9:
            print("D. Peso normal")
        elif 25<imc and imc<29.9:
            print("E. Sobrepeso")
        elif 30<imc and imc<39.9:
            print("F. Obesidad pre-mórbida")
        elif 40<imc and imc<45:
            print("G. Obesidad mórbida")
        else:
            print("H. Obesidad híper-mórbida")
indice_mc= Imc()
indice_mc.cal_imc()

##############   ejercicio 8

# Escriba un algoritmo que reciba una fecha (día y mes) 
# correspondiente al año 2014 e imprima por pantalla el número de días que han 
# pasado desde el 1 de Enero de 2014 hasta la fecha dada.

from datetime import date
class Dias_pas:
    def dias(self):
        print("Dias que ha pasado delde el 2014/01/01")
        mes=int((input("Ingrese el mes: ")))
        dia=int((input("Ingrese el día: ")))

        fecha=date(2014,1,1)
        fecha2=date(2014,mes,dia)
        resta=fecha2-fecha
        print("Ha pasado",resta.days,"días.")
dias_paso=Dias_pas()
dias_paso.dias()

############## ejercicio 9

# Solicitar un número entre el 1 y el 12 e 
#imprimir el mes correspondiente a dicho número.

class Calendario:
    def mes(self):
        print("Ingrese un número para ver el mes correspondiente")
        año=int(input("Escriba un numero del 1 al 12: "))
        if año<=1:
            print("Enero")
        elif 2<=año and año<3:
            print("Febrero")
        elif 3<=año and año<4:
            print("Marzo")
        elif 4<=año and año<5:
            print("Abril")
        elif 5<=año and año<6:
            print("Mayo")
        elif 6<=año and año<7:
            print("Junio")
        elif 7<=año and año<8:
            print("Julio")
        elif 8<=año and año<9:
            print("Agosto")
        elif 9<=año and año<10:
            print("Septiembre")
        elif 10<=año and año<11:
            print("Octubre")
        elif 11<=año and año<12:
            print("Noviembre")
        elif año<13:
            print("Diciembre")
        else:
            print("Errorrrr")
validar_mes=Calendario()
validar_mes.mes()

#############  ejercicio 10

# En un almacén se hace un 20% de descuento a los clientes cuya compra supere los Bs 1000, se 
# desea que realice un algoritmo el cual tome por entrada el monto a pagar por el cliente y 
# arroje como salida el monto aplicando el descuento de ser necesario.

class Descuento:
    def validar_des(self):     
        descuento= 0.20
        monto_pagar=float(input("Monto a pagar: $"))

        if monto_pagar>1000:
            a=monto_pagar*descuento
            b= monto_pagar-a
            print("Se le aplico un descuesto del 20%, precio final a pagar: $",format(b,"0.2f"))
        else:
            print("Precio a pagar: $",monto_pagar)
var_descuento= Descuento()
var_descuento.validar_des()

###########################################################
###########################################################
###########    Estructuras Iterativas        ##############
###########################################################
###########################################################
###########################################################

######### ejercicio 1

# Dado un número entero N, calcular e informar al usuario cuántos dígitos tiene dicho número.

class Num_digito:
    def digitos(self):
        print("Caclcular el número de dígitos")
        numero= int(input("Ingrese un número: "))
        contador= len(str(numero))
        print("El número ingresado tiene %s dígitos" %(contador))
contar_digitos= Num_digito()
contar_digitos.digitos()

######### ejercicio 2

# Dado un número, determine si es capicúa.
# Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás.

class Nu_capi:
    def capi(self):
        print("Determinar si el número es capicúa.")
        numero=int(input("Ingrese un número positivo: "))
        if numero>=0:
            if str(numero)==str(numero)[::-1]:
                print("Es capicúa.")
            else:
                print("No es capicúa.")
nu_capicua= Nu_capi()
nu_capicua.capi()

######## ejercicio 3

# Dado un número N determinar si es un número primo.
# Nota: Un número primo es aquel que solo es divisible por 1(uno) y por el mismo.

#### rango= inmutable
#### %modulo= si al dividir es igual a 0

class Num_primo:
    def primo(self):
        numero=int(input("Ingrese un número: "))
        primo=True
        for i in range(2, numero):
            if numero% i==0:
                primo=False
        if primo:
            print("Es número primo")
        else:
            print("No es número primero")
prim_num= Num_primo()
prim_num.primo()

####### ejercicio 4

## Construya un programa que dado un valor entero
## N, haga el cálculo de la función factorial utilizando estructuras iterativas.

class Factorial:
    def num_fac(self):
        print("Calcular el factorial")
        numero= int(input("Ingrese un número: "))
        factorial=1
        for i in range(1,numero+1):
            factorial*=i
        print("El factorial de",numero,"es: ", factorial)
facto=Factorial()
facto.num_fac()

########### ejercicio 5

# Dado un número entero N que representa una contraseña y asumiendo que una 
# contraseña debe tener al menos 10 dígitos para ser segura, 
# determine si la contraseña ingresada por el usuario es correcta, de no serlo debe 
# pedirla nuevamente hasta que tenga los 10 (diez) dígitos solicitados y al ser 
# correcta mostrar un mensaje de éxito al usuario, por salida estándar.

class Contraseña:
    def validar_contra(self):
        print("Su contraseña debe de tener 10 dígitos(números enteros) para ser segura.")
        contra= int(input("Ingrese una contraseña: "))

        while contra<1000000000:
            print("Contraseña insegura, tiene que tener al menos 10 dígitos.")
            contra= int(input("Ingrese una contraseña: "))
        print("Contraseña segura.")
contra= Contraseña()
contra.validar_contra()

############ ejercicio 6

# Dada una secuencia de números terminada en cero (0), elaborar un 
# algoritmo que informe al usuario qué valor tiene el número 
# mayor y qué valor tiene el número menor, sin contar el cero (0).

class Mayor_menor:
    def numero_m_m(self):
        numero=(input("Ingrese un núnemo:"))
        resp= sorted([int(n)for n in list(numero)])

        validar=min(filter(lambda x:x>0,resp))
        print("mayor", max(resp))
        print("menor", validar)
resultado=Mayor_menor()
resultado.numero_m_m()


##sorted:::: ordena los numeros de menor a mayor 

###filter():::: función extrae elementos de un iterable 
###(lista, tupla, etc.) para los que devuelve una función True.
# toma dos argumentos:
# función - una función
# iterable : un iterable como conjuntos , listas , tuplas , etc.
### VALOR DE RETORNO: puede convertir fácilmente iteradores en secuencias 
#### como listas, tuplas, cadenas, etc.

##lambda::::Sin embargo, existe una forma más rápida de escribir funciones sobre la marcha, 
## y se denominan lambdafunciones porque utiliza la palabra clave lambda.
#### Las expresiones lambda en Python son una forma corta de declarar funciones 
#### pequeñas y anónimas (no es necesario proporcionar un nombre para las funciones lambda). 

################ Ejercicio 7

# Se tiene una secuencia de enteros terminada en cero, que corresponde a la edad, 
# peso y estatura de una muestra de hombres y mujeres mayores de 18 años. Con base 
# en dicha secuencia se desea realizar un estudio a fin de conocer:
# •	Edad promedio de todas las personas en la muestra.
# •	Peso promedio de todas las personas en la muestra.
# •	Estatura promedio de todas las personas en la muestra.
# •	Cuántas personas hay con edad entre los 18 y 25 años.
# •	Cuántas personas son mayores a 36 años.
# •	Cuál es el promedio de peso de las personas con edades entre 18 y 35 años.

class Calcular_epe:
    def epe(self):
        print("Digite 0 cuando ya no desee ingresar más datos.")
        print("Edad=0; Peso=0; Altura=0.\n")
        print("Recuerde que son edades mayores o iguales a 18.")

        contar_edad=0
        contar36=0
        contar18_25=[]
        contador=-1
        suma=0
        edad=1

        contador1=-1
        suma1=0
        peso=1

        contador2=-1
        suma2=0
        altura=1
        while edad!=0:
            edad=int(input("Ingrese la edad: "))
            suma+=edad
            contador+=1
            contar18_25.append(edad)
            if edad <=25 and edad>=18:
                contar_edad+=1      
            if edad>=36:
                contar36+=1
                
            if edad<=17 and edad>=1:
                print("Error, tiene que ser mayor de 18 años.\n")
                contador=-1
                suma=0
                edad=1
                contar18_25.append(edad)
                if edad<=25 and edad>=18:
                    contar_edad+=1
                if edad>=36:
                    contar36+=1

            peso=float(input("Ingrese el peso en kilogramo: "))
            suma1+=peso
            contador1+=1
            if peso<=17 and peso>=1:
                print("Error, no puede pesar menos de 17kg.\n")
                contador1=-1
                suma1=0
                peso=1

            altura=float(input("Ingrese la altura en metros: "))
            suma2+=altura
            contador2+=1
            if altura>=2.10:
                print("Error, no puede medir más de 2.10m .\n")
                contador2=-1
                suma2=0
                altura=1
            
        prom_edad=suma/contador
        prom_peso=suma1/contador1
        prom_altura=suma2/contador2
        print("\n")
        print("La edad promedio es:",round (prom_edad,0))
        print("El peso promedio es: ",round(prom_peso,2))
        print("La altura promedio es: ",round(prom_altura,2))
        print("Las peronas entre 18 y 25 años son: ",contar_edad)
        print("Las personas mayores de 36 años son: ", contar36)

        ##### el ultimo punto no sabia como hacerlo :(  
resultado_epe=Calcular_epe()
resultado_epe.epe()



############# ejercicio #8

# Construye un algoritmo que calcule e imprima la tabla de multiplicar, desde la tabla del 1 hasta la del 10.

class Tabla:
    def multiplicar(self):
        for i in range(1,14):
            mult= i* 1
            print("1","x",i,"=",mult)
        print("\n")
        for i in range(1,14):
            mult= i* 2
            print("2","x",i,"=",mult)
        print("\n")
        for i in range(1,14):
            mult= i* 3
            print("3","x",i,"=",mult)
        print("\n")
        for i in range(1,14):
            mult= i* 4
            print("4","x",i,"=",mult)
        print("\n")
        for i in range(1,14):
            mult= i* 5
            print("5","x",i,"=",mult)
        print("\n")
        for i in range(1,14):
            mult= i* 6
            print("6","x",i,"=",mult)
        print("\n")
        for i in range(1,14):
            mult= i* 7
            print("7","x",i,"=",mult)
        print("\n")
        for i in range(1,14):
            mult= i* 8
            print("8","x",i,"=",mult)
        print("\n")
        for i in range(1,14):
            mult= i* 9
            print("9","x",i,"=",mult)
        print("\n")
        for i in range(1,14):
            mult= i* 10
            print("10","x",i,"=",mult)
multi= Tabla()
multi.multiplicar()

############################## ejercicio 9

## Escribir un algoritmo que muestre todas las fichas de dominó, sin repetir.

class Dominó:
    def fichas(self):
        for aba in range(0,7):
            for arri in range(0,aba+1):
                print(arri,"|",aba,"\n")
muestra=Dominó()
muestra.fichas()

########################### ejercicio 10

#  Dados N número positivos (N>1) calcular el promedio 
#  de esta serie. Considere que la serie termina al leer un 0.

class Promedio:
    def serie(self):      
        print("Digite 0 cuando ya no desee ingresar más números.")
        contador= -1
        suma= 0
        num=1
        while num!=0:
            num= float(input("Ingrese un número: "))
            suma+=num
            contador+=1

        promedio= suma/contador
        print("El promedio es: ", format(promedio,"0.2f"))
serie_pro=Promedio()
serie_pro.serie()


###################################################################
############### Procedimientos (Acciones y Funciones) #############
###################################################################
###################################################################
###################################################################


#################### Ejercicio 1

# Construya una función que solicite edades al usuario y 
# determine el promedio de las edades mayores a 18 años. 
# El usuario indicará cuando desea dejar de suministrar datos de 
# entrada. En la Acción Principal se informará el promedio calculado.

class calcular_edad:
    def edad(self):
        print("Digite 0 cuando ya no desee ingresar más datos.")
        print("Recuerde que son edades mayores o iguales a 18.")
        contador=-1
        suma=0
        edad=1
        while edad!=0:
            edad=int(input("ingrese la edad: "))
            suma+=edad
            contador+=1     
            if edad<=17 and edad>=1:
                print("Error, tiene que ser mayor de 18 años.\n")
                contador=-1
                suma=0
                edad=1
        prom_edad=suma/contador
        print("La edad promedio es:",round (prom_edad,0))
edad_18=calcular_edad()
edad_18.edad()


############# ejercicio #2

# Construya una función “Eleva” Que reciba como parámetros una base y un exponente
# y retorne al algoritmo principal el resultado de elevar un numero al otro.

class Elevar:
    def expo(self):
        def Eleva(base,expo):
            resultado=base**expo
            return resultado
        a= int(input("Ingrese un número para la base: "))
        b= int(input("Ingrese un número para el exponente: "))
        print ("Resultado: ",Eleva(a,b))
result=Elevar()
result.expo()

############ ejercicio 3

# Escriba una función que calcule el perímetro del pentágono 
# (siendo el perímetro la suma de los lados del polígono).

##### en caso de que un lado no sea igual

class Perimetro:
    def suma(self):
        def perimetro(a,b,c,d,e):
            resultado= a+b+c+d+e
            return resultado
        a= int(input("Ingrese el lado 1: "))
        b= int(input("Ingrese el lado 2: "))
        c= int(input("Ingrese el lado 3: "))
        d= int(input("Ingrese el lado 4: "))
        e= int(input("Ingrese el lado 5: "))
        print ("El perímetro es: ",perimetro(a,b,c,d,e))
suma_lado=Perimetro()
suma_lado.suma()

################## si todos los lados son iguales

# class Perimetro2:
#     def sum(self):     
#         def perimetro(a):
#             resultado= a*5
#             return resultado
#         a= int(input("Ingrese el lado del Pentágono: "))
#         print ("El perímetro es: ",perimetro(a))
# sum_lado=Perimetro2()
# sum_lado.sum()

##################### ejercicio 4

# En una empresa pagan según las horas trabajadas y una tarifa fija por hora. 
# Si la cantidad de horas trabajadas en una semana es mayor
#  a 40, la tarifa se incrementa en un 35% para las horas extras. Escribe una acción 
# principal que solicite la identificación de 5 empleados, el monto cancelado por 
# hora, y la cantidad de horas trabajadas por cada uno, llame a acciones/funciones que 
# calculen el salario semanal por horas trabajadas (<=40) y los ingresos por concepto de 
# horas extras, y finalmente informe los resultados en la acción principal.


class pago_de_empresa:
    def pagar(self):
            
        suma=0
        for i in range(5):
            empleado=str(input("Ingrese el nombre de empleado: "))
            monto=float(input("Ingrese el monto a cancelar por hora:$ "))

            print("""\nRecuerde que si hizo horas extras esas se las pedirá más abajo, 
            no las entrevere con las horas trabajadas que son menor a 40""")

            horas_tabajadas=int(input("Ingrese las horas trabajadas: "))
            horas_extras=int(input("Ingrese las horas extras: "))
            tarifa=1.35

            if horas_tabajadas<=40:
                salario_semanal=horas_tabajadas*monto
                horas_ex= horas_extras*tarifa
                total= salario_semanal+horas_ex
                print("Monto a cancelar de la empresa a",empleado,"es de: ",round(total,2))
            else:
                print("Error")
            suma=suma+1
pagar_horas= pago_de_empresa()
pagar_horas.pagar()


##################### ejercicio 5

# Escriba una acción (MillasAKilometros) que convierta una distancia en millas 
# a kilómetros (1milla = 1.60935km). Esta acción recibirá como parámetros: el 
# nombre de la ciudad origen, el nombre de la ciudad destino y la distancia en millas 
# entre ellas y debe retornar la distancia entre las ciudades en kilómetros.
# Desarrolle además una acción principal en donde utilice a 
# la acción MillasAKilometros para convertir e informar la 
# distancia en kilómetros entre 4 pares de ciudades suministradas por el usuario.
# Entrada:
# Cuidad A
# Ciudad B
# 332
# Salida:
# Entre la Ciudad A y la Ciudad B hay 534.30 Km.

class Millas_a_km:
    def kilometro(self):
        MillasAKilometros=1.60935
        ciudad_origen1= input("Ingrese la ciudad de origen: ")
        ciudad_destino1= input("Ingrese la ciudad de destino: ")
        distancia_millas1=int(input("Ingrese la distancia en millas: "))

        ciudad1= round(distancia_millas1*MillasAKilometros,2)

        ciudad_origen2= input("\nIngrese la ciudad de origen: ")
        ciudad_destino2= input("Ingrese la ciudad de destino: ")
        distancia_millas2=int(input("Ingrese la distancia en millas: "))

        ciudad2= round( distancia_millas2*MillasAKilometros,2)
        ciudad_22= ciudad1+ciudad2

        ciudad_origen3= input("\nIngrese la ciudad de origen: ")
        ciudad_destino3= input("Ingrese la ciudad de destino: ")
        distancia_millas3=int(input("Ingrese la distancia en millas: "))

        ciudad3= round( distancia_millas3*MillasAKilometros,2)
        ciudad_33= ciudad_22+ciudad3

        ciudad_origen4= input("\nIngrese la ciudad de origen: ")
        ciudad_destino4= input("Ingrese la ciudad de destino: ")
        distancia_millas4=int(input("Ingrese la distancia en millas: "))

        ciudad4= round( distancia_millas4*MillasAKilometros,2)
        ciudad_44=round (ciudad_33+ciudad4,2)


        print("\nEntre la ciudad de {} y la ciudad de {} hay {} Km".format(ciudad_origen1,ciudad_destino1,ciudad1))
        print("Entre la ciudad de {} y la ciudad de {} hay {} Km".format(ciudad_origen2,ciudad_destino2,ciudad2))
        print("Entre la ciudad de {} y la ciudad de {} hay {} Km".format(ciudad_origen3,ciudad_destino3,ciudad3))
        print("Entre la ciudad de {} y la ciudad de {} hay {} Km".format(ciudad_origen4,ciudad_destino4,ciudad4))

        print("\nLa distancia entre la ciudad de {} y la ciudad de {} hay {} Km".format(ciudad_origen1,ciudad_destino4,ciudad_44))
milla_kilom=Millas_a_km()
milla_kilom.kilometro()


