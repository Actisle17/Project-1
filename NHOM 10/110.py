def is_perfect_number(num):
    # Find all proper divisors of the number
    divisors = [1]
    for i in range(2, num):
        if num % i == 0:
            divisors.append(i)
    
    # Check if sum of proper divisors is equal to the number
    if sum(divisors) == num:
        return True
    else:
        return False

# Find all perfect numbers between 1 and 10000
perfect_numbers = []
for i in range(1, 10001):
    if is_perfect_number(i):
        perfect_numbers.append(i)

# Print the list of perfect numbers
print("The perfect numbers between 1 and 10000 are:")
print(perfect_numbers)