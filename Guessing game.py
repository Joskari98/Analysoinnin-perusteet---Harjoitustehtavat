attempts = 0
correct_name = "joni"  
name = ""

while True:
    name = input("Please, guess my name: ")
    attempts += 1
    if name.lower() == correct_name:
        print("Congratulations!")
        print("Guesses: " + str(attempts))
        break  # Poistutaan loopista oikean vastauksen jälkeen
    else:
        quit = input("Do you want to quit? Y/N: ")
        if quit.lower() == "y":
            print("Guesses: " + str(attempts))
            break
        elif quit.lower() == "n":
            continue  # Jatketaan kysymistä, jos käyttäjä ei halua lopettaa
        else:
            print ("Error! Write a correct input.")
            






        


