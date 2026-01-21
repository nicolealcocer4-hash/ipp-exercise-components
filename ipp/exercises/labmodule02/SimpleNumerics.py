# Test 1: int
age = 25
count = -10
large_number = 1000000
alt_large_number = 1_000_000
print(f"Age: {age}; Count: {count}; Large #: {large_number}; Alt Large #: {alt_large_number}")


# Test 2: float

price = 19.99
temperature = 72.4
sci_value = 1.23e-4

print(f"Price: {price}; Temperature: {temperature}; Sci Value: {sci_value}")

# Test 3: abs() and conversion

price = 15.99
price_no_cents = int(price)
price_with_cents = float(price_no_cents)

print(f"Price: {price}; Price No Cents: {price_no_cents}; Price With Cents: {price_with_cents}")
