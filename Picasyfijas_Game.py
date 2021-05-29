import time
import random
start = time.time()
def game():
  boton = True
  x = []
  a = input("1 para adivinar un numero random, 2 para adivinar el numero de un usuario anterior")
  if int(a) == 1:
    b =input("Nivel de dificultad del 1 al 10")
    
    while len(x) < int(b):
      y = int(random.random()*9)
      x.append(y)
      random_number= "".join([str(i) for i in x])
    numero_adivinar = random_number
    
  intento = 0
  while boton:
    picas = 0
    fijas = 0
    if int(a) == 2:
      numero_usuario_anterior = "5618"
      numero_adivinar = numero_usuario_anterior
    num = input(f"Intente adivinar el numero de {b} cifras >>")
    b = int(b)      
    mydict = {}
    for c in range(b):
      if numero_adivinar[c] == num[c]:
        fijas = fijas + 1
      elif num[c] in numero_adivinar:
          picas = picas + 1
    mydict.update({picas:fijas})
    if fijas != b:
      pass
    else:
      end = time.time() 
      print(f"Usted adivino el numero en su intento numero {intento} y se demoro {int(end-start)} segundos!")
      boton = False
      exit()
    intento = intento + 1              
    print(f"Usted tiene {picas} picas y {fijas} fijas {mydict} y es su {intento} intento")

game()
 
