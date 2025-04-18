# Dynamic Pricing Engine

This project is a dynamic pricing engine built in Python. It automatically adjusts product prices based on recent sales performance and current stock levels, helping businesses optimize their pricing strategy to match demand and inventory constraints while maintaining healthy profit margins.

---

## Project Objective

The goal of the project is to simulate a real-world pricing mechanism where product prices are dynamically updated using predefined business rules. This pricing engine processes product data and sales history to:

- Increase prices for high-demand, low-stock items
- Decrease prices for overstocked or unsold inventory
- Ensure a minimum profit margin for all products

---

## 📁 Directory Structure

```         
pricing_engine/                                     # Main Directory
|
|--- data/                                          # Sub directory to store the data
|    |--- products.csv                              # Product catalog with current prices, cost, and stock
|    |--- sales.csv                                 # Sales data
|
|--- Data and Logic implementation Notebook.ipynb   # Primary logic and code implementation notebook
|--- pricing_engine.py                              # Main script that processes and updates prices
|--- updated_pricing.csv                            # Output file with new pricing
|___ README.md                                      # Project documentation (this file)
```

---

## 📈 Pricing Rules
###### (from provided document)

Prices are updated based on the following rules (applied in order):

1. **Rule 1 – Low Stock, High Demand**
   - **Condition:** `stock < 20` **and** `quantity_sold > 30`
   - **Action:** Increase price by **15%**

2. **Rule 2 – Dead Stock**
   - **Condition:** `stock > 200` **and** `quantity_sold == 0`
   - **Action:** Decrease price by **30%**

3. **Rule 3 – Overstocked Inventory**
   - **Condition:** `stock > 100` **and** `quantity_sold < 20`
   - **Action:** Decrease price by **10%**

4. **Rule 4 – Minimum Profit Constraint (Always Applied)**
   - **Condition:** New price must be at least **20% above** the cost price.
   - **Action:** If not, set price to `cost_price × 1.2`

5. **Final Rounding**
   - All prices are rounded to **2 decimal places**.

---

## 🛠 How to Run

1. Make sure you have **Python 3.x** installed.
2. Place your `products.csv` and `sales.csv` files in the `data/` directory.
3. Run the script:

```bash
python pricing_engine.py
```

4. The script will generate an output file called `updated_prices.csv` in the project root, containing:

- `sku`
- `old_price` (with `$` units)
- `new_price` (with `$` units)

---

## 📤 Output Example

```
sku,old_price,new_price
A123,$649.99,$600.00
B456,$699.00,$803.85
C789,$999.00,$699.30
```

---

## 📬 Notes

- The script ensures all price changes are justifiable and comply with business constraints.
- You can extend this engine by integrating it with a live dashboard or API for real-time pricing adjustments.

---

## 👨‍💻 Author

**Shreyash A. Kamble**  
AI Developer | Aspiring Data Scientist <br>

---

## 🔗 Contact & Repository

- 📧 Email: [shreyash261020@gmail.com](mailto:shreyash261020@gmail.com)
- 🧑‍💻 GitHub Repository: [Dynamic Pricing Engine]()

---

**NOTE:** This is a CLI-based program designed for simplicity and automation. I can also develop a fully interactive graphical dashboard or web interface for enhanced usability and real-time pricing insights. Looking forward to showcasing more!