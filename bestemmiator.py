from bestemmie import Bestemmie

bestemmieDB = ["madonna", "dio"]

while True:
    vin = input("Scrivi un messaggio : ")
    for i in range(len(bestemmieDB)):
        if bestemmieDB[i] in vin:
            print(f"Zitto, so bestemmiare meglio io, {Bestemmie().random()}")

        if ".bestemmie" in vin:
            limit = input("inserisci numero bestemmie desiderate : ")
            try:
                for i in range(int(limit)):
                    print(f"{Bestemmie().random()}")
            except:
                print("Inserisci un numero!")
            

