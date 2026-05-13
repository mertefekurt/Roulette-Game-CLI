<div align="center">

![Roulette Game CLI banner](https://capsule-render.vercel.app/api?type=rect&height=190&color=random&text=Roulette%20Game%20CLI&fontColor=ffffff&desc=Strategy%2C%20stats%2C%20saves%2C%20and%20table%20pressure%20in%20Python&descAlign=50&descAlignY=67)

![License](https://img.shields.io/badge/license-MIT-dc2626?style=for-the-badge)
![Language](https://img.shields.io/badge/language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PRs](https://img.shields.io/badge/PRs-welcome-16a34a?style=for-the-badge)
![Status](https://img.shields.io/badge/build-passing-111827?style=for-the-badge)

</div>

![typing demo](https://readme-typing-svg.demolab.com?font=Fira+Code&duration=1500&pause=500&color=DC2626&background=11182700&width=900&lines=python+roulette.py;Place+single+or+multi-bets.;Track+streaks%2C+history%2C+and+profit.;Save+the+session+before+you+walk+away.)

## The Pitch

Most terminal games stop at a random number and a win-or-lose message. Roulette Game CLI adds the systems that make a table session interesting: multiple bet types, strategy helpers, persistent saves, achievements, hot/cold tracking, and exportable statistics.

## Feature Stack

| Area | Included |
| --- | --- |
| Bet types | Number, color, odd/even, high/low, and multiple bets |
| Strategy helpers | Martingale, Fibonacci, Conservative, and D'Alembert |
| Player state | Balance, history, win rate, streaks, best payout, worst loss |
| Persistence | Save/load game state and leaderboard support |
| Analysis | Hot/cold numbers, betting calculator, exported statistics |
| Progression | Achievement checks for milestones and standout sessions |

> Gambling systems do not change probability. Use the strategy modes as gameplay tools, not financial advice.

## Install And Play

```bash
git clone https://github.com/mertefekurt/Roulette-Game-CLI.git
cd Roulette-Game-CLI
python roulette.py
```

Optional starting balance:

```bash
ROULETTE_START_BALANCE=2500 python roulette.py
```

## Menu Keys

Press <kbd>1</kbd> through <kbd>5</kbd> for bets, <kbd>r</kbd> to repeat the previous bet, <kbd>c</kbd> to choose a strategy, and <kbd>0</kbd> to leave the table.

<details>
<summary>Full command table</summary>

| Key | Command |
| --- | --- |
| <kbd>1</kbd> | Bet on a number from 0 to 36 |
| <kbd>2</kbd> | Bet on red or black |
| <kbd>3</kbd> | Bet on odd or even |
| <kbd>4</kbd> | Bet on high or low |
| <kbd>5</kbd> | Create multiple bets for one spin |
| <kbd>6</kbd> | View statistics |
| <kbd>7</kbd> | View bet history |
| <kbd>8</kbd> | Save game |
| <kbd>9</kbd> | Load game |
| <kbd>a</kbd> | View leaderboard |
| <kbd>b</kbd> | Export statistics |
| <kbd>c</kbd> | Set betting strategy |
| <kbd>d</kbd> | View achievements |
| <kbd>e</kbd> | Open the betting calculator |
| <kbd>f</kbd> | View hot and cold numbers |

</details>

## Runtime Flow

```mermaid
stateDiagram-v2
    [*] --> Menu
    Menu --> BetEntry: choose bet
    Menu --> Strategy: c
    Menu --> Stats: 6 / 7 / f
    Strategy --> Menu: strategy selected
    BetEntry --> Spin: valid amount
    Spin --> Resolve: wheel result
    Resolve --> UpdatePlayer: payout and history
    UpdatePlayer --> Achievements: check milestones
    Achievements --> Menu: continue
    Menu --> Save: 8
    Save --> Menu
    Menu --> [*]: 0
    state UpdatePlayer {
      [*] --> Balance
      Balance --> Streaks
      Streaks --> Frequency
    }
    classDef payout fill:#fee2e2,stroke:#dc2626,color:#7f1d1d
    class Resolve,UpdatePlayer payout
```

## Project Anatomy

```text
Roulette-Game-CLI/
├── roulette.py       # Main loop, wheel logic, bet resolution
├── strategies.py     # Betting strategy implementations
├── achievements.py   # Milestone tracking
├── storage.py        # Saves, leaderboard, exports
├── calculator.py     # Payout helper
├── config.py         # Table limits and constants
└── utils.py          # Formatting helpers
```

## Table Rules

- Starting balance defaults to `$1,000`
- Minimum bet is `$10`
- Maximum bet is `$10,000`
- Number bets pay `36x`
- Even-money bets pay `2x`

## License

Released under the MIT License.
