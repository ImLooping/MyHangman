import time
from os import system, name
from list_of_words import words_list
from random import choice
import re

def word_selection(words_list):
  #Selects a random word among the list of words (e.g. list_of_words python file)
  selected_word = choice(words_list)
  return selected_word

def word_length(selected_word):
  #Returns the length of selected word
  len_word = len(selected_word)
  return len_word

def word_shape():
  #Returns the shape of selected word
  return "_"


def letter_found(selected_word, letter, word_guessed):
  #Fills the word shape ("P____") with the new guessed letter (such as "PE__E") 
  
    # finditer returns an iterator yielding objects that match a pattern in a string
    matches = re.finditer(letter, selected_word)
    # matches_positions is a list of the guessed letter's position(s) in the word
    matches_positions = [match.start() for match in matches]

    for j in matches_positions:
        word_guessed_list = list(word_guessed)
        word_guessed_list.pop(j)
        word_guessed_list.insert(j, letter)
        word_guessed = "".join(word_guessed_list)
      
    return word_guessed



# ------- Ne fonctionne pas sur notebook


def loading_game():
  # Loading game animation at game start
    for x in range(0, 4):
        clear()
        loading = "Loading game" + "." * x
        print(loading, end="\r")
        time.sleep(1)
        clear()

# clear output function 
def clear(): 
    # for windows
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux
    else: 
        _ = system('clear')