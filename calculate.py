
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

def is_number(value):
    try:
        int(value)  
        return True
    except ValueError:
        return False



def kivonas():
    user_input = input("Kérlek, add meg az inputot: ")
    numbers = [int(num) for num in user_input.split("-")]
    operations = "-"
    
    pass

def összeadas():
    pass

def szorzas():
    pass

def osztas():
    pass

def negyzet():
    pass

def osszetett_muveletek():
    pass


def main():
    pass
    
    
if __name__ == "__main__":
    main()