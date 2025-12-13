# Roulette Game CLI

A feature-rich command-line roulette game built with Python.

## Features

### Betting Options
- Place bets on numbers (0-36), colors (red/black), odd/even, high/low
- Multiple bets in a single round
- Quick bet amounts (a: $10, b: $50, c: $100, d: $500)
- Repeat last bet with 'r' key
- Maximum bet limit: $10,000
- Minimum bet: $10

### Betting Strategies
- **Martingale**: Double bet after each loss
- **Fibonacci**: Use Fibonacci sequence for bet amounts
- **Conservative**: Reduce bet after 3 consecutive losses
- **D'Alembert**: Increase by base amount on loss, decrease on win

### Game Features
- Track your balance with low balance warnings
- View detailed statistics (wins, losses, win rate, profit)
- Win/loss streak tracking (current and maximum streaks)
- Hot/Cold numbers tracking (most/least frequent numbers)
- Bet history (last 5 bets)
- Achievements system
- Leaderboard (top 10 players)
- Save/Load game state
- Export statistics to file
- Betting calculator for payout calculations

## How to Run

```bash
python roulette.py
```

### Configuration

- `ROULETTE_START_BALANCE`: optional environment variable to set the starting balance (default: 1000).
- Starting balance: $1,000
- Minimum bet: $10
- Maximum bet: $10,000

## Menu Options

- `1-4`: Place single bets (number, color, odd/even, high/low)
- `5`: Multiple bets
- `r`: Repeat last bet (if available)
- `6`: View statistics
- `7`: View bet history
- `8`: Save game
- `9`: Load game
- `a`: View leaderboard
- `b`: Export statistics
- `c`: Set betting strategy
- `d`: View achievements
- `e`: Betting calculator
- `f`: View hot/cold numbers
- `0`: Quit



