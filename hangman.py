import requests

# ---------------- HANGMAN STAGES ---------------- #

stages = [

# 0 lives left
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''',

# 1 life left
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''',

# 2 lives left
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''',

# 3 lives left
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',

# 4 lives left
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',

# 5 lives left
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',

# 6 lives left
'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

# ---------------- FETCH RANDOM WORD ---------------- #

try:
    url = "https://random-word-api.herokuapp.com/word"

    response = requests.get(url)

    # Convert API response into Python list
    word = response.json()[0].lower()

except:
    print("⚠️ API failed. Using default word.")
    word = "python"

# ---------------- GAME VARIABLES ---------------- #

guessed_letters = []
lives = 6

print("🎮 Welcome to Hangman!")
print("\nGuess the word letter by letter!")

# ---------------- GAME LOOP ---------------- #

while lives > 0:

    # Show hangman stage
    print(stages[lives])

    # Build display word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    # Win check
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word!")
        break

    # User input
    guess = input("\nGuess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Enter only ONE alphabet letter.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    # Store guessed letter
    guessed_letters.append(guess)

    # Wrong guess
    if guess not in word:
        lives -= 1
        print(f"❌ Wrong guess! Lives left: {lives}")

# ---------------- GAME OVER ---------------- #

if lives == 0:
    print(stages[0])
    print(f"\n💀 Game Over! The word was: {word}")