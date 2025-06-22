# 🎰 Discord SlotBot

Discord SlotBot is a fun and simple slot machine game built as a Discord bot using Python. Users can set balances, deposit money, and bet on 1 to 3 lines to try their luck — all within Discord chat!

---

## 🚀 Features

- 🎯 Set your initial balance using a command.
- 💰 Deposit additional money anytime.
- 🎲 Bet on 1, 2, or 3 lines.
- 🎰 Visually rendered slot machine using text.
- 🏆 Win money based on symbol matches and predefined values.

---

## ⚙️ Commands

Here are the main commands available:

| Command | Description |
|--------|-------------|
| `!setbalance <amount>` | Sets your starting balance. |
| `!deposit <amount>` | Adds money to your current balance. |
| `!slot <bet> <lines>` | Spins the slot machine with the specified bet and number of lines (1–3). |

---

## 🛠️ Tech Stack

- **Language**: Python
- **Library**: `discord.py`
- **Other**: `random`, `dotenv` for environment variable management

---

## 📦 Installation & Setup

### 1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/discord_slotbot.git
   cd discord_slotbot
   ```

### 2. Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```
#### Create a .env file:
  ```bash
  DISCORD_TOKEN=your_discord_bot_token_here
  ```

#### Run the bot:
  ```bash
  python main.py
  ```
---

## 📸 Demo

Gameplay screenshots are available in the /demo folder.

---
👤 Author

Tejas Kothavale
