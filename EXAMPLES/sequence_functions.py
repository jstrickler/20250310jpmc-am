colors = ["red", "blue", "green", "Yellow", "brown", "black"]
months = (
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
)

print(f"colors: len is {len(colors)}; min is {min(colors)}; max is {max(colors)}")
print(f"months: len is {len(months)}; min is {min(months)}; max is {max(months)}")
print()

print("sorted:", end=' ')
print(f"{sorted(colors) = }")

