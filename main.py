import argparse

from calculator import (
    future_value_monthly_deposit,
    calculate_total_invested,
    calculate_interest_earned,
    required_monthly_deposit
)

from utils import display_results


parser = argparse.ArgumentParser(
    description="Investment and Retirement Calculator"
)

# Existing calculator arguments
parser.add_argument(
    "--monthly_deposit",
    type=float,
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
    help="Investment duration in years"
)

# New retirement planning arguments
parser.add_argument(
    "--withdrawal_amount",
    type=float,
    help="Monthly withdrawal amount after retirement"
)

parser.add_argument(
    "--investment_years",
    type=float,
    help="Years for investment phase"
)

parser.add_argument(
    "--withdrawal_years",
    type=float,
    help="Years for withdrawal phase"
)

args = parser.parse_args()

# --------------------------------------------------
# Existing SIP calculation
# --------------------------------------------------

if (
    args.monthly_deposit is not None
    and args.time_in_years is not None
):

    final_amount = future_value_monthly_deposit(
        args.monthly_deposit,
        args.rate,
        args.time_in_years
    )

    total_invested = calculate_total_invested(
        args.monthly_deposit,
        args.time_in_years
    )

    interest_earned = calculate_interest_earned(
        final_amount,
        total_invested
    )

    display_results(
        total_invested,
        interest_earned,
        final_amount,
        args.time_in_years
    )

# --------------------------------------------------
# Retirement planning calculation
# --------------------------------------------------

elif (
    args.withdrawal_amount is not None
    and args.investment_years is not None
    and args.withdrawal_years is not None
):

    (
        required_deposit,
        total_invested,
        total_withdrawn,
        total_interest_earned
    ) = required_monthly_deposit(
        annual_rate=args.rate,
        investment_years=args.investment_years,
        withdrawal_years=args.withdrawal_years,
        monthly_withdrawal=args.withdrawal_amount
    )

    print(
        f"Required monthly deposit: "
        f"{required_deposit:.2f}"
    )

    print(
        f"Total money invested: "
        f"{total_invested:.2f}"
    )

    print(
        f"Total money withdrawn: "
        f"{total_withdrawn:.2f}"
    )

    print(
        f"Total interest earned: "
        f"{total_interest_earned:.2f}"
    )

else:

    print("Invalid arguments provided.")