def convert_distance(distance, unit):
    """
    Converts a distance between kilometers and meters.

    Parameters:
    - distance (float): The distance to be converted.
    - unit (str): The unit of the distance ('km' or 'mtr').

    Returns:
    - tuple: A tuple containing the converted distance and its unit.
    """
    pass

# Example function calls
print(convert_distance(1.5, "km"))  # Expected output: (1500.0, "mtr")
print(convert_distance(3000, "mtr"))  # Expected output: (3.0, "km")
print(convert_distance(0, "mtr"))  # Expected output: (0.0, "km")

# NOTE: If you're testing an error case, make sure to comment the function call before executing the tests
# Sample Error Case 
# print(convert_distance(-2, "mtr"))  # Expected output: ValueError