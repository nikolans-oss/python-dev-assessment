def filter_and_sort_evens(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return sorted(even_numbers)

def count_character_frequency(text):
    frequency = {}
    for char in text.lower():
        frequency[char]= frequency.get(char, 0) + 1

    return frequency

print("\nFiltered and sorted even numbers:")
print(filter_and_sort_evens([3, 1, 4, 7, 1, 5, 9, 2, 6, 8]))

print("\nCharacter frequency: ")
print(count_character_frequency("This my task for Basic Data Structures & Algorithms"))