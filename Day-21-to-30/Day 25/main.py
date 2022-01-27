import random
import stages
from word_list import word_list

print(logo.logo1)


chosen_word=random.choice(word_list)

display = []
lives = 6


for i in range(len(chosen_word)):
    display += "_"


end_of=False
while  not end_of :
    guess = input("guess the value").lower()
    print(guess)


    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
    print(display)

    if "_" not in display:
        end_of = True
        print("You win.")
    if guess in display :
        print(f"you have already guessed{guess}")

    if guess not in chosen_word :
        print("you gussed wrong you will lose a life")
        lives -=1
    if lives==0 :
          end_of =True
          print("you lose")

    print(logo.stages[lives])
