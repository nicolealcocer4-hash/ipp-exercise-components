# Test 1: String append test

salutation = "Hello, World!"
new_salutation = salutation + " Good to meet you."

print(new_salutation)
print("New Salutation Length: ", len(new_salutation))

# Test 2: String multiplication test

lots_of_apples = "apples " * 3
print(lots_of_apples)

# Test 3: String formatting test

selling_apples = "{0} {1} {2}".format("i'm selling", lots_of_apples, "!")
print(selling_apples)
print(selling_apples.capitalize())

# Test 4: String formatting with arguments test

school_info = "Location: {school}, {city}".format(
    school="Northeastern University",
    city="Boston"
)

print(school_info)

school_info = school_info + ", Massachusetts"
print(school_info)
