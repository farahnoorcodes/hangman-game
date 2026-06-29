import random
words=["apple","ball","cat","dog","eagle","farah","gangster","heels","icecream","joker","king","lemon","monkey",
       "noor","owl","pasta","qatar","rimsha","summer","table","umberalla","van","window","xerography","you","zinger"]
stages = [
    """
  -----
|     |
|     O
|    /|\\
|    / \\
 ===""",
    """
  -----
|     |
|     O
|    /|\\
|    /
 ===""",
    """
  -----
|     |
|     O
|    /|\\
|
 ===""",
    """
  -----
|     |
|     O
|     |
|
 ===""",
    """
  -----
|     |
|     O
|
|
 ===""",
    """
  -----
|     |
|
|
|
 ===""",
    ]
chosen_word=random.choice(words)
display=[]
lives=5
game_over=False
guessed_letters=[]
for i in range(len(chosen_word)):
    display+='_'
print(display)
while not game_over:
    print(stages[lives])
    guessed_letter=input("guess a letter: ").lower()
    if guessed_letter in guessed_letters:
        print("you already guessed that letter!")
        continue
    guessed_letters.append(guessed_letter)
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print(stages[0])
            print("you LOSE!!!")
            print("the word is '",chosen_word,"'")

    if '_' not in display:
        game_over=True
        print("you WIN!!!")
