'''
author: Jan Zeisel
email: jzeisel@seznam.cz
'''

#Texty k analýze
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#Oddělovač výstupů
CARA = "-" * 40

#Seznam registrovaných uživatelů
registered_users = {"bob": "123", 
"ann": "pass123",
"mike": "password123",
"liz": "pass123"
}

#Login uživatele
print(CARA)
username = input("Zadej uživatelské jméno:")
password = input("Zadej heslo:")
print(CARA)

#Ověření registrace uživatele
if registered_users.get(username) == password:
    print("Welcome to the app,", username,)
else:
    exit("Unregistered user. Terminating the program.")

#Výběr textu k analýze
print("We have", len(TEXTS), "texts to be analyzed.")
print(CARA)
while True:
    try:
        choice = int(input("Zvol si text č. 1-3:")) - 1
        if choice < 0 or choice > len(TEXTS):
            raise IndexError
        chosen_text = TEXTS[choice]
        break
    except IndexError:
        exit("This text number is not defined. Terminating the program.")
    except ValueError:
        exit("The input is not a number. Terminating the program.")

#Analýza textu
#Nejdříve rozdělení zvoleného textu na jednotlivá slova a zjištění celkového počtu slov
words = chosen_text.split()
word_count = len(words)

#Zavedení pomocných načítacích proměnných, kam se ukládají počty výskytů sledovaných znaků 
capital_count = 0
uppercase_count = 0
lowercase_count = 0
numeric_count = 0

#List pro ukládaní čísel
numeric_values = []

#Slovník pro ukládaní slov s určitým počtem znaků a frekvencí výskytu slov s danou délkou znaku
word_length = {}

#Početní operace pro analýzu slov ve vybraném textu

for word in words:
    length=len(word)
    if length in word_length:
        word_length[length] += 1
    else:
        word_length[length] = 1
    if word.istitle():
        capital_count += 1
    if word.isupper() and word.isalpha():
        uppercase_count += 1
    if word.islower():
        lowercase_count += 1
    if word.isnumeric():
        numeric_count += 1
        numeric_values.append(int(word))

#Seřazení hodnot klíče slovníku od nejmenší po největší
sorted_world_length = dict(sorted(word_length.items())) 

#Tisk výsledků analýzy
print(CARA)
print("There are", word_count, "words in the selected text.")
print("There are", capital_count, "titlecase words.")
print("There are", uppercase_count, "uppercase words.")
print("There are", lowercase_count, "lowercase words.")
print("There are", numeric_count, "numeric strings.")
print("The sum of all the numbers is", sum(numeric_values), ".")
print(CARA)
print("LEN|  OCCURENCES  |NR.")
print(CARA)
for length, frequency in sorted_world_length.items():
    occurences = "*" * frequency
    print(f"{length:>3}|{occurences:<14}|{frequency:>1}")