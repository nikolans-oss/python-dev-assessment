def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    try:
        return total / len(numbers)
    except ZeroDivisionError:
        return None

data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []
print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")


def get_list_element(my_list, index):
    try:
        return my_list[index]
    except TypeError:
        print("Expected a list object.")
        return None
    except IndexError:
        print("Index is out of bounds.")
        return None

list = ["red", "blue", "green"]

print("\nValid Input:")
print(f"Result: {get_list_element(list, 1)}\n")

print("Out-of-bounds Input:")
print(f"Result: {get_list_element(list, 5)}\n")

print("Incorrect Type Input:")
print(f"Result: {get_list_element(42, 0)}\n")