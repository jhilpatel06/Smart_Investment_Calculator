def future_value_monthly_deposit(x, r, t):

    annual_rate = r / 100

    months = int(t * 12)

    balance = 0

    balances = [0]

    for month in range(1, months + 1):

        # Monthly deposit
        balance += x

        # Annual compounding
        if month % 12 == 0:

            balance += balance * annual_rate

        balances.append(balance)

    return round(balance, 2), balances

def calculate_total_invested(monthly_deposit, time_period):

    return round(
        monthly_deposit * 12 * time_period,
        2
    )


def calculate_interest_earned(final_amount, total_invested):

    return round(
        final_amount - total_invested,
        2
    )


def required_monthly_deposit(
    annual_rate,
    investment_years,
    withdrawal_years,
    monthly_withdrawal
):

    annual_rate = annual_rate / 100

    invest_months = int(investment_years * 12)

    withdrawal_months = int(withdrawal_years * 12)

    low = 0

    high = monthly_withdrawal * withdrawal_months

    final_balances = []

    while high - low > 0.01:

        monthly_deposit = (low + high) / 2

        balance = 0

        balances = [0]

        # Investment phase
        for month in range(1, invest_months + 1):

            balance += monthly_deposit

            if month % 12 == 0:

                balance += balance * annual_rate

            balances.append(balance)

        # Withdrawal phase
        for month in range(1, withdrawal_months + 1):

            if month % 12 == 0:

                balance += balance * annual_rate

            balance -= monthly_withdrawal

            balances.append(balance)

        if balance >= 0:

            high = monthly_deposit

            final_balances = balances

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
        total_interest_earned,
        final_balances,
        invest_months,
        withdrawal_months
    )