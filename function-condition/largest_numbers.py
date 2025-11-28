

def largest_numbers(numbers):
    # largest = numbers[0]
    #
    # for number in numbers:
    #     if number > largest:
    #         largest = number
    #
    # return largest

    for(index, number) in enumerate(numbers):
        largest_number = numbers[index]

        if number > largest_number:
            largest_number = number

    return largest_number

print(largest_numbers([10, 5, 40, 2, 99]))

