import argparse

from calculator import (
    future_value_monthly_deposit,
    calculate_total_invested,
    calculate_interest_earned
)

from utils import display_results


parser = argparse.ArgumentParser(
    description="Monthly Deposit Calculator with Annual Compounding"
)

parser.add_argument(
    "--monthly_deposit",
    type=float,
    required=True,
    help="Monthly deposit amount"
)

parser.add_argument(
    "--rate",
    type=float,
    required=True,
    help="Annual interest rate"
)

parser.add_argument(
    "--time_in_years",
    type=float,
    required=True,
    help="Investment duration in years"
)

args = parser.parse_args()

monthly_deposit = args.monthly_deposit
rate_of_interest = args.rate
time_period = args.time_in_years

final_amount = future_value_monthly_deposit(
    monthly_deposit,
    rate_of_interest,
    time_period
)

total_invested = calculate_total_invested(
    monthly_deposit,
    time_period
)

interest_earned = calculate_interest_earned(
    final_amount,
    total_invested
)

display_results(
    total_invested,
    interest_earned,
    final_amount,
    time_period
)