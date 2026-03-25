"""  2. Problem Statement
You are given a list of products as tuples:

 Task:
• Keep only products in category "Electronics"
• Apply a 20% discount
• Return the total discounted price
Input
products = [
    ("Laptop", "Electronics", 1000),
    ("Shirt", "Clothing", 50),
    ("Phone", "Electronics", 500)
]
Output:
1200.0  """

products = [
    ("Laptop", "Electronics", 1000),
    ("Shirt", "Clothing", 50),
    ("Phone", "Electronics", 500)
]
total_discounted_price = sum(
    price * 0.80
    for name, category, price in products
    if category == "Electronics"
)
print(total_discounted_price)
