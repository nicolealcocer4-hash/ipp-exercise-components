# Test 1: simple int calcs

picked_apples = 30
bagged_apples = 7

available_apples = picked_apples + bagged_apples

consumed_apples = 5
remaining_apples = available_apples - consumed_apples

print(f"Apples collected. Picked: {picked_apples}; Bagged: {bagged_apples}; Available: {available_apples}")
print(f"After eating some apples. Consumed: {consumed_apples}; Remaining: {remaining_apples}")

# Test 2: simple product calcs

shopping_trips = 3
apples_per_trip = 4

purchased_apples = shopping_trips * apples_per_trip
total_apples = remaining_apples + purchased_apples

print(f"Shopping trips: {shopping_trips}; Apples per trip: {apples_per_trip}")
print(f"Purchased apples: {purchased_apples}; Total apples: {total_apples}")

# Test 3: remainders

days_per_week = 7

daily_apples_for_week = int(total_apples / days_per_week)
left_over_apples_mod = total_apples % days_per_week
left_over_apples_sub = total_apples - (daily_apples_for_week * days_per_week)

print(f"Total apples: {total_apples}; Daily apples for week: {daily_apples_for_week}")
print(f"Left over apples (mod): {left_over_apples_mod}; Left over apples (sub): {left_over_apples_sub}")
