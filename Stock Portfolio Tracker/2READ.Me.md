#  Stock Portfolio Tracker using Python

##  Project Overview

**Stock Portfolio Tracker** is a Python-based application that allows users to maintain and track their stock investments.

The application stores information about stocks purchased by the user, such as:

* Stock symbol
* Company name
* Number of shares
* Purchase price
* Current price
* Investment value
* Profit or loss

The application calculates the overall portfolio value and shows whether the user is making a profit or a loss.

This project is useful for learning **Python programming, data handling, calculations, and basic financial application development**.

---

#  Objectives

The main objectives of this project are:

* Add stocks to a portfolio.
* Store stock information.
* Track the number of shares.
* Calculate investment amount.
* Calculate current portfolio value.
* Calculate profit or loss.
* Display portfolio information.
* Update stock prices.
* Remove stocks from the portfolio.
* Calculate total portfolio value.

---

#  Technologies Used

| Technology           | Purpose                    |
| -------------------- | -------------------------- |
| Python               | Main programming language  |
| JSON / CSV           | Store portfolio data       |
| Functions            | Organize application logic |
| Lists / Dictionaries | Store stock information    |
| `datetime`           | Track dates                |
| Command Line         | User interface             |

If you connect the project to a live stock-price API, an API client/library can also be added.

---

#  Project Structure

```text
Stock_Portfolio_Tracker/
│
├── stock_tracker.py
├── portfolio.json
└── README.md
```

If your project uses CSV instead:

```text
Stock_Portfolio_Tracker/
│
├── stock_tracker.py
├── portfolio.csv
└── README.md
```

---

#  How the Application Works

The application follows this workflow:

```text
Start Application
       ↓
Display Menu
       ↓
Add / View / Update / Delete Stock
       ↓
Calculate Investment
       ↓
Calculate Current Value
       ↓
Calculate Profit / Loss
       ↓
Display Portfolio
       ↓
Save Data
       ↓
Exit
```

---

#  Stock Information

Each stock can contain information such as:

```text
Symbol       : AAPL
Company      : Apple
Quantity     : 10
Purchase Price: $150
Current Price : $180
```

The program can then calculate:

```text
Investment Value = Quantity × Purchase Price

Current Value = Quantity × Current Price

Profit/Loss = Current Value - Investment Value
```

---

#  Example Calculation

Suppose the user buys:

```text
Stock       : ABC
Quantity    : 10
Buy Price   : ₹100
Current Price: ₹120
```

### Investment

```text
10 × ₹100 = ₹1,000
```

### Current Value

```text
10 × ₹120 = ₹1,200
```

### Profit

```text
₹1,200 - ₹1,000 = ₹200
```

Therefore:

```text
Profit = ₹200
```

---

#  How to Run the Project

## Step 1: Install Python

Check whether Python is installed:

```bash
python --version
```

You should see something similar to:

```text
Python 3.x.x
```

---

## Step 2: Open the Project Folder

Open the project in VS Code or PyCharm.

Example:

```bash
cd "C:\Users\poornima\Stock_Portfolio_Tracker"
```

---

## Step 3: Run the Application

If your Python file is named `stock_tracker.py`:

```bash
python stock_tracker.py
```

---

#  Application Menu

When the program starts, it can display:

```text
=================================
      STOCK PORTFOLIO TRACKER
=================================

1. Add Stock
2. View Portfolio
3. Update Stock
4. Delete Stock
5. Calculate Portfolio Value
6. Calculate Profit/Loss
7. Exit

Enter your choice:
```

---

#  Adding a Stock

Select:

```text
1. Add Stock
```

Example input:

```text
Enter stock symbol: AAPL
Enter company name: Apple
Enter quantity: 10
Enter purchase price: 150
Enter current price: 180
```

Output:

```text
Stock added successfully!
```

---

#  Viewing Portfolio

Select:

```text
2. View Portfolio
```

Example output:

```text
========================================
             MY PORTFOLIO
========================================

Symbol    Company       Quantity   Buy Price   Current Price
-------------------------------------------------------------
AAPL      Apple         10         ₹150         ₹180
GOOG      Google        5          ₹120         ₹140
TSLA      Tesla         8          ₹200         ₹220
```

---

#  Portfolio Value

The application calculates the current value of all stocks.

Example:

```text
AAPL → 10 × ₹180 = ₹1,800
GOOG → 5 × ₹140  = ₹700
TSLA → 8 × ₹220  = ₹1,760
```

Total:

```text
Portfolio Value = ₹4,260
```

---

#  Profit and Loss

The application calculates profit or loss for each stock.

Example:

```text
AAPL
Investment = ₹1,500
Current    = ₹1,800
Profit     = ₹300
```

The portfolio summary could display:

```text
Total Investment : ₹3,500
Current Value    : ₹4,260
Total Profit     : ₹760
```

---

#  Updating a Stock

