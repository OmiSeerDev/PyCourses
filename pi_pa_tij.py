import random
user_wins = 0
pc_wins = 0
round = 1
while (True):
    print(f"=====================\nROUND: {round}")
    inserto = input("Inserte su opción: piedra, papel o tijeras\n").lower()
    computer_opt = random.randint(1, 3)


    def select_option(option):
      option_dic = {1: "tijeras", 2: "papel", 3: "piedra"}
      return option_dic[option]


    if ((inserto == "piedra" and computer_opt == 3)
        or (inserto == "tijeras" and computer_opt == 1)
        or (inserto == "papel" and computer_opt == 2)):
      print(f"Empate 😒: Tú => {inserto} vs PC => {select_option(computer_opt)}")

    elif (inserto == "piedra" and computer_opt == 2):
      print(f"Perdiste 😩: Tú => {inserto} vs PC => {select_option(computer_opt)}")
      pc_wins += 1
    elif (inserto == "piedra" and computer_opt == 1):
      print(f"Ganaste 😊: Tú => {inserto} vs PC => {select_option(computer_opt)}")
      user_wins += 1
    elif (inserto == "papel" and computer_opt == 1):
      print(f"Perdiste 😩: Tú => {inserto} vs PC => {select_option(computer_opt)}")
      pc_wins += 1
    elif (inserto == "papel" and computer_opt == 3):
      print(f"Ganaste 😊: Tú => {inserto} vs PC => {select_option(computer_opt)}")
      user_wins += 1

    elif (inserto == "tijeras" and computer_opt == 3):
      print(f"Perdiste 😩: Tú => {inserto} vs PC => {select_option(computer_opt)}")
      pc_wins += 1
    elif (inserto == "tijeras" and computer_opt == 2):
      print(f"Ganaste 😊: Tú => {inserto} vs PC => {select_option(computer_opt)}")
      user_wins += 1
    else:
      print("Opción inválida")
    round +=1
    if (user_wins == 3):
     print("¡Usted gana!")
     break
    if (pc_wins == 3):
     print("¡La PC gana!")
     break