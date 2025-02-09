import pygame, time, random





'''
1. generate random word and tell the user the length of the word
2. ask for user input on a letter
3. generate the hangman after every wrong letter 
'''
from wonderwords import RandomWord, Defaults, random_word



w = RandomWord()



word = w.random_words(word_min_length=5, word_max_length=7)

#print(word[0])

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


LW = len(word[0])


print("\nHere are the rules:")
print("\nYou have 7 lives till the hangman is fully hung.")
print("\nIf you are stuck on a word then do the command /help.")
print()
print("\nThe word is", LW, "letter long:")


userword = False
pointer = 0
blurred = []
lettersused = []
lives = 0


for i in range (LW):
    blurred.append("_")
userblur = ''.join(blurred)

print(userblur)





while userword == False:
    userletter = input("\nInput 1 letter/character:")
    pointer = 0
    if userletter == '/help':
        help = input("\nAre you sure you need help? \nThis command can only be used once! "
                     "\nUsing the /help command will burn one life and reveal two letters!"
                     "\nUse Y or N to answer (yes or no)"
                     "\n:")
        if help == 'Y':
            print("The two of the letters are:")
            print(word[0][random.randint(0, len(word[0]))])
#            print(word[0][random.randint(0, len(word[0]))])




    else:
        if userletter in lettersused:
            print("\nThe letter ", userletter, " has already been used once!")
            print("Use a different letter.")
            print("\n",''.join(blurred))

        else:
            lettersused.append(userletter)
            got_it_right = False
            for n in word[0]:
                if userletter == n:
                    blurred[pointer] = n
                    got_it_right = True
                pointer += 1

            if got_it_right:
                print("\nyou got the letter", userletter, "correct!")
                print(''.join(blurred))

            if not got_it_right:
                lives += 1#make lives go down not up
                print("\nThe letter", userletter, " is not part of this word!")

                if lives == 7:
                    print("\nThe word was:", word[0])

                    print('''\n
███████████████████████████████████████
█─▄─▄─█─█─█▄─▄▄─███▄─▄▄─█▄─▀█▄─▄█▄─▄▄▀█
███─███─▄─██─▄█▀████─▄█▀██─█▄▀─███─██─█
██▄▄▄██▄█▄█▄▄▄▄▄███▄▄▄▄▄█▄▄▄██▄▄█▄▄▄▄██''')
                    print("Thanks for playing!")

                    break
                else:
                    print(HANGMANPICS[lives])
                    print(7-lives, "lives left")


'''
    if lives == 7:
        print("the end!")
        break

'''



'''
- every life the new hangman image is printed 
- every life, the amount of lives left are printed
- every life lost a hint os given???
- compare every letter, example:
the word is _____
the word is __I__
- print out which letter is right/if not in the right position then tell player


'''




'''
4. After every wrong letter post a new image of hangman - print the images.
5. ever letter that is correct tell user that its correct.

https://wonderwords.readthedocs.io/en/latest/api_docs/random_word.html


'''