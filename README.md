# MatchBetting

A project for match betting analysis and automation.

## Description

This repository contains code for finding the lay stakes when creating a bet-builder with multiple outcomes. It will find the lay stakes that give the maximum "locked-in" profit[^1]. 

[^1] locked-in profit is the profit returned when the outcome with the lowest profit from your options occurs. For example, if I'll get £2.50 for a 1-0 win, £2.40 for 2-0 or £4.00 if the back loses then the locked-in profit is £2.40. 

The code is written to take any number of score options. But the number of score_names must match the number of odds. You can also use it for a boosted bet builder. Just enter the boosted odds and set the free bet stake to 0. There are other multi-lay calculators which already exist for this but this option maybe helpful if placing the same bet builder accross multiple offers as it saves copying the odds into different calculators. 

## Installation

```bash
# Clone the repository
git clone [repository-url]
cd MatchBetting
```

## Usage

```python3 multilay_adjuster.py
```

## Setup
Edit the initial lines of code for:
* lay odds
* back odds
* back stake
* free bet stake
* free bet return percentage (advise 0.8 for standard and 0.6 for bet builder)

## Requirements

- numpy, random, itertools

## License

This project is licensed under GNU General Public License v3.0 - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For questions or support, please open an issue.
