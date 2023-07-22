import random


acceptable_elements = ["kő", "papir", "olló"]

player_name = input("Hello idegen! mond meg a neved: ")
print("örülök a találkozásnak ", player_name, "!")
print(
"""
gyere és játsz velem  Rock-Paper-Scissors játékot!
-------------------------------------------------
"""
)

game_is_on = True
buffer = " " * 5 # buffer = "     "

while game_is_on:
    users_choice = input("válasz egyett a listából: kő, papir, olló vagy exit!\nVálasztásod: ").lower() 

    if users_choice in acceptable_elements:
        computers_choice = random.choice(acceptable_elements)

        print(buffer, "Játékos: ", users_choice, "Gép: ", computers_choice)

        if users_choice == computers_choice:
            round_message = "ugyan az újra "
        elif users_choice == "kő" and computers_choice == "olló":
            round_message = "nyertél"
        elif users_choice == "olló" and computers_choice == "papir":
            round_message = "nyertél"
        elif users_choice == "papir" and computers_choice == "kő":
            round_message = "nyertél"
        else:
            round_message = "veszitettél"

        print(buffer, round_message)

    elif users_choice == "exit":
        game_is_on = False
    else:
        print("ez nem igazi érték")

print("vicces volt ", player_name, " viszlát")