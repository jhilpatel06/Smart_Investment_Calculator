def format_indian_currency(amount):

    amount = f"{amount:.2f}"

    integer_part, decimal_part = amount.split(".")

    if len(integer_part) <= 3:

        return integer_part + "." + decimal_part

    last_three = integer_part[-3:]

    remaining = integer_part[:-3]

    parts = []

    while len(remaining) > 2:

        parts.insert(0, remaining[-2:])

        remaining = remaining[:-2]

    if remaining:

        parts.insert(0, remaining)

    formatted = ",".join(parts) + "," + last_three

    return formatted + "." + decimal_part


def display_investment_results(
    total_invested,
    interest_earned,
    final_amount,
    time_period
):

    print(
        f"Total invested amount: "
        f"{format_indian_currency(total_invested)}"
    )

    print(
        f"Interest earned: "
        f"{format_indian_currency(interest_earned)}"
    )

    print(
        f"Final amount after {time_period} years: "
        f"{format_indian_currency(final_amount)}"
    )


def display_retirement_results(
    required_deposit,
    total_invested,
    total_withdrawn,
    total_interest_earned
):

    print(
        f"Required monthly deposit: "
        f"{format_indian_currency(required_deposit)}"
    )

    print(
        f"Total money invested: "
        f"{format_indian_currency(total_invested)}"
    )

    print(
        f"Total money withdrawn: "
        f"{format_indian_currency(total_withdrawn)}"
    )

    print(
        f"Total interest earned: "
        f"{format_indian_currency(total_interest_earned)}"
    )