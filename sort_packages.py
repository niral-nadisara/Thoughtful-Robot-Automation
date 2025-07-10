def sort(width, height, length, mass):

    # Input validation
    if any(type(val) not in [int, float] or val < 0 for val in [width, height, length, mass]):
        raise ValueError("Dimensions and mass must be non-negative numbers.")
    
    # Calculate the volume of the package
    volume = width * height * length

    logging_info = f"Width: {width}, Height: {height}, Length: {length}, Mass: {mass}, Volume: {volume}"
    print(logging_info)  # debugging output

    # Determine if the package is bulky or heavy
    is_bulky = volume >= 1000000 or (width >= 150 or height >= 150 or length >= 150)
    is_heavy = mass >= 20

    logging_info = f"Is Bulky: {is_bulky}, Is Heavy: {is_heavy}"
    print(logging_info)  # debugging output

    # Determine the sorting category based on the conditions
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
    

# Example usage:
sorted_package = sort(100, 200, 300, 25)
print(sorted_package)  # Output: "REJECTED"

# Example usage:
sorted_package = sort(100, 200, 300, 15)
print(sorted_package)  # Output: "SPECIAL"

# Example usage:
sorted_package = sort(100, 200, 300, 5)
print(sorted_package)  # Output: "STANDARD"

# Example usage with error handling
try:
    print(sort(-1, 100, 100, 10))  # Should raise ValueError
except ValueError as e:
    print(e)
