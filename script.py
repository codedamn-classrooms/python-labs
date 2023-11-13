def is_pythagorean_triplet(lst):
    """
    Checks if a list of three numbers can form a Pythagorean triplet.
    
    Parameters:
    lst (list): A list of three numbers.
    
    Returns:
    bool: True if the numbers form a Pythagorean triplet, False otherwise.
    
    Raises:
    ValueError: If the input list does not contain exactly three numbers.
    """
    pass

# Example function calls and printing the output
if __name__ == "__main__":
        print(is_pythagorean_triplet([3, 4, 5]))      # Should return True
        print(is_pythagorean_triplet([10, 5, 24]))    # Should return False
        print(is_pythagorean_triplet([5, 3, 4]))      # Permutation of the first example, should return True
        print(is_pythagorean_triplet([1, 1, 1]))       # Not a Pythagorean triplet, should return False
        print(is_pythagorean_triplet([7, 24, 25]))    # A larger Pythagorean triplet, should return True
        print(is_pythagorean_triplet([9, 40, 41]))    # Another Pythagorean triplet, should return True

        print(is_pythagorean_triplet('random value')) # Value Error 