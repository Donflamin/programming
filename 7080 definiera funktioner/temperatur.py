#
# Funktion för att konvertera mellan Celsius, Kelvin och Fahrenheit.
#

def konvertera_temperatur(nummer, första_enhet, andra_enhet):
    konverteringar = {
        ("C", "F"): lambda C: C * 9/5 + 32, # Celsius till Fahrenheit
        ("C", "K"): lambda C: C + 273.15, # Celsius till Kelvin
        ("F", "C"): lambda F: (F - 32) * 5/9, # Fahrenheit till Celsius
        ("F", "K"): lambda F: (F- 32) * 5/9 + 273.15, # Fahrenheit till Kelvin
        ("K", "C"): lambda K: K - 273.15, # Kelvin till Celsius
        ("K", "F"): lambda K: (K - 273.15) * 9/5 + 32 # Kelvin till Fahrenheit
    }

    return konverteringar[(första_enhet, andra_enhet)](nummer)

#
### Huvud programmet
#

def huvud():
    enheter = {"C": "Celsius", "F": "Fahrenheit", "K": "Kelvin"} # Kopplar C F och K till respektive fulla ord
    while True:
        try: # Error handling
            första_enhet = input(f"Jag vill konvertera denna enhet ({'/'.join(enheter.keys())}): ").upper()
            if första_enhet not in enheter:
                raise ValueError("felaktig enhet")

            andra_enhet = input(f"Jag vill konvertera till ({'/'.join(enheter.keys())}): ").upper()
            if andra_enhet not in enheter:
                raise ValueError("felaktig enhet")

            nummer = float(input("Skriv temperatur: "))
            resultat = konvertera_temperatur(nummer, första_enhet, andra_enhet)
            print(f"{nummer} {enheter[första_enhet]} är {resultat} {enheter[andra_enhet]}")

            if input("Konvertera igen? (J/N): ").upper() != "J":
                break
        except ValueError as e:
            print(f"Felaktig inmatning: {e}")

if __name__ == "__main__": # Om detta är huvud skriptet (alltså inte importerat) så körs huvud
    huvud()

