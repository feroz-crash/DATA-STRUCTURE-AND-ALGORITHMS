def fractional_knapsack(items, capacity):
    """
    items: list of tuples (name, value, weight)
    capacity: max weight the knapsack can carry
    returns: (total_value, list of (name, fraction_taken, weight_taken))
    """
    # Step 1: sort by value/weight ratio, descending
    items = sorted(items, key=lambda x: x[1] / x[2], reverse=True)

    total_value = 0.0
    taken = []
    remaining = capacity

    for name, value, weight in items:
        if remaining <= 0:
            break

        if weight <= remaining:
            # take the whole item
            taken.append((name, 1.0, weight))
            total_value += value
            remaining -= weight
        else:
            # take a fraction of it
            fraction = remaining / weight
            taken.append((name, fraction, remaining))
            total_value += value * fraction
            remaining = 0

    return total_value, taken


# Example usage
items = [
    ("Gold", 60, 10),
    ("Silver", 100, 20),
    ("Diamond", 120, 30),
]
capacity = 50

max_value, breakdown = fractional_knapsack(items, capacity)

print(f"Max value: {max_value}")
for name, frac, wt in breakdown:
    print(f"  {name}: took {frac*100:.1f}% ({wt} weight)")