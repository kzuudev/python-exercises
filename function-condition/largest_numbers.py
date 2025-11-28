

def largest_numbers(numbers):
    # largest = numbers[0]
    #
    # for number in numbers:
    #     if number > largest:
    #         largest = number
    #
    # return largest

    largest_number = numbers[0]

    for(index, number) in enumerate(numbers):
        if number > largest_number: # check if the current number is bigger. Otherwise (if not greater), do nothing — it just continues to the next number.
            largest_number = number

    return largest_number

print(f"Largest number is:", largest_numbers([10, 82, 40, 2, 80]))

