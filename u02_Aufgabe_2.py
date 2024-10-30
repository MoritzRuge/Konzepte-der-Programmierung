def main():
    while True:
        print("1.Flächenberechnung\n2.Schaltjahr\n3.Mersennezahl\nExit\nBitte wählen Sie mittels 1-4 oder geben Sie Exit ein um das Programm zu beenden.")
        value = input().title()
        match value:
            case "1":
                Flaechenberechnung()
            case "2":
                Schaltjahr()
            case "3":
                MersenneZahl()
            case "Exit":
                quit()
            case _:
                print("Entschuldigung, diese Anweisung verstehe ich nicht.")

#Funktion für die Berechne der Fläche eines Dreiecks mit Grundseitenlnge a und höhe h
def Flaechenberechnung():
    print("Hallo, willkommen bei der Dreiecks Flächenberechnung. Bitte gebe die Grundseitenlänge a und die höhe h ein.")
    a = int(input("a: ")) # user input für die Variable a
    h = int(input("h: ")) # user input für die Variable h
    area = 0.5 * a * h # Formel für die Flächenberechnung A = 0,5 * a * h
    print(f"Die Fläche beträgt {area:.2f}") # Print das Endergebnis

# User gibt uns eine Zahl/Jahr Funktion gibt genau dann True zurück, wenn die Zahl/Jahr ein Schaltjahr
# im Gregorianischen Kalender ist.
# Jahreszahl muss durch 4 teilbar sein
# Die Jahreszahl darf nicht restlos durch 100 teilbar sein
#Ist eine Jahreszahl, die restlos durch 100 teilbar ist, ebenfalls restlos durch 400 teilbar, ist das Jahr dennoch ein Schaltjahr.
def Schaltjahr():
    print("Willkommen im Schaltjahrrechner, bitte geben Sie die Gewünschte Jahreszahl ein.")
    year = int(input("Year: ")) # user Input für das Jahr
    modulus_four = year % 4 # Erstellt den Modulus für den Input durch 4
    modulus_hundred = year % 100 # Erstellt den Modulus für den Input von 100
    modulus_four_hundred = year % 400 # Berechnet den Modulus für 400
    if modulus_four == 0: # Wenn die Zahl Restlos durch 4 teilbar ist gehen wir in die nächste if Schleife
        if modulus_hundred == 0 and modulus_four_hundred == 0: # Restlos durch 100 und 400 teilbar return true
            print(True)
        elif modulus_hundred == 0: # wenn nur durch restlos durch 100 teilbar retun false
            print(False)
        else: # wenn nur restlos durch 4 teilbar dann true
            print(True)
    else: # Zahl nicht restlos durch 4 teilbar retun false
        print(False)

def MersenneZahl():
    # Mersenne Zahl: 2^n - 1 in Bit Operationen
    # Bit shift nach links entspricht 2^n
    n = int(input("n: "))
    n << n
    print(n)
# Vorsichtsmaßnahme erklärung muss ich noch raussuchen...duh
if __name__ == "__main__":
    main()
