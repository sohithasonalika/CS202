# Initial setup
cost_price = 5000       # Cost price of a product
selling_price = 7000    # Selling price of the product
quantity_sold = 50      # Quantity sold
profit_margin = 0.2     # Profit margin (20%)

# Calculating the total cost and revenue
total_cost = cost_price * quantity_sold
total_revenue = selling_price * quantity_sold

# Calculating the profit
profit = total_revenue - total_cost

# Adjusting profit with the profit margin
adjusted_profit = profit + (profit * profit_margin)

# Checking if the business is making a profit or loss
is_profit = adjusted_profit > 0

# Membership operator to check if a certain price is within a price range
price_range = range(6000, 8000)
is_price_in_range = selling_price in price_range

# Display results
print(f"Total cost: {total_cost}")
print(f"Total revenue: {total_revenue}")
print(f"Profit: {profit}")
print(f"Adjusted profit with margin: {adjusted_profit}")
print(f"Is the business making a profit? {is_profit}")
print(f"Is the selling price in the range 6000-8000? {is_price_in_range}")
