import sys

def hamming_distance(lists):
    distance = 0
    current_pos = 0
    total_length = len(lists[0])
    if len(lists[0]) != len(lists[1]):
        return -1
    while current_pos < total_length:
        if lists[0][current_pos] != lists[1][current_pos]:
            distance += 1
        current_pos += 1
    return distance

def main():
    list1 = ["10011", "10100"]
    distance = hamming_distance(list1)
    print(f'Hamming Distance: {distance}')
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
