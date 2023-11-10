def calculate_bmi(height, weight):
    """
    Calculate the Body Mass Index (BMI) and determine the BMI category.
    
    :param height: Height in centimeters.
    :param weight: Weight in kilograms.
    :return: A tuple containing the BMI value (rounded to two decimal places) and the BMI category.
    """
    pass
    

# Example function calls
print(calculate_bmi(155, 43.3))  # Expected: (18.02, "underweight")
print(calculate_bmi(170, 62.2))  # Expected: (21.52, "healthy")
print(calculate_bmi(150, 77.1))  # Expected: (34.27, "obese")
print(calculate_bmi(189, 101.2)) # Expected: (28.37, "overweight")