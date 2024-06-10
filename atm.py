# print("welcome to python program")
count = 0

first_number = 0
second_number = 1
next_number = first_number

while count <= 10:
    print(next_number, end=", ")
    first_number,second_number = second_number,next_number
    next_number = first_number + second_number
    count += 1

# number_range = input("Enter a range: ")



