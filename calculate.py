import math


# jövőbeli tervek ezzel hogy a felhasználó adja meg hogy milyen számitások legyenek pontosabban magyarul egyszerre legyen benne osztás, szorzoás etc... 

nev = input("Add meg a nevedet : ")
print(f" Üdvözöllek {nev} , hadd mutassam be az én kis játékomat számodra ")



config = {

    "szamitások": [
        "1. kivonás",
        "2. összeadás",
        "3. szorzás",
        "4. osztás",
        "5. négyzet",
        "6. összetett müveletek",
        "7. értékek",
        "8. Exit"
    ],
}

listam = []
def kivonas():
    user_input= int(input("Add meg az első számot: "))
    numbers = int(input("Add meg a második számot: "))
    megoldas1 = user_input - numbers
    listam.append(megoldas1)
    print()
    print(megoldas1)
    

def összeadas():
    user_input= int(input("Add meg az első számot: "))
    numbers = int(input("Add meg a második számot: "))
    megoldas1 = user_input + numbers
    listam.append(megoldas1)
    print()
    print(megoldas1)
    

def szorzas():
    user_input= int(input("Add meg az első számot: "))
    numbers = int(input("Add meg a második számot: "))
    megoldas1 = user_input * numbers
    listam.append(megoldas1)
    print()
    print(megoldas1)
    

def osztas():
    user_input= int(input("Add meg az első számot: "))
    numbers = int(input("Add meg a második számot: "))
    
    megoldas1 = user_input / numbers
    listam.append(megoldas1)
    print()
    print(megoldas1)
    

def negyzet():
    user_input= int(input("Add meg az első számot: "))
    megoldas1 = user_input * user_input
    listam.append(megoldas1)
    print()
    print(megoldas1)
    
    

def osszetett_muveletek():
    kivonas = ["kivonás", "kivonas", "kivonast", "kivonásos", "kivonasos"]
    összeadas = ["összeadásos""összeadas", "összeadás", "össze", "összeadasos"]
    while True:
        kerdes = input("Válaszd ki a lehetőségeket, ki akarsz e lépni vagy akarod e még folytatni  [nem | igen ] : \n ")
        if kerdes.lower() == "nem":
            print(" Remélem hasznára váltam")
            break
        elif kerdes.lower() == "igen":
            action = input("Milyen művelettel akarod kezdeni ? Ezeknek a funkcióknak a működése hogy 1 számmal számol további számokkal, javasolni tudom adott összegből való kiszámitásokra IRL példák hónap végén megmaradt összeg kiszámolása, 1 alapból bejövő pénz és sok akár apróbb összegek kiszámolása: \n Kivonásos \n  Összeadásos \n kilépek : \n  ")
            if action.lower() in kivonas:
                big_number = int(input("Adj meg egy számot amivel akarsz számolni/ elindulni:"))
                user_input = input("Kérem adjon meg több számot szóközzel elválasztva: ")
                numbers = [int(num) for num in user_input.split()]
                
                    
                calculate = big_number - sum(numbers)
                print(f" Az értéke : {calculate} " )
                listam.append(calculate)
            elif action.lower() in összeadas:
                big_number1 = int(input("Adj meg egy számot amivel akarsz számolni/ elindulni:"))
                user_input1 = input("Kérem adjon meg több számot szóközzel elválasztva: ")
                numbers1 = [int(num) for num in user_input1.split()]
                    
                calculate2 = big_number1 + sum(numbers1)
                print(f" Az értéke : {calculate2} " )
                listam.append(calculate2)
                
            elif action.lower == "kilépek":
                break
        else:
            print("Érvénytelen bemenet. Kérem adjon meg olyan bemeneti értéket mint amit felsoroltunk ")
            continue
                
              
        

def ertekes(valami):
    try:
        osz_ertekuk = sum(valami)
        hosszusag = len(valami)
        maxertek = max(valami)
        eddigi_adatok = valami[::]
        print(f"Eddig ennyi számmot kaptál :  {hosszusag} \n ekkora ezeknek az értéke :  {osz_ertekuk} \n Legnagyobb értéke {maxertek} \n Eddigi adatok : {eddigi_adatok}")
    except ValueError:
        print("Érvénytelen bemenet. lehet hogy még nincsenek benne még adatok ")
    
    


def main():
    while True:
        print("\nszamitások:")
        for item in config['szamitások']:
            print(item)

        choice = input("Válaszd ki 1-8 :  ")

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
            ertekes(listam)
        elif choice == '8':
            print(f"Remélem jól érezted magadat {nev}")
            break
        else:
            print("Invalid choice. Please choose again.")
    
    
    
if __name__ == "__main__":
    main()