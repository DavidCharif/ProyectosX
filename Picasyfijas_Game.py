def game():
  boton = True
  intento = 1
  while boton:
    picas = 0
    fijas = 0
    num = input("Ingrese un numero de cuatro cifras >>")
    numero_adivinar = '5618'
    mydict = {}
    for c in range(4):
      if numero_adivinar[c] == num[c]:
        fijas = fijas + 1
      elif num[c] in numero_adivinar:
          picas = picas + 1

    mydict.update({picas:fijas})
    if fijas == 4:
      print(f"Usted adivino el numero en su intento numero {intento}!")
      boton = False
      exit()
    
    intento = intento + 1              
    print(f"Usted tiene {picas} picas y {fijas} fijas {mydict} y es su {intento} intento")
game()
 
