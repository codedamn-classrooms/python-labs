from datetime import datetime

def validate_date(date_str):
    """
    Validates a date string in the format 'dd-mm-yyyy'.
    Returns 'today', 'past', or 'future' based on the date's relation to the current date.
    Raises a ValueError for invalid dates or formats.
    """
    pass 

# Example function calls
if __name__ == '__main__':
    print(validate_date("12-11-2023"))  # Output will depend on the current date
    print(validate_date(datetime.today().strftime('%d-%m-%Y')))  # Should return 'today'
    print(validate_date("01-01-2000"))  # Should return 'past'
    print(validate_date("32-12-2023"))  # Should raise ValueError
