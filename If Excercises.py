# Alustetaan muuttujat

number1 = 10
number2 = 10
number3 = 10

name1 = "Teppo"
name2 = "Jukka"
name3 = "Mikko"

# Tarkistetaan onko number1 yhtä suuri kuin number2

if number1 == number2:
    print("Number 1 is equal to Number 2")
else:
    print("Number 1 is not equal to Number 2")

# Tarkistetaan onko number1 suurempi kuin number2

if number1 > number2:
    print("Number 1 is greater than Number 2")
else:
    print("Number 1 is not greater than Number 2")

# Tarkistetaan onko number1 suurempi tai yhtä suuri kuin number2

if number1 >= number2:
    print("Number 1 is greater or equal to Number 2")
else:
    print("Number 1 is not greater or equal to Number 2")

# Tarkistetaan onko number1 erisuuri kuin number2

if number1 != number2:
    print("Number 1 is not equal to Number 2")
else:
    print("Number 1 is equal to Number 2")

# Tarkistetaan ovatko number1, number2 ja number3 yhtä suuria

if number1 == number2 == number3:
    print("Number 1, Number 2 and Number 3 are equal")
else:
    print("Number 1, Number 2 and Number 3 are not equal")

# Tarkistetaan ovatko number1 ja number2 TAI number2 ja number3 yhtä suuria

if number1 == number2 or number2 == number3:
    print("Number 1 and Number 2 are equal or Number 2 and Number 3 are equal")
else:
    print("Number 1 and Number 2 are not equal or Number 2 and Number 3 are not equal")

# Tarkistetaan onko number1 suurempi kuin number2 ja number3

if number1 > number2 and number1 > number3:
    print("Number 1 is greater than Number 2 and Number 3")
else:
    print("Number 1 is not greater than Number 2 and Number 3")

# Tarkistetaan onko number1 suurempi kuin number2 - jos ei, tarkistetaan onko number2 suurempi kuin number3

if number1 > number2:
    print("Number 1 is greater than Number 2")
elif number2 > number3:
    print("Number 2 is greater than Number 3")
else:
    print("Number 1 is not greater than Number 2 and Number 2 is not greater than Number 3")

# Tarkistetaan ovatko number1 ja number2 yhtä suuret - jos ei, tarkistetaan ovatko number1 ja number3 yhtä suuret

if number1 == number2:
    print("Number 1 and Number 2 are equal")
elif number1 == number3:
    print("Number 1 and Number 3 are equal")
else:
    print("Number 1 and Number 2 are not equal and Number 1 and Number 3 are not equal")

# Tarkistetaan onko name1 yhtä suuri kuin name2

if name1 == name2:
    print("Name 1 is equal to Name 2")
else:
    print("Name 1 is not equal to Name 2")

# Tarkistetaan ovatko name1 ja name2 eri suuret

if name1 != name2:
    print("Name 1 is not equal to Name 2")
else:
    print("Name 1 is equal to Name 2")

# Tarkistetaan onko name1 yhtä suuri kuin name2 - jos ei, tarkistetaan onko name1 yhtä suuri kuin name3

if name1 == name2:
    print("Name 1 is equal to Name 2")
elif name1 == name3:
    print("Name 1 is equal to Name 3")
else:
    print("Name 1 is not equal to Name 2 and Name 1 is not equal to Name 3")



