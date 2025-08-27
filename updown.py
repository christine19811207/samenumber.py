def check_first_and_last(numbers):


    if len(numbers) < 1:
        return False
    return numbers[0] == numbers[-1]
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print(f"numbers_x: {check_first_and_last(numbers_x)}")
print(f"numbers_y: {check_first_and_last(numbers_y)}")
