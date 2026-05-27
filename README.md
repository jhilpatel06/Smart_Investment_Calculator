# Monthly Investment Calculator

A Python command-line application that calculates the future value of monthly deposits using annual compound interest.

The program allows users to:
- Deposit a fixed amount every month
- Apply annual compound interest
- Calculate total invested amount
- Calculate interest earned
- Display the final accumulated amount after a given number of years

---

# Features

- Command line input using `argparse`
- Annual compound interest calculation
- Monthly deposit support
- Output values rounded to 2 decimal places
- Beginner-friendly Python implementation

---

# Technologies Used

- Python 3
- argparse module

---

# Formula Used

Future value is calculated using the compound interest formula:

\[
A = P(1+r)^t
\]

Where:
- \(P\) = yearly deposited amount
- \(r\) = annual interest rate
- \(t\) = remaining compounding years

Each year's deposits are compounded separately and added to the final amount.

---

# Project Structure

```bash
interest.py
README.md