import random

# Luodaan lista
furniture = ["table", "chair", "shelf", "sofa"]

# Tulostetaan koko lista
print (furniture)

#Tulostetaan listan kaksi ensimmäistä elementtiä
print (furniture[:2])

# Tarkistetaan onko listassa elementti "sofa" - jos on, se tulostetaan
for item in furniture:
    if item.lower() == "sofa":
        print("Sofa")
        break
else:
    print("'sofa' was not found")

# Alustetaan muuttujat
random_number1 = random.randint(1, 100)
random_number2 = random.randint(1, 100)
random_number3 = random.randint(1, 100)
random_number4 = random.randint(1, 100)
random_number5 = random.randint(1, 100)


# Luodaan toinen lista
thrownDiceNumber = [random_number1, random_number2, random_number3, random_number4, random_number5]

# Tulostetaan koko lista
print (thrownDiceNumber)

# Lasketaan listan numerot yhteen ja tulostetaan summa
total_sum = sum(thrownDiceNumber)
print (total_sum)

# Tulostetaan isoin arvo listasta
highest_value = max (thrownDiceNumber)
print (highest_value)

# Tulostetaan viisi numeroa väliltä 1-20 ja varmistetaan että jokainen numero on eri
random_numbers = random.sample (range(1, 20), 5)
print (random_numbers)






