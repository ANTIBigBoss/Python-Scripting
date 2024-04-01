# I don't fully understand the math in here but my understanding is
# Euler's formula is a mathematical constant approximately equal to 2.71828

def approximate_e(epsilon=1e-9):
    # For 0! we set it in factorial of 1
    factorial = 1
    # Start with the first term of the series, which is 1
    sum_e = 1
    # Start with 1! as the next term's factorial
    n = 1

    while True:
        # Calculate n! by multiplying with the previous factorial
        factorial *= n
        # Calculate the term to be added
        term = 1 / factorial
        # Add the term to the sum to approximate e
        sum_e += term
        # If the term is less than epsilon, we break out of the loop because we reached the point of accuracy we want
        if term < epsilon:
            break

        # If not we continue to the next term until we do
        n += 1

    return sum_e


# This function is to help us print the approx value
approx_e = approximate_e()

# I don't get the same approximate number as in the example, but I think the logic is correct?
print("The approximate value is:", approx_e)
