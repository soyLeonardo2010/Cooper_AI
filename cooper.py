from datetime import datetime
import speech_recognition as sp
import pyttsx3
import pywhatkit
import datetime 
import script

print(script.Day.day)
 
runn = True
game = script.Day.juego 
game = str(game)
day = script.Day.day
day = str(day)
version = '[1.7.6]'
script.waomi()
if runn:
    print("Cooper Version" + version)
    print("Presiona enter para que cooper te escuche")
    print("solo di \"adios\" para salir")
while script.run.runner:
    a = (input(">>> "))
    if a == "exit":
      break
    elif a == 'waomi':
      print(f"User: {script.whath()}")
      continue
      
    line_of_code = 116 + 210
    listener = sp.Recognizer()  
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    name = 'cooper' 

    def talk(text):
      word = name
      texto = text.replace(word, "")
      engine.say(texto)
      engine.runAndWait()



    def lisen():
      try:
        with sp.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec1 = listener.recognize_google(voice)
            rec1 = rec1.lower()
            print(rec1)
            if name in rec1:
               talk(rec1)
            else:
              pass
      except UnboundLocalError:
           print("Error en el microfono :(")
           script.runner=False
      except sp.exceptions.UnknownValueError:
        print("Error en el micrifono :(")
        script.runner=False
      return rec1
    
  
    def run():
      rec1 = lisen()

      if 'reproduce' in rec1:
        music = rec1.replace('reproduce', '')
        talk("Reproduciendo" + music)
        print("Reproduciendo...")
        pywhatkit.playonyt(music)
      
      
      elif 'hora' in rec1:
        hora_actual = datetime.datetime.now()
        t1 = hora_actual.strftime("%H:%M")
        t2 = str(t1)
        talk("La hora actual es:" + t2)
        print("La hora actual es:" + t2)
        
      elif 'record a torio' in rec1:
        global dia
        global rec
        talk("Muy bien, ingresa el dia y el asunto del recordatorio")
        dia = input("Ingresa el dia del recordatorio: ")
        rec = input("Ingresa el asunto: ")
        x = open('file.txt', 'a')
        y = x.write(f'\n asunto: {rec}')
        x.close()
        
      elif 'recordatorio' in rec1:
        talk("Muy bien, ingresa el dia y el asunto del recordatorio")
        dia = input("Ingresa el dia del recordatorio: ")
        rec = input("Ingresa el asunto: ")
        
      elif 'hola' in rec1:
          talk("Hola, señor Leo, como estas hoy, todod bien?" + "solo para recordarte que hoy es " + day + ', y el juego de hoy es, ' + game + ", solo di," + game)
          h = open('file.txt', 'r')
          f = h.read()
          if f is str():
            try:
              w = open('file.txt', 'r')
              z = w.read()
              z.removeprefix(' asunto: ')
              w.close()
              talk("A y antes de que se me olvide hoy tiene unos recordatorios " + z)
            except NameError:
              pass
          else:
            pass
          h.close()
          
      elif 'nombre' in rec1:
          talk("mi nombre es " + 'cuuper,' + "soy una inteligencia artificial echa por el programador leonardo Mota, fundador de la empreza RaptirIndustries, me programaron en el famoso lenguaje de programacion python, y mi proposito es que usted tenga la mejo experiencia, y yo sea de su utilidad.")
      elif 'eres' in rec1:
          talk("mi nombre es " + 'cuuper,' + "soy una inteligencia artificial echa por el programador leonardo Mota, fundador de la empreza RaptirIndustries, me programaron en el famoso lenguaje de programacion python, y mi proposito es que usted tenga la mejo experiencia, y yo sea de su utilidad.")
      
      elif 'gracias' in rec1:
        talk("Estoy para ayudarte")
        
      elif 'piedra papel o tijera' in rec1:
        script.game_1()
      elif 'piedra papel or tijera' in rec1:
        script.game_1()
        
      elif 'char' in rec1:
        script.game_2()
        
      elif 'adivinanzas' in rec1:
         script.game_3()
      
      elif 'cuanto es' in rec1:
        talk("Para hacer algun calculo en espesifico, solo di calculadora")
      
      elif 'calculadora' in rec1:
        script.calculo()
      
      elif 'adios' in rec1:
        script.runner=False
        talk("adios usuario, nos vemos pronto")
        
      elif 'salir' in rec1:
        script.runner=False
        talk("adios usuario, nos vemos pronto")
      
      elif 'hicieron' in rec1:
        line = str(line_of_code)
        talk("A mi me programaron en le famoso lenguaje de programacion python, tengo mas de " + line +"lineas de codigo y todabia trbajan en mi desarroyo para que usted tenga la mejor ecperiencia posibel")
       
      elif 'soy' in rec1:
        talk('Usted es el usuario' + script.whath())
        print("User: ", script.whath())
        print() 
        
      elif 'chistes' in rec1:
        script.chistes()
      else:
        buscar = rec1.replace('buscando', '')
        talk("No entendi lo que dijiste lo buscare en la web")
        talk("Buscando")
        print("Buscando...")
        pywhatkit.search(buscar)
        
    
    run()
    
    
    