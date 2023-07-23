while True:
    try:
        user_input = input("Kérem adjon meg több számot szóközzel elválasztva: ")
        numbers = [int(num) for num in user_input.split()]

        # Itt a numbers listában egész számok találhatók, használhatjuk tovább
        print(f"A bevitt számok: {numbers}")

    except ValueError:
        print("Érvénytelen bemenet. Kérem adjon meg csak számokat és szóközöket!")
