<div align="center">

![Banner](https://capsule-render.vercel.app/api?type=waving&color=timeGradient&height=250&section=header&text=Roulette-Game-CLI&fontSize=60&fontAlignY=35&desc=A%20cinematic%20terminal%20roulette%20suite%20with%20strategy%20engines%2C%20persistent%20sessions%2C%20achievements%2C%20and%20table-grade%20analytics.%20Play%2C%20learn%2C%20track%2C%20and%20export%20every%20spin%20from%20one%20fast%20Python%20CLI.&descAlignY=55&descSize=20)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Terminal](https://img.shields.io/badge/Interface-CLI-111827?style=for-the-badge&logo=gnometerminal&logoColor=white)
![Analytics](https://img.shields.io/badge/Analytics-Hot%20%2F%20Cold%20Numbers-FF006E?style=for-the-badge&logo=databricks&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-16A34A?style=for-the-badge&logo=opensourceinitiative&logoColor=white)

</div>

![Header](https://readme-typing-svg.demolab.com/?font=Righteous&weight=700&size=26&color=33C9FF&width=500&height=40&lines=High-Stakes+Terminal+Gameplay)

Roulette Game CLI turns a simple wheel spin into a full table-session simulator with multi-bets, strategy helpers, save files, leaderboards, achievements, and exportable statistics. It is built for players, learners, and terminal enthusiasts who want a polished casino-style loop without leaving the command line.

<table>
  <tr>
    <td width="50%" valign="top">

![Header](https://readme-typing-svg.demolab.com/?font=Righteous&weight=700&size=26&color=FF4ECD&width=500&height=40&lines=Core+Features)

- 🎯 Number, color, odd/even, high/low, and multi-bet modes
- 🧠 Martingale, Fibonacci, Conservative, and D'Alembert strategy helpers
- 💾 Save/load support with leaderboard persistence
- 📊 Win rate, streaks, profit/loss, best payout, and worst-loss tracking
- 🔥 Hot/cold number analytics driven by session history
- 🏆 Achievement checks for milestones and standout sessions

    </td>
    <td width="50%" valign="top">

![Code Snapshot](assets/code-snapshot.png)

    </td>
  </tr>
</table>

![Header](https://readme-typing-svg.demolab.com/?font=Righteous&weight=700&size=26&color=9DFF57&width=500&height=40&lines=Blazing+Fast+CLI+Demo)

![Demo](https://readme-typing-svg.demolab.com/?font=Fira+Code&duration=1500&pause=500&multiline=true&width=900&height=130&color=F8F8F2&background=282A3600&lines=%24+python+roulette.py;%3E+Choose+a+bet+type+and+amount;%3E+Spin+the+wheel+and+resolve+payouts;%3E+Review+stats%2C+save%2C+export%2C+or+climb+the+leaderboard)

![Header](https://readme-typing-svg.demolab.com/?font=Righteous&weight=700&size=26&color=FFB86C&width=500&height=40&lines=Runtime+Architecture)

```mermaid
flowchart TD
    A[Launch CLI] --> B[Render Table Menu]
    B --> C{Choose Action}
    C -->|Place Bet| D[Validate Bet and Balance]
    C -->|Strategy| E[Calculate Suggested Stake]
    C -->|Stats| F[Render Session Analytics]
    D --> G[Spin Wheel]
    G --> H[Resolve Payout]
    H --> I[Update Balance and History]
    I --> J[Check Achievements]
    J --> B
    E --> D
    F --> B
    C -->|Save or Load| K[Storage Layer]
    K --> B
    classDef entry fill:#33C9FF,stroke:#0B1020,color:#0B1020,stroke-width:2px
    classDef action fill:#FF4ECD,stroke:#2A0A1F,color:#FFFFFF,stroke-width:2px
    classDef engine fill:#9DFF57,stroke:#17320E,color:#0B1020,stroke-width:2px
    classDef data fill:#FFB86C,stroke:#4A2500,color:#0B1020,stroke-width:2px
    class A,B entry
    class C,D,E,G,H action
    class I,J engine
    class F,K data
```

![Header](https://readme-typing-svg.demolab.com/?font=Righteous&weight=700&size=26&color=33C9FF&width=500&height=40&lines=Quick+Start)

```bash
git clone https://github.com/mertefekurt/Roulette-Game-CLI.git
cd Roulette-Game-CLI
python roulette.py
```

<details>
<summary>🛠️ View CLI Reference / Advanced Config</summary>

| Key | Command |
| --- | --- |
| `1` | Bet on a number from 0 to 36 |
| `2` | Bet on red or black |
| `3` | Bet on odd or even |
| `4` | Bet on high or low |
| `5` | Build multiple bets for one spin |
| `6` | View statistics |
| `7` | View bet history |
| `8` | Save the game |
| `9` | Load the game |
| `a` | View leaderboard |
| `b` | Export statistics |
| `c` | Select a betting strategy |
| `d` | View achievements |
| `e` | Open the betting calculator |
| `f` | View hot/cold numbers |
| `r` | Repeat the previous bet |
| `0` | Exit the table |

| Setting | Default |
| --- | --- |
| Starting balance | `$1,000` |
| Minimum bet | `$10` |
| Maximum bet | `$10,000` |
| Number payout | `36x` |
| Even-money payout | `2x` |

Gambling systems do not change probability. Strategy modes are gameplay tools, not financial advice.

</details>

![Header](https://readme-typing-svg.demolab.com/?font=Righteous&weight=700&size=26&color=FF4ECD&width=500&height=40&lines=Project+Map)

```text
Roulette-Game-CLI/
├── roulette.py       # Main loop, wheel logic, and bet resolution
├── strategies.py     # Strategy helper implementations
├── achievements.py   # Milestone tracking
├── storage.py        # Saves, leaderboards, and exports
├── calculator.py     # Payout helper
├── config.py         # Table limits and constants
└── utils.py          # Formatting helpers
```
