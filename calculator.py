def future_value_monthly_deposit(x, r, t):
    annual_rate = r / 100
    total_amount = 0

    for year in range(1, int(t) + 1):
        yearly_deposit = x * 12
        remaining_years = t - year + 1

        total_amount += yearly_deposit * ((1 + annual_rate) ** remaining_years)

    return round(total_amount, 2)


def calculate_total_invested(monthly_deposit, time_period):
    return round(monthly_deposit * 12 * time_period, 2)


def calculate_interest_earned(final_amount, total_invested):
    return round(final_amount - total_invested, 2)

def required_monthly_deposit(
    annual_rate,
    investment_years,
    withdrawal_years,
    monthly_withdrawal
):

    monthly_rate = (annual_rate / 100) / 12

    invest_months = int(investment_years * 12)
    withdrawal_months = int(withdrawal_years * 12)

    low = 0
    high = monthly_withdrawal * withdrawal_months

    while high - low > 0.01:

        monthly_deposit = (low + high) / 2

        balance = 0

        # Investment phase
        for _ in range(invest_months):

            balance += monthly_deposit
            balance += balance * monthly_rate

        # Withdrawal phase
        for _ in range(withdrawal_months):

            balance += balance * monthly_rate
            balance -= monthly_withdrawal

        if balance >= 0:
            high = monthly_deposit
        else:
            low = monthly_deposit

    required_deposit = round(high, 2)

    total_invested = round(
        required_deposit * invest_months,
        2
    )

    total_withdrawn = round(
        monthly_withdrawal * withdrawal_months,
        2
    )

    total_interest_earned = round(
        total_withdrawn - total_invested,
        2
    )

    return (
        required_deposit,
        total_invested,
        total_withdrawn,
        total_interest_earned
    )