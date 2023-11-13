def time_difference(start, end):
    """
    Calculate the difference in hours and minutes between two times.
    Args:
    start (str): Start time in 'hh:mm' format.
    end (str): End time in 'hh:mm' format.

    Returns:
    dict: A dictionary with keys 'hours' and 'minutes' indicating the time difference.
    """
    pass

# Example function calls and print statements
print(time_difference('2:25', '3:00'))  # Expected Output: {'hours': 0, 'minutes': 35}
print(time_difference('23:15', '00:30')) # Expected Output: {'hours': 1, 'minutes': 15}
print(time_difference('5:30', '5:30')) # Expected Output: {'hours': 0, 'minutes': 0}