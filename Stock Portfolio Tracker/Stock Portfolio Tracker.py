stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "AMZN": 3300
}

portfolio = {}
total_investment = 0

n = int(input("Enter number of stocks you want to add: "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        portfolio[stock_name] = quantity
    else:
        print("Stock not found in price list!")

print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock} -> Quantity: {qty}, Price: {price}, Value: {value}")

print(f"\nTotal Investment Value: {total_investment}")

with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        file.write(f"{stock}, {qty}, {price}, {value}\n")
    file.write(f"\nTotal Investment: {total_investment}")

print("\nPortfolio saved to portfolio.txt")