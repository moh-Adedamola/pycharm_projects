import random

def get_random_numbers():

    random.seed(50)

    numbers_list = []
    for _ in range(10):
        numbers = random.randint(1, 50)

        numbers_list.append(numbers)

    return numbers_list

print(get_random_numbers())


def find_length(numbers_list):
    count = 0
    for _ in numbers_list:
        count += 1

    return count


def sum_elements_at_even_positions(numbers_list):
    index = 0
    sum_even_positions = 0

    for index in range(0, find_length(numbers_list), 2):
        sum_even_positions += numbers_list[index]

    return sum_even_positions


def sum_elements_at_odd_positions(numbers_list):
    index = 0
    sum_odd_positions = 0

    for index in range(0, find_length(numbers_list), 2):
        sum_odd_positions += numbers_list[index]

    return sum_odd_positions


def multiply_elements_at_every_third_positions(numbers_list):
    index = 0
    multiply_elements = 0

    for index in range(0, find_length(numbers_list), 3):
        multiply_elements *= numbers_list[index]

    return multiply_elements


def average(numbers_list):
    sum_of_numbers = 0

    for index in range(find_length(numbers_list)):
        sum_of_numbers += numbers_list[index]

    average = sum_of_numbers / find_length(numbers_list)

    return average


def largest(numbers_list):
    max = numbers_list[0]

    for index in range(find_length(numbers_list)):

        if numbers_list[index] > max:
            max = numbers_list[index]

    return max

numbers_list = [32, 18, 24, 41, 16, 45, 31, 50, 22, 6]
print(largest(numbers_list))

def smallest(numbers_list):
    min = numbers_list[0]

    for index in range(find_length(numbers_list)):

        if numbers_list[index] < min:

            min = numbers_list[index]

    return min

numbers_list = [32, 18, 24, 41, 16, 45, 31, 50, 22, 6]
print(smallest(numbers_list))

def count_words(words):
    count = 0

    for word in words:

        if find_length(word) > 1 and word[0] == word[-1]:

            count += 1

    return count

print(count_words(['abc', 'xyz', 'aba', '1221']))

def sequential_list():
    numbers = range(1, 16)

    number_list = list(numbers)

    return number_list


print(sequential_list())


def duplicate_list():
    numbers = range(1, 16)

    number_list = list(numbers)

    new_list = []

    for number in number_list:
        new_list.append(number)
        new_list.append(number)

    return new_list


print(duplicate_list())

def remove_duplicates():

    new_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]

    new_list  = list(set(new_list))

    return new_list

print(remove_duplicates())



