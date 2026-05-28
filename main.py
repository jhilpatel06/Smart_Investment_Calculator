import argparse

from calculator import (
    future_value_monthly_deposit,
    calculate_total_invested,
    calculate_interest_earned,
    required_monthly_deposit
)

from utils import (
    display_investment_results,
    display_retirement_results
)

from plots import (
    plot_financial_timeline,
    plot_investment_timeline
)


parser = argparse.ArgumentParser(
    description="Financial Planning Calculator"
)

# --------------------------------------------------
# Investment Mode Arguments
# --------------------------------------------------

parser.add_argument(
    "--monthly_deposit",
    type=float,
    help="Monthly investment amount"
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

# --------------------------------------------------
# Retirement Planning Arguments
# --------------------------------------------------

parser.add_argument(
    "--withdrawal_amount",
    type=float,
    help="Monthly withdrawal amount"
)

parser.add_argument(
    "--investment_years",
    type=float,
    help="Years spent investing"
)

parser.add_argument(
    "--withdrawal_years",
    type=float,
    help="Years spent withdrawing"
)

args = parser.parse_args()

# --------------------------------------------------
# Investment Growth Mode
# --------------------------------------------------

if (
    args.monthly_deposit is not None
    and args.time_in_years is not None
):

    final_amount, balances = future_value_monthly_deposit(
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

    display_investment_results(
        total_invested,
        interest_earned,
        final_amount,
        args.time_in_years
    )

    plot_investment_timeline(balances)

# --------------------------------------------------
# Retirement Planning Mode
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
        total_interest_earned,
        balances,
        invest_months,
        withdrawal_months
    ) = required_monthly_deposit(
        annual_rate=args.rate,
        investment_years=args.investment_years,
        withdrawal_years=args.withdrawal_years,
        monthly_withdrawal=args.withdrawal_amount
    )

    display_retirement_results(
        required_deposit,
        total_invested,
        total_withdrawn,
        total_interest_earned
    )

    plot_financial_timeline(
        balances,
        invest_months,
        withdrawal_months
    )