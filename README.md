# 🔢 Higher-Lower Follower Game

This is a simple command-line game built with Python where you compare two celebrities or brands and guess which one has more Instagram followers.

## 🎮 Gameplay

You are shown two public figures (A and B), along with their descriptions and countries. Your goal is to guess which one has more Instagram followers. If you're correct, your score increases by 1 and the game continues. If you're wrong, the game ends and your final score is displayed.

## 🧠 How It Works

- The game uses a predefined list of dictionaries, each containing:
  - `name`
  - `follower_count`
  - `description`
  - `country`
- Python's `random.choice()` is used to select two different entries for each round.
- Input is taken from the user (`A` or `B`) to choose who they think has more followers.

## 🛠️ How to Run

Make sure you have Python installed. Then, clone this repository and run the game:

```bash
python main.py
