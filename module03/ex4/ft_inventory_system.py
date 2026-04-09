import sys


def main():
    if len(sys.argv) == 1:
        print("At the beginning of the game, your inventory "
              "is usually empty ;)")
        return

    print("=== Inventory System Analysis ===")
    inventory = {}
    item_order = []

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item_name, quantity_str = parts

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(quantity_str)
            inventory[item_name] = quantity
            item_order.append(item_name)
        except ValueError:
            print(f"Quantity error for '{item_name}': invalid "
                  "literal for int() with base 10: '{quantity_str}'")

    if not inventory:
        return

    print(f"Got inventory: {inventory}")
    print(f"Item list: {item_order}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    for item in item_order:
        percentage = (inventory[item] / total_quantity) * 100
        print(f"Item {item} represents {percentage:.1f}%")

    most_abundant = item_order[0]
    least_abundant = item_order[0]

    for item in item_order:
        if inventory[item] > inventory[most_abundant]:
            most_abundant = item
        if inventory[item] < inventory[least_abundant]:
            least_abundant = item

    print(f"Item most abundant: {most_abundant} "
          "with quantity {inventory[most_abundant]}")
    print(f"Item least abundant: {least_abundant} "
          "with quantity {inventory[least_abundant]}")

    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
