svar = int(input("Gissa ett tal!"))
counter = 1
while counter < 6 and svar != 42:
        if svar > 42:
            svar = int(input("För stort"))
            counter = counter + 1
        if svar < 42:
            svar =int(input("För litet"))
            counter = counter + 1
        else:
            print("Rätt")
            counter = 6
