#  Hangman Game using Python

##  Project Overview

**Hangman Game** is a simple command-line game developed using Python.

The player has to guess a hidden word by entering one letter at a time. For every incorrect guess, the player loses one chance. The player wins if they correctly guess all the letters before the maximum number of incorrect attempts is reached.

This project is designed to practice Python fundamentals such as:

* Variables
* Strings
* Lists
* Loops
* Conditional statements
* Functions
* User input
* Random selection

---

#  Objectives

The main objectives of this project are:

* Create an interactive Hangman game.
* Randomly select a word.
* Allow the user to guess letters.
* Display the progress of the hidden word.
* Track incorrect guesses.
* Prevent repeated guesses.
* Display the final result.
* Practice Python programming concepts.

---

#  Technologies Used

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python        | Main programming language |
| Random module | Select a random word      |
| Command Line  | User interface            |

No external libraries are required.

---

#  Project Structure

```text
Hangman_Game/
│
├── hangman.py
└── README.md
```

---

#  How the Game Works

The game follows these steps:

```text
Start Game
    ↓
Select a Random Word
    ↓
Hide the Letters
    ↓
Ask Player to Enter a Letter
    ↓
Check the Letter
    ↓
Correct → Reveal Letter
    │
    └── Incorrect → Reduce Attempts
    ↓
Check Whether Word is Complete
    ↓
Win / Lose
    ↓
End Game
```

---

#  How to Run the Project

## Step 1: Install Python

Check whether Python is installed:

```bash
python --version
```

You should see something similar to:

```text
Python 3.x.x
```

---

## Step 2: Open the Project Folder

Open the project folder in **VS Code**, **PyCharm**, or Command Prompt.

Example:

```bash
cd "C:\Users\poornima\Hangman_Game"
```

---

## Step 3: Run the Program

If your Python file is called `hangman.py`, run:

```bash
python hangman.py
```

You can also run it directly from VS Code by clicking the **Run Python File** button.

---

# 🎮 How to Play

When the game starts, you will see something like:

```text
Welcome to Hangman!

Word: _ _ _ _ _

Guess a letter: a
```

If the letter is correct:

```text
Good guess!

Word: _ a _ _ _
```

If the letter is incorrect:

```text
Wrong guess!

Attempts remaining: 5
```

Continue guessing until you either:

* Guess the complete word → **WIN**
* Run out of attempts → **LOSE**

---

#  Example Game

Suppose the selected word is:

```text
PYTHON
```

Initially:

```text
_ _ _ _ _ _
```

Player enters:

```text
p
```

Output:

```text
P _ _ _ _ _
```

Player enters:

```text
y
```

Output:

```text
P Y _ _ _ _
```

Player continues:

```text
t
h
o
n
```

Finally:

```text
P Y T H O N
```

Output:

```text
 Congratulations!
You guessed the word!
```

---

#  Incorrect Guess Example

Suppose the word is:

```text
PYTHON
```

The player enters:

```text
z
```

Output:

```text
Wrong guess!
Attempts remaining: 5
```

If the player continues making incorrect guesses:

```text
Wrong guess!
Attempts remaining: 4

Wrong guess!
Attempts remaining: 3

Wrong guess!
Attempts remaining: 2

Wrong guess!
Attempts remaining: 1

Wrong guess!
Attempts remaining: 0
```

Then:

```text
 Game Over!

The word was: PYTHON
```

---

#  Main Features

### 1. Random Word Selection

The program can select a word randomly from a predefined list.

Example:

```python
words = [
    "python",
    "computer",
    "programming",
    "developer",
    "database"
]
```

The `random` module can be used to select the word.

---

### 2. Hidden Word

The letters of the selected word are hidden initially.

For example:

```text
_ _ _ _ _ _
```

---

### 3. Letter Guessing

The player enters one letter at a time.

Example:

```text
Guess a letter: p
```

---

### 4. Correct Guess

If the guessed letter exists in the word, it is revealed.

```text
P _ _ _ _ _
```

---

### 5. Incorrect Guess

If the letter does not exist, the number of remaining attempts decreases.

```text
Wrong guess!

Attempts remaining: 5
```

---

### 6. Repeated Guess Detection

The program can prevent the player from entering the same letter multiple times.

Example:

```text
You already guessed 'p'.
Try another letter.
```

---

### 7. Win Condition

The player wins when all letters are correctly guessed.

```text
 You Win!
```

---

### 8. Lose Condition

The player loses when all attempts are used.

```text
 You Lose!
The word was: PYTHON
```

---

#  Python Concepts Used

This project helps practice several important Python concepts.

### Variables

```python
word = "python"
attempts = 6
```

### Lists

```python
words = ["python", "java", "database"]
```

### Loops

```python
while attempts > 0:
    ...
```

### Conditions

```python
if guess in word:
    print("Correct!")
else:
    print("Wrong!")
```

### Functions

```python
def play_hangman():
    ...
```

### Sets

A set can be used to store letters already guessed:

```python
guessed_letters = set()
```

### Random Module

```python
import random

word = random.choice(words)
```

---

#  Game Logic

The main game logic is:

```text
1. Choose a word.
2. Create hidden blanks.
3. Set the number of attempts.
4. Ask the player for a letter.
5. Check whether the letter exists.
6. Reveal the letter if correct.
7. Reduce attempts if incorrect.
8. Check whether the entire word has been guessed.
9. Continue until the player wins or loses.
```

---

#  Common Problems

## Python is not recognized

If you get:

```text
'python' is not recognized as an internal or external command
```

Python may not be added to your system PATH.

Try:

```bash
py hangman.py
```

---

## Invalid Input

The program should ideally accept only one alphabetic character.

For example:

```text
Guess a letter: ab
```

should produce:

```text
Please enter only one letter.
```

---

## Repeated Letter

If the user enters a previously guessed letter:

```text
Guess a letter: p
```

the program should display:

```text
You already guessed that letter.
```

---

#  Future Improvements

The basic Hangman game can be improved by adding:

*  GUI using Tkinter
*  Sound effects
*  Score system
*  Visual Hangman drawing
*  Different word categories
*  Difficulty levels
*  Two-player mode
*  Timer
*  High-score storage
*  Web version using Flask or FastAPI

---

#  Example Categories

You can organize words into categories such as:

```text
Animals
---------
tiger
elephant
lion
elephant

Programming
------------
python
java
javascript
database

Countries
---------
india
japan
canada
brazil
```

The player could select a category before starting the game.

---

# 📈 Project Learning Outcome

After completing this project, you will understand how to:

* Write a Python command-line application.
* Use loops and conditions.
* Work with strings and lists.
* Create and use functions.
* Handle user input.
* Use the `random` module.
* Build game logic.
* Handle invalid and repeated input.
* Structure a small Python project.

---

#  Author

*Poornima*

Python Beginner Project

---

#  Conclusion

The Hangman Game is a beginner-friendly Python project that combines several fundamental programming concepts into one interactive application.

The overall process is:

```text
Random Word
     ↓
Hide Word
     ↓
Player Guess
     ↓
Check Letter
     ↓
Correct ─────→ Reveal Letter
     │
     ↓
Incorrect ───→ Reduce Attempt
     │
     ↓
Check Word
     ↓
WIN / LOSE
```

It is a good project for beginners to understand **loops, conditions, functions, strings, lists, sets, user input, and game logic**.
interface

# License

Free to use for learning purposes
