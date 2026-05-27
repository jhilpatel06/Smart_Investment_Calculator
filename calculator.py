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