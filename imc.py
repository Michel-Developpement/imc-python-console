while True:
  while True:
    taille = input("Entrez votre taille en cm : ")
    weight = input("Entrez votre poids en kg : ")
    if taille.isdigit() and weight.isdigit():
      break
    else:
      print("Entrez uniquement des chiffres")
  taille_carre = float(taille) / 100
  imc = float(weight) / (taille_carre ** 2)
  print(f"Votre imc est de {imc}.")
  restart = input('Taper "quit" pour quitter : ')
  restart.lower()
  if restart == "quit":
    break