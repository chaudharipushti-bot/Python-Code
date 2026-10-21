# 3.11 Inventory System
inventory_value = {}

def add_item_value(entered_name, qty_value):
    inventory_value[entered_name] = inventory_value.get(entered_name, 0) + qty_value

def remove_item_value(entered_name):
    if entered_name in inventory_value:
        del inventory_value[entered_name]
    else:
        print(f"Item '{entered_name}' not found.")

def update_qty_value(entered_name, qty_value):
    if entered_name in inventory_value:
        inventory_value[entered_name] = qty_value
    else:
        print(f"Item '{entered_name}' does not exist.")

def display_inventory_value():
    print(f"\n{'Item':<15} | {'Quantity':<10}")
    print("-" * 28)
    for entered_name, qty_value in inventory_value.items():
        print(f"{entered_name:<15} | {qty_value:<10}")

def low_stock_value():
    low_value = {entered_name: qty_value for entered_name, qty_value in inventory_value.items() if qty_value < 5}
    print(f"\nLow Stock Items (<5): {low_value if low_value else 'None'}")


# Simulation
add_item_value("Notebooks", 15)
add_item_value("Pens", 3)
add_item_value("Erasers", 2)
add_item_value("Markers", 10)

display_inventory_value()
low_stock_value()

update_qty_value("Pens", 12)
remove_item_value("Erasers")

print("\n--- After Modifications ---")
display_inventory_value()