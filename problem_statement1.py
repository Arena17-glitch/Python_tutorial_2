"""  1. Total Revenue from Active Customers
Problem Statement
You are given a list of customer dictionaries.
Each customer has:
• name
• purchases → list of purchase amounts
• active → boolean
Calculate the total revenue generated only by active customers, but:
• Ignore purchase amounts less than 100
• Apply a 10% tax to each valid purchase before summing

customers = [
    {"name": "A", "purchases": [50, 200, 300], "active": True},
    {"name": "B", "purchases": [500, 20], "active": False},
    {"name": "C", "purchases": [150, 250], "active": True}
]
Output
990.0  """

customers = [
    {"name": "A", "purchases": [50, 200, 300], "active": True},
    {"name": "B", "purchases": [500, 20], "active": False},
    {"name": "C", "purchases": [150, 250], "active": True}
]

total_revenue = sum(
    purchase * 1.10
    for customer in customers
    if customer["active"]
    for purchase in customer["purchases"]
    if purchase >= 100
)

print(total_revenue)
