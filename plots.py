import matplotlib.pyplot as plt


def plot_financial_timeline(
    balances,
    investment_months,
    withdrawal_months
):

    total_months = investment_months + withdrawal_months

    # Convert months to years
    years = [month / 12 for month in range(total_months + 1)]

    # Convert balance to lakhs
    balances_in_lakhs = [
        balance / 100000 for balance in balances
    ]

    plt.figure(figsize=(12, 6))

    plt.plot(years, balances_in_lakhs)

    # Retirement start marker
    plt.axvline(
        x=investment_months / 12,
        linestyle="--",
        label="Retirement Start"
    )

    plt.xlabel("Years")

    plt.ylabel("Balance (Lakhs ₹)")

    plt.title(
        "Investment and Retirement Timeline"
    )

    plt.grid(True)

    plt.legend()

    plt.show()

def plot_investment_timeline(balances):

    years = [
        month / 12
        for month in range(len(balances))
    ]

    balances_in_lakhs = [
        balance / 100000
        for balance in balances
    ]

    plt.figure(figsize=(12, 6))

    plt.plot(years, balances_in_lakhs)

    plt.xlabel("Years")

    plt.ylabel("Balance (Lakhs ₹)")

    plt.title(
        "Investment Growth Timeline"
    )

    plt.grid(True)

    plt.show()