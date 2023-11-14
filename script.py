from datetime import datetime

def calculate_age(dob_str):
    pass

# Example function calls
print(calculate_age("01-01-2010"))  # Example of a past date
print(calculate_age(datetime.today().strftime("%d-%m-%Y")))  # Example of the current date
print(calculate_age(datetime.strftime(datetime.today().replace(year=datetime.today().year, day=1, month=1 ), '%d-%m-%Y')))  # Example of the current year date
print(calculate_age("15-06-2022"))  # Example of a date within the last year
