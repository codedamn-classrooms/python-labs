def unique_elements(lst):
    """
    Returns a new list containing unique elements from the input list, 
    preserving their original order. If the input is not a list or is empty, 
    handles accordingly.
    """
    pass

# Example function calls
if __name__ == "__main__":
    print(unique_elements([1, 2, 2, 3, 3, 3, 4]))  # Output: [1, 2, 3, 4]
    print(unique_elements(["apple", "banana", "apple", "orange", "banana"]))  # Output: ["apple", "banana", "orange"]
    print(unique_elements([]))  # Output: None
    print(unique_elements("not a list"))  # ! This will raise a TypeError
