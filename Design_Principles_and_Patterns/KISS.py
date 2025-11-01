# KISS Principle Example
# KISS -> "Keep It Simple, Stupid"
# Concept: Write code that is simple, clear, and easy to understand.
# Avoid unnecessary complexity or over-engineering.

# BAD EXAMPLE (for reference)
"""
def is_even(n):
    return True if n % 2 == 0 else False
"""
# The above code works, but it’s unnecessarily complex.
# The expression 'n % 2 == 0' already returns True or False.
# There’s no need to use an extra conditional expression.

# GOOD EXAMPLE (Using KISS Principle)
def is_even(n):
    # Simple and clear: directly return the boolean result of the condition
    return n % 2 == 0

# ---- Main program ----

# Take user input
n = int(input("Enter any number: "))

# Call the function to check if the number is even
result = is_even(n)

# Display the result to the user
if result:
    print(f"{n} is an even number.")
else:
    print(f"{n} is an odd number.")
