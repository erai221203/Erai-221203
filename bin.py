def count_binary_digits(decimal_number):
    # Convert decimal to binary
    binary_representation = bin(decimal_number)

    # Count the number of binary digits (excluding the '0b' prefix)
    num_binary_digits = len(binary_representation) 

    return num_binary_digits

# Example usage:
decimal_number = 42
result = count_binary_digits(decimal_number)
print("The binary representation of ",decimal_number,'has',result,"digits.")
