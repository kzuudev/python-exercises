

def even_numbers(numbers):
    numbers.sort()

    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers



all_even_numbers = even_numbers([29, 40, 32, 2, 10, 8])
print(all_even_numbers)