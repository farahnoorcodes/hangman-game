# Hangman Game 

A classic console-based Hangman game where the player guesses letters to reveal a hidden word before running out of lives. Features ASCII art that builds up the hangman as wrong guesses are made.

## Features

- Random word selection from a built-in word list
- ASCII art hangman that progresses with each wrong guess
- 5 lives before the game ends
- Repeat-guess detection — guessing the same letter twice won't cost an extra life
- Win/lose detection with the correct word revealed on loss

## Tech Stack

- **Language:** Python 3
- **Module used:** `random`

## How It Works

1. The program picks a random word from the `words` list.
2. The word is displayed as a row of underscores (`_`), one per letter.
3. The player guesses one letter at a time.
4. If the letter is in the word, it's revealed in its correct position(s).
5. If the letter is wrong, a life is lost and the hangman drawing progresses.
6. Guessing the same letter again doesn't cost a life — the game just lets you know you've already tried it.
7. The game ends when:
   - All letters are revealed → Win
   - Lives reach 0 → Lose, and the word is revealed

## Sample Run

```
['_', '_', '_']

  -----
|     |
|
|
|
 ===
guess a letter: c
['c', '_', '_']

  -----
|     |
|     O
|
|
 ===
guess a letter: a
['c', 'a', 't']
you WIN!!!
```

## Getting Started

### Run
```bash
python3 hangman.py
```

## Author

**Farah Noor**
<div>
    GitHub: [farahnoorcodes](https://github.com/farahnoorcodes)
</div>
