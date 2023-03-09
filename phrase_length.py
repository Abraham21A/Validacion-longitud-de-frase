# Longitud de una frase o palabra / Length of a phrase or word

# Se inicia un ciclo infinito con la estructura while True
while True:
  # Se solicita al usuario que ingrese una palabra
  word = input("Por favor, ingrese una palabra (o escriba 'salir' para terminar): ")
  # Si el usuario ingresa "salir" o "exit", se rompe el ciclo y se termina el programa
  if word.lower() in ['salir', 'exit']:
    break
  # Si la palabra ingresada es vacía o numérica, se le pide al usuario que ingrese una palabra válida y se continua el ciclo
  elif word == "" or word.isnumeric():
    print("Ingrese una palabra valida")
    continue
  # Si la palabra ingresada es válida, se verifica su longitud y se imprime un mensaje correspondiente
  else:
    try:
      # Se eliminan los espacios de la palabra ingresada
      word_no_spaces = word.replace(" ", "")
      # Se calcula la longitud de la palabra sin espacios
      word_len = len(word_no_spaces)
      # Si la longitud de la palabra está entre 4 y 8 letras, se imprime un mensaje indicando que la palabra es correcta y su longitud
      if word_len >= 4 and word_len <= 8:
        print("La palabra {} es correcta, tiene {} letras".format(word, word_len))
      # Si la longitud de la palabra es menor a 4 letras, se imprime un mensaje indicando que faltan letras
      elif word_len < 4:
        print("Hacen falta letras, La palabra {} solo tiene {} letras.".format(word, word_len))
      # Si la longitud de la palabra es mayor a 8 letras, se imprime un mensaje indicando que sobran letras
      else:
        print("Sobran letras. La palabra {} tiene {} letras".format(word, word_len))
    # Si se produce un error al realizar alguna de las operaciones anteriores, 
    # se imprime un mensaje indicando que el valor ingresado es incorrecto y se continúa el ciclo
    except ValueError:
      print("Valor Incorrecto, vuelva a ingresar la palabra")
      continue