Select:

```text
3. Update Stock
```

Example:

```text
Enter stock symbol: AAPL
Enter new current price: ₹190
```

Output:

```text
Stock price updated successfully!
```

The portfolio value and profit/loss will then be recalculated.

---

#  Deleting a Stock

Select:

```text
4. Delete Stock
```

Example:

```text
Enter stock symbol: TSLA
```

Output:

```text
TSLA removed from portfolio.
```

---

#  Data Storage

The portfolio can be stored in a JSON file.

Example:

```json
[
    {
        "symbol": "AAPL",
        "company": "Apple",
        "quantity": 10,
        "purchase_price": 150,
        "current_price": 180
    }
]
```

This allows the portfolio to remain available even after closing the program.

---

#  Python Concepts Used

This project helps practice:

### Variables

```python
quantity = 10
purchase_price = 150
```

### Dictionaries

```python
stock = {
    "symbol": "AAPL",
    "quantity": 10,
    "purchase_price": 150
}
```

### Lists

```python
portfolio = []
```

### Functions

```python
def add_stock():
    pass
```

### Loops

```python
for stock in portfolio:
    print(stock)
```

### Conditional Statements

```python
if profit > 0:
    print("Profit")
else:
    print("Loss")
```

### File Handling

```python
with open("portfolio.json", "w") as file:
    ...
```

---

#  Main Features

### 1. Add Stock

Allows users to add a new stock to their portfolio.

### 2. View Portfolio

Displays all stocks currently held.

### 3. Update Stock

Allows the user to update the current price or other information.

### 4. Delete Stock

Removes a stock from the portfolio.

### 5. Calculate Investment

Calculates the amount originally invested.

### 6. Calculate Current Value

Calculates the present value based on the stored current price.

### 7. Calculate Profit/Loss

Determines whether the investment has increased or decreased in value.

### 8. Save Portfolio

Stores portfolio information in a file.

---

#  Example Run

```text
=================================
      STOCK PORTFOLIO TRACKER
=================================

1. Add Stock
2. View Portfolio
3. Update Stock
4. Delete Stock
5. Portfolio Value
6. Profit/Loss
7. Exit

Enter your choice: 1

Enter stock symbol: AAPL
Enter company name: Apple
Enter quantity: 10
Enter purchase price: 150
Enter current price: 180

Stock added successfully!

Enter your choice: 5

Total Portfolio Value: ₹1800
```

---

#  Important Note About Stock Prices

A basic version of this project can use **manually entered current prices**.

For example:

```text
Purchase Price = ₹100
Current Price = ₹120
```

For a more advanced version, the application can obtain current market prices through a suitable financial-data API.

Live market prices may change frequently, and API availability, rate limits, and market hours should be considered.

---

#  Future Improvements

The project can be upgraded with:

*  Graphs and charts
*  Live stock prices
*  Historical price charts
*  Price alerts
*  Portfolio performance reports
*  SQLite database
*  Tkinter GUI
*  Flask/FastAPI web application
*  User login
*  Mobile-friendly interface
*  Sector-wise portfolio analysis
*  Percentage return calculation
*  Transaction history
*  Investment date tracking

---

#  Advanced Portfolio Example

An advanced portfolio record could contain:

```text
Symbol          : AAPL
Company         : Apple
Quantity        : 10
Purchase Price  : ₹15,000
Current Price   : ₹18,000
Investment      : ₹15,000
Current Value   : ₹18,000
Profit          : ₹3,000
Return          : 20%
```

---

#  Project Learning Outcomes

After completing this project, you will understand:

* How to build a Python application.
* How to store structured data.
* How to use lists and dictionaries.
* How to perform financial calculations.
* How to read and write JSON/CSV files.
* How to create menu-driven applications.
* How to calculate profit and loss.
* How to organize Python code using functions.
* How a basic portfolio tracking system works.

---

#  Complete Project Flow

```text
                USER
                  ↓
             Main Menu
                  ↓
       ┌──────────┼──────────┐
       ↓          ↓          ↓
    Add Stock  View Stock  Update Stock
       ↓          ↓          ↓
       └──────────┼──────────┘
                  ↓
          Portfolio Data
                  ↓
        Calculate Investment
                  ↓
        Calculate Current Value
                  ↓
          Calculate P/L
                  ↓
          Display Results
                  ↓
             Save Data
```

---

#  Author

*Poornima H B*

Python Project
Stock Portfolio Tracker

---

#  Conclusion

The **Stock Portfolio Tracker** is a beginner-friendly Python project that demonstrates how programming can be used to manage investment information.

The basic process is:

```text
Add Stocks
    ↓
Store Stock Information
    ↓
Track Prices
    ↓
Calculate Portfolio Value
    ↓
Calculate Profit / Loss
    ↓
Display Portfolio Performance
```

The project provides a good foundation for developing a more advanced **financial portfolio management application**.

---
