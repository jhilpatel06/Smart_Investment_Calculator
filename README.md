# Financial Planning Calculator

A modular Python command-line application for investment growth and retirement planning using compound interest.

The project supports:
- Monthly investment growth calculation
- Retirement planning simulation
- Safe withdrawal modeling
- Compound interest calculations
- Command-line interface using `argparse`

---

# Features

## Investment Mode
- Calculates future value of monthly investments
- Computes total invested amount
- Computes interest earned
- Supports annual compounding

## Retirement Planning Mode
- Calculates required monthly investment
- Simulates retirement withdrawals
- Calculates:
  - total invested money
  - total withdrawn money
  - total interest earned

## Software Features
- Modular project structure
- Command line interface
- Financial simulation using loops
- Binary search optimization
- Rounded outputs to 2 decimal places

---

# Project Structure

```bash
project/
│
├── main.py
├── calculator.py
├── utils.py
└── README.md
```

---

# Modules

## main.py

Acts as the entry point of the application.

Responsibilities:
- Parse command-line arguments
- Select program mode
- Call required calculator functions
- Display results

---

## calculator.py

Contains all financial calculation logic.

Functions:
- `future_value_monthly_deposit()`
- `calculate_total_invested()`
- `calculate_interest_earned()`
- `required_monthly_deposit()`

---

## utils.py

Handles formatted output display.

Functions:
- `display_results()`

---

# Financial Logic

The application models two phases:

---

# Phase 1 — Investment Phase

User deposits money every month.

Each month:
1. money is deposited
2. interest is added
3. balance grows continuously

Future value is based on compound growth.

Compound interest formula:

\[
A = P(1+r)^t
\]

Where:
- \(P\) = principal
- \(r\) = interest rate
- \(t\) = time

---

# Phase 2 — Retirement Withdrawal Phase

After investment years:
- deposits stop
- monthly withdrawals begin
- remaining balance still earns interest

Each month:
1. interest gets added
2. withdrawal happens
3. remaining balance keeps compounding

Goal:
- ensure money lasts exactly for retirement duration

---

# Binary Search Optimization

The program uses Binary Search to calculate the required monthly deposit.

Reason:
- smaller deposits → money exhausts early
- larger deposits → money survives longer

Since the solution boundary is monotonic, Binary Search efficiently finds the minimum required deposit.

Time complexity:

```text
O(log N × total_months)
```

---

# Installation

## Clone Project

```bash
git clone <repository_url>
```

---

# Requirements

- Python 3.x

No external libraries required.

---

# How to Run

---

# 1. Investment Mode

Calculates future investment value.

## Command

```bash
python main.py --monthly_deposit 1000 --rate 10 --time_in_years 5
```

## Output Example

```text
Total invested amount: 60000.00
Interest earned: 20114.80
Final amount after 5.0 years: 80114.80
```

---

# 2. Retirement Planning Mode

Calculates how much must be invested monthly so retirement withdrawals remain sustainable.

## Command

```bash
python main.py --rate 10 --withdrawal_amount 50000 --investment_years 15 --withdrawal_years 20
```

## Output Example

```text
Required monthly deposit: 12873.44
Total money invested: 2317219.20
Total money withdrawn: 12000000.00
Total interest earned: 9682780.80
```

---

# Command Line Arguments

| Argument | Description |
|---|---|
| `--monthly_deposit` | Monthly investment amount |
| `--rate` | Annual interest rate |
| `--time_in_years` | Investment duration |
| `--withdrawal_amount` | Monthly retirement withdrawal |
| `--investment_years` | Years spent investing |
| `--withdrawal_years` | Years spent withdrawing |

---

# Core Functions

---

## future_value_monthly_deposit()

Calculates future value of monthly investments.

### Parameters

| Parameter | Meaning |
|---|---|
| `x` | Monthly deposit |
| `r` | Annual interest rate |
| `t` | Time in years |

---

## required_monthly_deposit()

Calculates minimum monthly investment required for retirement sustainability.

### Parameters

| Parameter | Meaning |
|---|---|
| `annual_rate` | Annual interest rate |
| `investment_years` | Investment duration |
| `withdrawal_years` | Retirement duration |
| `monthly_withdrawal` | Monthly withdrawal amount |

---

# Example Financial Scenario

Suppose:

- You want ₹50,000/month after retirement
- Retirement lasts 20 years
- You can invest for 15 years
- Interest rate is 10%

The program calculates:
- required monthly investment
- total invested capital
- total withdrawal amount
- wealth generated through compounding

---

# Learning Outcomes

This project demonstrates:
- Python modularization
- Command-line interfaces
- Financial mathematics
- Compound interest modeling
- Binary search optimization
- Simulation-based computation
- Clean software architecture

---

# Future Improvements

Possible extensions:
- Inflation adjustment
- Tax calculations
- Monthly compounding selection
- Graph visualization using matplotlib
- GUI application
- Web dashboard
- CSV/PDF export
- FIRE calculator
- SIP comparison tool
- Real stock market return simulation

---

# Example Project Flow

```text
User Input
    ↓
main.py
    ↓
calculator.py
    ↓
Financial Simulation
    ↓
utils.py
    ↓
Formatted Output
```

---

# Sample Commands

## Investment Growth

```bash
python main.py --monthly_deposit 2000 --rate 12 --time_in_years 10
```

## Retirement Planning

```bash
python main.py --rate 8 --withdrawal_amount 40000 --investment_years 20 --withdrawal_years 25
```

---
