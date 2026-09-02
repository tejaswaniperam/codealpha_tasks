# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}

portfolio = {}
total_investment = 0

print("=" * 40)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 40)

while True:

    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

        value = stock_prices[stock] * quantity
        total_investment += value

        print(f"{stock} added successfully.")
        print(f"Investment value: ${value}")

    except ValueError:
        print("Please enter a valid quantity.")

print("\n" + "=" * 40)
print("           YOUR PORTFOLIO")
print("=" * 40)

for stock, quantity in portfolio.items():

    value = stock_prices[stock] * quantity

    print(
        f"{stock}: {quantity} shares × "
        f"${stock_prices[stock]} = ${value}"
    )

print("-" * 40)
print(f"TOTAL INVESTMENT: ${total_investment}")
print("=" * 40)