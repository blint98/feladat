
nev = input("Add meg a nevedet : ")
print(f" Üdvözöllek {nev} , hadd mutassam be az én kis játékomat számodra ")



config = {

    "szamitások": [
        "1. kivonás",
        "2. összeadás",
        "3. szorzás",
        "4. osztás",
        "5. négyzet",
        "6. osszetett müveletek",
        "7. Exit"
    ],
}


def kivonas():
    user_input= input("Kérlek adj meg 2 számot: ")
    numbers = int(user_input)
    
    return f" A megoldás {numbers[0] + numbers[1]}"
    return f" A megoldás {numbers[1] + numbers[0]}"

def összeadas():
    user_input1 = input("Kérlek adj meg 2 számot: ")
    numbers = int(user_input1)
    
    return f" A megoldás {numbers[0] + numbers[1]}"
    return f" A megoldás {numbers[1] + numbers[0]}"

def szorzas():
    user_input2 = input("Kérlek adj meg 2 számot: ")
    numbers = int(user_input1)
    
    return f" A megoldás {numbers[0] + numbers[1]}"
    return f" A megoldás {numbers[1] + numbers[0]}"

def osztas():
    user_input2 = input("Kérlek adj meg 2 számot: ")
    numbers = int(user_input2)
    
    return f" A megoldás {numbers[0] / numbers[1]}"
    return f" A megoldás {numbers[1] / numbers[0]}"

def negyzet():
    user_input3 = input("Kérlek adj meg 2 számot: ")
    numbers = int(user_input3)
    
    return f" A megoldás {square(numbers[0])}"
    return f" A megoldás {square(numbers[1])}"
    

def osszetett_muveletek():
    pass     
    


def main():
    while True:
        print("\nMenu:")
        for item in config['szamitások']:
            print(item)

        choice = input("Válaszd ki 1-7 :  ")

        if choice == '1':
            kivonas()
        elif choice == '2':
            összeadas()
        elif choice == '3':
            szorzas()
        elif choice == '4':
            osztas()
        elif choice == '5':
            negyzet()
        elif choice == '6':
            osszetett_muveletek()
        elif choice == '7':
            print("Remélem jól érezted magadat {nev}")
            break
        else:
            print("Invalid choice. Please choose again.")
    
    
    
if __name__ == "__main__":
    main()