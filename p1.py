"""
This script calculates the total cost, revenue, and profit for a product.
It also checks if the business is making a profit and if the selling price falls within a specific range.
"""

# Initial setup
COST_PRICE = 5000       # Cost price of a product
SELLING_PRICE = 7000    # Selling price of the product
QUANTITY_SOLD = 50      # Quantity sold
PROFIT_MARGIN = 0.2     # Profit margin (20%)

# Calculating the total cost and revenue
TOTAL_COST = COST_PRICE * QUANTITY_SOLD
TOTAL_REVENUE = SELLING_PRICE * QUANTITY_SOLD

# Calculating the profit
PROFIT = TOTAL_REVENUE - TOTAL_COST

# Adjusting profit with the profit margin
ADJUSTED_PROFIT = PROFIT + (PROFIT * PROFIT_MARGIN)

# Checking if the business is making a profit or loss
IS_PROFIT = ADJUSTED_PROFIT > 0

# Membership operator to check if a certain price is within a price range
PRICE_RANGE = range(6000, 8000)
IS_PRICE_IN_RANGE = SELLING_PRICE in PRICE_RANGE

# Display results
print(f"Total cost: {TOTAL_COST}")
print(f"Total revenue: {TOTAL_REVENUE}")
print(f"Profit: {PROFIT}")
print(f"Adjusted profit with margin: {ADJUSTED_PROFIT}")
print(f"Is the business making a profit? {IS_PROFIT}")
print(
    f"Is the selling price in the range 6000-8000? {IS_PRICE_IN_RANGE}"
)
