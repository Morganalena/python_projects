author = """
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Alena Morgan
email: Alena.karnosova@gmail.com
discord: Alena M.
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''',
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

#Vyžádá si od uživatele přihlašovací jméno a heslo,
#zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,
#pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,
#pokud není registrovaný, upozorni jej a ukonči program.**


#Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS:
    #Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí,
    #pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.


import sys

registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
    }

user_name = input("Enter your login name: ").casefold()
password = input("Enter your password: ")
   
if not (user_name in registered_users and password == registered_users[user_name]):
    
    print(f'Username: {user_name}'
          f'\nPassword: {password}'
          f'\nUnregistered user, terminating the program..'
          )
    sys.exit(0)

else:
    print(f'Username: {user_name}'
          f'\nPassword: {password}'
          f'\n{"-" * 40}'
          f'\nWelcome to the app, {user_name}' 
          f'\nWe have 3 texts to be analyzed.'
          f'\n{"-" * 40}'
          )

answer = input("Enter a number btw. 1 and 3 to select: ")

if not (answer.isnumeric() and int(answer) in range(1, 4)):
    print("Invalid input. Terminating the program...")
    sys.exit(0)

else:
    print("-" * 40)
    
selected_text = TEXTS[int(answer) - 1].replace(",", " ").replace(".", " ").split( )

#6/Pro vybraný text spočítá následující statistiky:
    #počet slov,
    #počet slov začínajících velkým písmenem,
    #počet slov psaných velkými písmeny,
    #počet slov psaných malými písmeny,
    #počet čísel (ne cifer),
    #sumu všech čísel (ne cifer) v textu.

word_counts = len(selected_text)
print("There are", word_counts, "words in the selected text.")

titlecase = sum (1 for word in selected_text if word.istitle())
print("There are", titlecase,"titlecase words.")

uppercase = sum (1 for word in selected_text if word.isupper() 
                 and word.isalpha())
print("There are", uppercase,"uppercase words.")

lowercase = sum (1 for word in selected_text if word.islower() 
                 and word.isalpha())
print("There are", lowercase,"lowercase words.")
      
numeric = sum (1 for number in selected_text if number.isdigit() 
               and not number.isalpha())
print("There are", numeric,"numeric strings.")

sum_of_all_numbers = sum (int(sum_number) for sum_number in selected_text 
                          if sum_number.isdigit() and not sum_number.isalpha())
print(f'The sum of all the numbers {sum_of_all_numbers}'
      f'\n{"-" * 40}'
    )

#7/Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. 

word_lengths_count = {}

for word in selected_text:
    length = len(word)
    if length in word_lengths_count:
        word_lengths_count[length] += 1
    else:
        word_lengths_count[length] = 1
    
max_count = max(word_lengths_count.values())

print(f'LEN|  OCCURENCES {" " * (max_count - 11)}|NR.'
        f'\n{"-" * 40}'
    )

for length in sorted(word_lengths_count):
    count = word_lengths_count[length]

    print(f'{length:3}|{"*" * count:{max_count}}  |{count}'
    )
















