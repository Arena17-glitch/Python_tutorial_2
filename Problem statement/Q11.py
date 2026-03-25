sales = [("Pen", 10), ("Pencil", 25), ("Pen", 15)]
total_sales = {}

for product, qty in sales:
    total_sales[product] = total_sales.get(product, 0) + qty
highest_product = max(total_sales, key=total_sales.get)

print(highest_product)
