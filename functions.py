def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers




nums = list(range(1, 51))
print(nums)
print(get_even_numbers(nums))




