def convert_temperature(value, input_unit, output_unit):
    """
    Convert a temperature value from one unit to another.
    
    Parameters:
    - value (float): The temperature value to convert.
    - input_unit (str): The unit of the input value ('c', 'f', 'k').
    - output_unit (str): The unit to convert to ('c', 'f', 'k').

    Returns:
    float: The converted temperature, rounded to two decimal places.
    """
    pass 


# Example function calls
print(convert_temperature(25, 'c', 'f'))  # Celsius to Fahrenheit
print(convert_temperature(10, 'c', 'k'))  # Celsius to Kelvin
print(convert_temperature(300, 'k', 'c'))  # Kelvin to Celsius
print(convert_temperature(273, 'k', 'f'))  # Kelvin to Fahrenheit
print(convert_temperature(68, 'f', 'k'))  # Fahrenheit to Kelvin
print(convert_temperature(32, 'f', 'c'))  # Fahrenheit to Celsius
