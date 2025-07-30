# This is a hangman game program 
import random

words = ["Manzana", "Platano", "Naranja", "Pera", "Kiwi", "Mandarina", "Frutilla", "Piña", "Sandia", "Menbrillo", "Frambuesa", "Limon"]

# Random word the game will take
random_word = random.choice(words)
print(random_word)

# first word of the random word
first_word = random_word[0] 

# last word of the random word
last_word = random_word[-1] 

# removes the first and last index of the random word
hide_words = random_word[1:-1] 

hide = []
for i in hide_words:
    hide.append("*")

result_hide = "".join(hide)
final_word = first_word + result_hide + last_word
print(final_word)

tries = len(final_word) + 2

while True:
    choice = input(": ")
    
    for i in random_word:
        if i == choice:
            print("La letra esta en la palabra.")
            break
    print("La letra no esta en la palabra.")
    tries -= 1

    if tries == 0:
        print("Perdiste!")
        break




        
