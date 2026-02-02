# 🧠 Mind Reading Game Using Python

A simple Python-based **mind reading game** where the computer predicts the player's next move (`0` or `1`) by learning from previous inputs.

The game adapts over time and becomes better at predicting patterns in player behavior.

---

## 🎮 How the Game Works

- The player enters either **0** or **1**
- The computer predicts the player's choice
- If the prediction is correct → **Computer scores**
- If the prediction is wrong → **Player scores**
- The first to reach **20 points** wins the game

---

## 🧠 Game Logic

- The game stores the **last two player inputs**
- Uses a small memory structure to track patterns
- A confidence bit decides whether to trust past behavior
- If no reliable pattern exists, prediction is random

This is similar to a **simple learning / prediction algorithm**.

---

## 📂 Project Structure

- mind_reader.py
- README.md
- requirements.txt


---

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/heyrevath/mind-reading-game.git


