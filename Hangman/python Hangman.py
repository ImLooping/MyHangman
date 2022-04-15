
import plistlib
from hangman_functions import *
from hangman_drawings import *
from string import punctuation



word = word_selection(words_list)
length = word_length(word)
shape = length * word_shape()
attemps = 0
letters = []


clear()
loading_game()

print("############\n# NEW GAME #\n############")
while attemps < 10:
    if shape == word:
        print(f"\n################################################################ \nFELICITATIONS !!! Vous avez trouvé le mot correct : {word} !\n################################################################")
        break
    print(shape)
    if len(letters) > 0:
        print(f"""\nLes lettres déjà utilisées sont:
        {letters}\n""")
    letter = input("\nEssayez une lettre :")
    result = letter_found(word, letter, shape)
    if letter not in letters and letter.isalpha() and len(letter) == 1 and letter not in punctuation:
        shape = letter_found(word, letter, shape)
        letters.append(letter)
        if letter in word:
            print("\n########## BRAVO ! Cette lettre est bien dans le mot recherché ! ##########\n")
        elif letter in letters and letter not in word:
            print("\n########## Cette lettre n'est pas dans le mot recherché ##########\n")
            attemps += 1
            drawing_number(attemps)
    else:
        print("\nVous avez essayé un caractère incorrect :\n   - Déjà utilisé \n   - Pas une lettre \n   - Plus d'une lettre\n")
        #j'ai voulu être sympa et ne pas rajouter une tentative dans ce cas là
    if attemps == 10:
        dead_func()
        print("#######################################\n Vous avez épuisé toutes vos chances !\n#######################################")
        break


















