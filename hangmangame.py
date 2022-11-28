def game():
  attempts = 6
  rules = "Hello today you are going to play hangman. You get 6 lives in order to guess my magic word. Good luck! "
  print(rules)
  word_list = ("bag", "decent", "Group", "Leader", "Ministry", "Participate", "Context", "Dinosaur", "Architecture", "Mechanic", "Hypothetically", " Inconsequential", "Deez", "Neighborhood", "Block", "Hood", "Orangutan", "Parkway", "Gardens", "Hellcat")
  from random import choice
  word = list(choice(word_list))
 
#   guess = input("Choose a letter: ")
#   print(guess)
#   if guess in word: 
    
#   else:
#     return attempts -= 1 

# #print(ඞ🔪ඞ end if incorrect)