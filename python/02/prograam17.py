my_dict = {0: 10, 1: 20, 2: 25, 3: 30, 4: 40}

# 1. Check if key 3 exists
key_to_check = 3
if key_to_check in my_dict:
    print(f"Key {key_to_check} exists in the dictionary.")
    # Print its value
    print(f"Value of key {key_to_check} is: {my_dict[key_to_check]}")
else:
    print(f"Key {key_to_check} does not exist.")

# 2. Find the sum of the values associated with keys 2 and 3
key_2_value = my_dict[2]  # Value is 25
key_3_value = my_dict[3]  # Value is 30

sum_of_values = key_2_value + key_3_value

print(f"\nSum of values for keys 2 and 3 ({key_2_value} + {key_3_value}): {sum_of_values}")