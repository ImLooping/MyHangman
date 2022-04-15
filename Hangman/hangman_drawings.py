


def drawing_number(fail_number):
    #Draws the hangman corresponding to the number of failures
    drawings = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, dead_func]
    return drawings[fail_number]()

def f0():
  print("\n")
  print("\n")
  print("\n")
  print("\n")
  print("\n")
  print("\n")
  print("\n")

def f1():
  print("\n")
  print("\n")
  print("\n")
  print("\n")
  print("\n")
  print("_____________\n")

def f2():
  print("\n")
  print(" |\n")
  print(" |\n")
  print(" |\n")
  print(" |\n")
  print(" |\n")
  print("_|____________\n")

def f3():
  print("_____________\n")
  print(" |\n")
  print(" |\n")
  print(" |\n")
  print(" |\n")
  print(" |\n")
  print("_|____________\n")

def f4():
  print("_____________\n")
  print(" | /\n")
  print(" |/\n")
  print(" |\n")
  print(" |\n")
  print(" |\n")
  print("_|____________\n")

def f5():
  print("_____________\n")
  print(" | /       |\n")
  print(" |/\n")
  print(" |\n")
  print(" |\n")
  print(" |\n")
  print("_|____________\n")

def f6():
  print("_____________\n")
  print(" | /       |\n")
  print(" |/        O\n")
  print(" |\n")
  print(" |\n")
  print(" |\n")
  print("_|____________\n")

def f7():
  print("_____________\n")
  print(" | /       |\n")
  print(" |/        O\n")
  print(" |         |\n")
  print(" |\n")
  print(" |\n")
  print("_|____________\n")

def f8():
  print("_____________\n")
  print(" | /       |\n")
  print(" |/        O\n")
  print(" |        /|\\n")
  print(" |\n")
  print(" |\n")
  print("_|____________\n")

def f9():
  print("_____________ \n")
  print(" | /       | \n")
  print(" |/        O \n")
  print(" |        /|\ \n")
  print(" |        / \ \\n")
  print(" |\n")
  print("_|____________\n")
  print("YOU'RE ALMOST DEAD !\n")

def f10():
  print("_____________ \n")
  print(" | /       | \n")
  print(" |/        O \n")
  print(" |        /|\ \n")
  print(" |        / \ \n")
  print(" |\n")
  print("_|____________\n")

def dead_func():
  print("T00 LATE ! YOU'RE DEAD MAN !!!\n")

