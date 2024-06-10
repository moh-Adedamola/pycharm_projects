def find_length(items):
    count = 0

    for _ in items:
        count += 1

    return count


items = "proportionate"
print(find_length(items))