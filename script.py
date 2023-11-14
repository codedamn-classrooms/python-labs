def sum_of_digits(n):
    """
    This function takes an integer n, sums its digits, and continues summing the digits
    of the result until a single-digit number is obtained. This single-digit result is then returned.
    """
    pass

# Example function calls and printing their outputs
if __name__ == "__main__":
    examples = [29, 12345, 45, 7, 987654, 0]
    for example in examples:
        print(f"sum_of_digits({example}) = {sum_of_digits(example)}")
