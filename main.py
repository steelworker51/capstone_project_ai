def largest():
    with open("numbers.txt", "r") as file:
        max_number = None
        for line in file:
            number = int(line.strip())
            if max_number is None or number > max_number:
                max_number = number
        return max_number

# Call the function and print the result
print("The largest number is:", largest())
