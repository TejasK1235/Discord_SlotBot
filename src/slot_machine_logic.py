import random

MAX_BET = 100
MIN_BET = 1
MAX_LINES = 3

ROWS = 3
COLS = 3

symbol_count = {
    "A": 8,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 10,
    "B": 4,
    "C": 3,
    "D": 2
}

class SlotMachine:

    def __init__(self) -> None:
        self.balances = {}



    def check_winnings(self, columns, lines, bet):
        winnings = 0
        winning_lines = []
        for line in range(lines):
            symbol = columns[0][line]
            for column in columns:
                symbol_to_check = column[line]
                if symbol != symbol_to_check:
                    break
            else:
                winnings += symbol_value[symbol] * bet
                winning_lines.append(line + 1)
        
        return winnings, winning_lines

    def spin_machine(self, rows, cols, symbols):
        all_symbols = []
        for symbol, symbol_count in symbols.items():
            for _ in range(symbol_count):
                all_symbols.append(symbol)

        columns = []
        for _ in range(rows):
            column = []
            copy_of_all_symbols = all_symbols[:]  # If not sliced will affect original list
            for _ in range(cols):
                value = random.choice(copy_of_all_symbols)
                copy_of_all_symbols.remove(value)
                column.append(value)
            columns.append(column)
        
        return columns
    

    def set_balance(self, user, amount):
        user_id = user.id
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                self.balances[user_id] = amount
                return f"Your balance has been set to ${amount}."
            else:
                return "Initial balance must be greater than zero"
        else:
            return "Please enter a number"
        

    def deposit(self, user, amount):
        user_id = user.id
        if user_id not in self.balances:
            return "Please set the initial balance before depositing more.\nRun command !setbalance <amount>"

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                self.balances[user_id] += amount
                return f"${amount} has been added to your balance.\nYour current balance is ${self.balances[user_id]}"
            else:
                return "Deposit amount must be greater than zero"
        else:
            return "Please enter a number"
        

    def print_machine(self, columns):
        rows_output = []
        for row in range(len(columns[0])):
            row_output = ""
            for i, column in enumerate(columns):
                row_output += column[row] + (" | " if i != len(columns) - 1 else "")
            rows_output.append(row_output)
        return "\n".join(rows_output)

    async def play(self, user, bet, lines):
        user_id = user.id
        if user_id not in self.balances:
            return "Enter your initial balance using command !setbalance <amount>"
        
        balance = self.balances[user_id]
        if balance < MIN_BET:
            return f"Insufficient balance. Your current balance is ${balance}"
        
        if not bet.isdigit() or not lines.isdigit(): 
            return "Bet and lines must be numbers"
        
        lines = int(lines)
        bet = int(bet)

        if bet < MIN_BET or bet > MAX_BET:
            return f"Bet must be between ${MIN_BET} and ${MAX_BET}."
        
        if lines < 1 or lines > MAX_LINES:
            return f"Lines must be between 1 and {MAX_LINES}."
        
        total_bet = lines * bet
        if total_bet > balance:
            return f"You don't have enough balance to bet ${total_bet}.\nYour current balance is ${balance}"
        
        balance -= total_bet
        slot = self.spin_machine(ROWS, COLS, symbol_count)
        machine_response = self.print_machine(slot)
        winnings, winning_lines = self.check_winnings(slot, lines, bet)
        balance += winnings
        self.balances[user_id] = balance

        result_msg = (
            f"Slot Machine Results:\n{machine_response}\n"
            f"You bet ${total_bet} on {lines} lines.\n"
            f"You won ${winnings} on lines {', '.join(map(str, winning_lines))}.\n"
            f"Your new balance is ${balance}."
        )

        return result_msg
