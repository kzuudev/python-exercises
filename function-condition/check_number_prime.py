


def check_number_prime(number):
    if number % 2 == 0:
        return "prime"
    else:
        return "odd"

print(f"the provided number is {check_number_prime(1)}")