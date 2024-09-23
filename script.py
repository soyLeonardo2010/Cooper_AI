from datetime import datetime
import pyttsx3
import speech_recognition as sp
import random
import math
import time

class run():
   runn = True
   runner = True
class Day:
   juego = ''
   

   fecha = datetime.today().weekday()
   if fecha == 0:
    juego = str(juego)
    juego = 'piedra papel o tijera'
   elif fecha == 1:
    juego = str(juego)
    juego = 'adivinanzas'
   elif fecha == 2:
    juego = str(juego)
    juego = 'chistes'
   elif fecha == 6:
    juego = str(juego)
    juego = 'char'
   elif fecha == 4:
    juego = str(juego)
    juego = 'tres lineas'
   elif fecha == 5:
    juego = str(juego)
    juego = 'aquineitor'
   elif fecha == 3:
    juego = str(juego)
    juego = 'dia, de jupiter'
    
   fecha = datetime.today().weekday()
   day = fecha
   if fecha == 0:
      day = 'Lunes'
   elif day == 1:
       day = 'Martes'
   elif fecha == 2:
       day = 'Miercoles'
   elif fecha == 3:
      day = 'Jueves'
   elif fecha == 4:
      day = 'Viernes'
   elif fecha == 5:
      day = 'Sabado'
   elif fecha == 6:
      day = 'Domingo'
   
listener = sp.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

name = 'cooper' 

def lisen():
      try:
        with sp.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec1 = listener.recognize_google(voice)
            rec1 = rec1.lower()
            if name in rec1:
               talk(rec1)
               print(rec1)
            else:
              pass
      except UnboundLocalError:
           print("Error en el microfono :(")
      except sp.exceptions.UnknownValueError:
        print("Error en el micrifono :(")
      return rec1
  
def talk(text):
    word = name
    texto = text.replace(word, "")
    engine.say(texto)
    engine.runAndWait()
    
def game_1():
    talk("Bienvenido a el juego de piedra papel y tijera, para que tu jueges, solo di piedra papel o tijera")
    print("ingresa. piedra papel o tijera")
    print()
    puntaje_pc = 0
    puntaje_player = 0
    lista = ['piedra', 'papel', 'tijera']
    while puntaje_pc or puntaje_pc == 0:
        aleatorio = random.choice(lista)
        try:
           jugada_player = input("> ")
        except UnboundLocalError:
            print("Error en el microfono")
            continue
        except sp.exceptions.UnknownValueError:
            print("Error en el microfono")
            continue

        if aleatorio == 'tijera' and jugada_player == 'papel':
           print("punto para la computadora")
           talk("punto para la computadora")
           puntaje_pc += 1
        elif aleatorio == 'piedra' and jugada_player == 'tijera':
            print("punto para la computadora")
            talk("punto para la computadora")
            puntaje_pc += 1
        
        elif aleatorio == 'papel' and jugada_player == 'piedra':
            print("punto para la computadora")
            talk("punto para la computadora")
            puntaje_pc += 1
        
        if jugada_player == 'tijera' and aleatorio == 'papel':
            print("punto para el usuario")
            talk("punto para el usuario")
            puntaje_player += 1
        elif jugada_player == 'piedra' and aleatorio == 'tijera':
            print("punto para el Usuario")
            talk("punto para el usuario")
            puntaje_player += 1
        
        elif jugada_player == 'papel' and aleatorio == 'piedra':
            print("punto para el usuario")
            talk("punto para el usuario")
            puntaje_player += 1
     
        elif jugada_player == aleatorio:
            print("Emapte!")
            talk("Valla, toco un empate")
            
        else:
            talk("No entendi lo que escribiste :(")
            print("Error al decir la opcion :(")
            continue
    
        print()
        print("Usuario: "+ jugada_player)
        print("Cooper: "+ aleatorio)
    
        if puntaje_pc == 3:
            print("Cooper gana!")
            talk("Gane, muy bien jugado usuario, de verdad me diste batalla")
            talk("Para volver a jugar solo di, piedra papel o tijera")
            break
        elif puntaje_player == 3:
            print("El Usuario gana!")
            talk("Felicidades por su victoria usuario, de verdad que eres bueno en esto")
            talk("Para volver a jugar solo di, piedra papel o tijera")
            break
        
