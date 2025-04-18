import pandas as pd

# Load the product and sales data from 'data' directory
products = pd.read_csv(r"data/products.csv")
sales = pd.read_csv(r"data/sales.csv")

# Merge the sales data on the basis of 'sku' column
data = pd.merge(products, sales, on='sku')


# Pricing logic
def apply_pricing_rules(row):
    price = row["current_price"]
    cost = row["cost_price"]
    stock = row["stock"]
    sold = row["quantity_sold"]
    new_price = price  # Default is unchanged

    # Rule 1: Low Stock, High Demand
    if stock < 20 and sold > 30:
        new_price = price * 1.15

    # Rule 2: Dead Stock
    elif stock > 200 and sold == 0:
        new_price = price * 0.70

    # Rule 3: Overstocked Inventory
    elif stock > 100 and sold < 20:
        new_price = price * 0.90

    # Rule 4: Minimum Profit Constraint
    min_price = cost * 1.2
    if new_price < min_price:
        new_price = min_price

    # Final Rounding
    return round(new_price, 2)

# Apply pricing rules
data["new_price"] = data.apply(apply_pricing_rules, axis=1)

# Format price with units
# Note: the pricing unit is not declared in problem statement, hence I'm using `$` as a pricing unit.
data["old_price"] = data["current_price"].apply(lambda x: f"{x:.2f}$")
data["new_price"] = data["new_price"].apply(lambda x: f"{x:.2f}$")

# Final output DataFrame
output_data = data[["sku", "old_price", "new_price"]]
output_data.to_csv("updated_prices.csv", index=False)

print("updated_prices.csv has been generated.")
