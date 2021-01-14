
def moving_median(numbers):
    window_size = numbers[0]
    numbers = numbers[1:]
    index = 1
    result = []
    while index < window_size:
        result.append(sum(numbers[:index])//index)
        index += 1
    index = 0
    while index < len(numbers) - window_size + 1:
        current_window = sorted(numbers[index:index+window_size])
        result.append(current_window[window_size//2])
        print(f"more({index}): {current_window}")
        index += 1
    return result
# mylist = [1, 2, 3, 4, 5, 6, 7]
numbers = [3, 1, 3, 5, 10, 6, 4, 3, 1]
# expected = [1, 2, 3, 5, 6, 6, 4, 3]
# window_size = 3

print(moving_median(numbers))