def game_2():
    talk("Bienvenido a el juego del ahorcado, para que tu puedas jugar, nesecito que ingreses, la letra que es o que crees que es, y si cres que ya sabes las palabras, solo ingresa la palbra que es, estas listo para jugar?")
    palabra1 = 'microprosesador'
    palabra2 = 'python'
    palabra3 = 'pizza'
    palabra4 = 'balon'
    palabra5 = 'queso'
    palabra6 = 'chulada'


    dibujo = """
            -------
           |  x  x |
           |   --  |
            -------
               |
           ----|----
               |
               /\\
              /  \\
    """
    list_words = [palabra1, palabra2, palabra3, palabra4, palabra5, palabra6]
    word = random.choice(list_words)
    characters = list(word)
    print("la palabra tiene ", len(characters) + 1, "caracteres")
    c = len(characters) + 1
    d = str(c)
    talk("La palbara tiene " + d + 'caracteres')
    print("e inicia  con " + characters[0])
    talk("La palabra inicia con" + characters[0])
    a = '123456'
    for i in a:
        b = (input("la palabra tiene la letra: "))
        if b.lower() == word:
          print("Ganaste!!!")
          talk("Felisidades usuario, has ganado, para volver a jugar solo di, char")
          break
        elif b.lower() in word:
           print("si, tine", b)
           talk("si tiene" + b)
        else:
           print("no tiene", b)
           talk("no tiene " + b)
    else:
       print(dibujo)
       print("Game Over")
       talk("Has perdido, muy bien jugado usuario")
       print("La palabra era", word)
       talk("la palabra era " + word)
       talk("Para volver a jugar, solo di ahorcado, gracias por jugar")
    

def game_3():
    talk("Bienvenido a el juego de las adivianzas, para jugar, yo te dire una pista y tu tienes que tratar de adivinar la palabra, estas listo para jugar")
    print("Para ingresa salir en la consola")
    palabra1 = 'tabla periodica'
    palabra2 = 'tiktok'
    palabra3 = 'pizza'
    palabra4 = 'cuerda'
    palabra5 = 'whattsapp'
    palabra6 = 'gato'
    palabra7 = 'yo'
    
    def adivinanza(mensaje, word):
        print(mensaje)
        talk(mensaje)
        op = '123456'
        for i in op:
            console = (input("que es?: "))
            if console.lower() == word:
                print("Ganaste!")
                talk("Felicidades usuario has ganado")
                break
            else:
                talk('no es' + console)
                print("No es", console)
                
        else:
            print("Game Over")
            talk("Has perdido, muy bine jugado usuario")
            print("La palabra era", word)
            talk("La palabra correcta era" + word)
                
    adivinanza1 = ['es una tabla que representa todos los elementos del universo en un solo papel y se usa en clase de quimica', palabra1]
    adivinanza2 = ['es una plataforma digital echa para ver videos con durasion maxima de 10 minutos', palabra2]
    adivinanza3 = ['es una comida italiana, por seirto la comida favorita del señor leonardo', palabra3]
    adivinanza4 = ['es un objeto, echo con hilos pequeños y sirve para ater cosas, pero se usa prinsipalmente en el ganado', palabra4]
    adivinanza5 = ['es una plataforma de chat muy popular', palabra5]
    adivinanza6 = ['animal favorito de mi creador, es un felino, muy comun', palabra6]
    adivinanza7 = ['es hijo de tus padres, pero no es tu hermano, es nieto de tus abuelos, pero no es tu primo', palabra7]
    
    wordlist = [adivinanza1, adivinanza2, adivinanza3, adivinanza4, adivinanza5, adivinanza6, adivinanza7]
    wordlist_random = random.choice(wordlist)
    a = wordlist_random[0]
    b = wordlist_random[1]
    adivinanza(a, b)
    talk("Muy bien Jugado usuario, para volver a jugar solo di adininanzas")
            
    
