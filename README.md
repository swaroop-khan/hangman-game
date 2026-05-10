# 🎮 Hangman Game

A terminal-based Hangman game built in Python, with words fetched live from a random word API.

---

## 📖 About

This is a clean, single-file implementation of the classic Hangman game. Each session pulls a fresh word from a public API, so you're always guessing something new. Guess letters one at a time — the ASCII hangman drawing fills in with every wrong answer.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- `requests` library

### Install Dependencies

```bash
pip install requests
```

### Run the Game

```bash
python hangman.py
```

---

## 🕹️ How to Play

1. A random word is fetched from the API and displayed as blanks (e.g. `_ _ _ _ _`).
2. Type a single letter and press **Enter** to make a guess.
3. Correct guesses reveal the letter wherever it appears in the word.
4. Wrong guesses cost a life and progress the hangman drawing.
5. You start with **6 lives**.
6. **Win** by revealing the full word before lives run out.
7. **Lose** when the hangman is fully drawn (0 lives remaining).

### Rules
- One alphabetic letter per guess — nothing else is accepted.
- Guessing a letter you've already tried won't cost a life, but won't help either.

---

## 🌐 Random Word API

Words are fetched from:

```
https://random-word-api.herokuapp.com/word
```

A single request is made at the start of each game. If the API is unreachable for any reason, the game falls back to the word `"python"` so you can still play offline.

---

## ✨ Features

- ✅ Live word fetching from a public API
- ✅ Offline fallback if the API fails
- ✅ 7-stage ASCII hangman art updated after each wrong guess
- ✅ Real-time word progress display
- ✅ Input validation — single alpha characters only
- ✅ Duplicate guess detection
- ✅ Clear win/lose messages with the answer revealed on loss

---

## 📂 Project Structure

```
hangman.py   # Complete game — all logic in a single script
README.md    # Project documentation
```

---

## 📸 Sample Gameplay

```
🎮 Welcome to Hangman!
Guess the word letter by letter!

  +---+
  |   |
      |
      |
      |
      |
=========
Word: _ _ _ _ _

Guess a letter: a

Word: _ a _ _ _

Guess a letter: x
❌ Wrong guess! Lives left: 5

  +---+
  |   |
  O   |
      |
      |
      |
=========
Word: _ a _ _ _
```

---

## 🛠️ Customization

**Change the number of lives:**
```python
lives = 6  # increase for easier, decrease for harder
```

**Change the fallback word:**
```python
word = "python"  # used when the API is unavailable
```

**Swap the word source** — replace the API URL with any other that returns a JSON array:
```python
url = "https://random-word-api.herokuapp.com/word"
```

---

## 📄 License

This project is open source and free to use for learning and personal projects.