def calculo():
    talk("Ingresa un numero")
    print("Ingresa un numero")
    n1 = (input())
    talk("Ingresa el operador del calculo mas, menos, por o divivdir")
    print("Ingresa el operador del calculo +. -, * o /")
    op = (input())
    talk("Okay, ahora ingresa otro numero")
    print("Ok, ahora ingresa otro numero")
    n2 = (input())
    
    n1 = float(n1)
    n2 = float(n2)
    
    if op == "+":
        print(n1, op, n2, "=", n1 + n2)
        talk(f"{n1} mas {n2} es aproximadamente {n1 + n2}")
        
    elif op == "-":
        print(n1, op, n2, "=", n1 - n2)
        talk(f"{n1} menos {n2} es aproximadamente {n1 - n2}")
        
    elif op == "*":
        print(n1, op, n2, "=", n1 * n2)
        talk(f"{n1} por {n2} es aproximadamente {n1 * n2}")
        
    elif op == "/":
        print(n1, op, n2, "=", n1 / n2)
        talk(f"{n1} entre {n2} es aproximadamente {n1 / n2}")
    
    elif op == "2":
        print(f"{n1} ^ {n2} = {math.pow(n1, n2)}")
        talk(f"{n1} a la potencia de {n2} es aproximadamente {math.pow(n1, n2)}")
        
    elif op == "r2":
        print(f"{n1} ^ {n2} = {math.pow(n1, n2)}")
        talk(f"a la raiz cuadrada de {n2} es aproximadamente {math.sqrt(n1)}") 
    else:
        print("Operador no valido")
        talk("Lo siento, no entendi eso")
        
        
def Recordatorio(name, time_):
    time.sleep(time_)
    talk("Recordatoriooooo "+  "usuario" + name)

class Users():
    user = 'none'

def waomi():
    global username
    a = open('Juegos\\Bases_Datos\\base.txt', 'r')
    b = a.read()
    print("Cooper por RaptorIndustries")
    print('-' * 23)
    print() 
    username = (input("Quien esta usando Cooper: "))
    if username in b:
          print("Bienvenido", username)
          talk("Bienvenido " + username)
        
        
    else:
        a.close()
        print("OOps, al pareser usted no ha iniciado secion con nosotros,")
        con = (input("Quiere iniciar secion y/n: "))
        if con == 'y':
            c = open('Juegos\\Bases_Datos\\base.txt', 'a')
            while True:
                new_username = (input("Ingresa tu nombre de usuario: "))
                if new_username in b:
                  print("Ese nombre ya existe, por favor elije otro :(")
                else:
                   print("Muy bien")
            
                new_pasw = (input("Ingresa tu contraseña: "))
                user = f"Username: {new_username}"
                psw = f"Password: {new_pasw}"
                c.write(f"\n{user} \n{psw}")
                print("Ok, Bienvenido a RaptorIndustries")
                c.close()
                Users.user = username
                break           
         
        elif con == 'n':
           print("ok, adios")
           run.runner=False
           run.runn=False
        else:
           print("No entendi lo que dijiste")
           
           
def whath():
    print(username)

def chistes():
    def ok():
        talk("Deacuerdo")
        talk("Me podrias pasar el saco")
        while True:
            rec = lisen()
            if 'cual saco' in rec:
              talk("Esta, jajjaajajajaja ")
              break
            else:
               talk("Se supone que tienes que deicir. cual saco")
               continue
           
        talk("Que lenguaje se mas")
        print("Que lenguje se mas")
        rec2 = lisen()
        if 'cual' in rec2:
            talk("SE mas mas")
            print("C++")
           
            
    talk("Algunos chistes, podrian ser inapropiados, gustas continuar")
    print("Algunos chistes, podrian ser inapropiados, gustas continuar")
    opcion = (input("oK/no: "))
    if opcion == 'ok':
        ok()

waomi()

