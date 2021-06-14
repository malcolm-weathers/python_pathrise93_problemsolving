# Sort an array of integers such that all the zeros are aligned to the left.

# Do the other numbers need to be sorted? Or just the zeros? If just the
# zeros, then:
def zerosleft(arr):
    arr2 = []
    arr3 = []
    for x in arr:
        if x == 0:
            arr2.append(x)
        else:
            arr3.append(x)
    return arr2 + arr3

def main():
    arr = [8, -1, 40, 0, 1, 5, 1, 0, 10]
    print(zerosleft(arr))

if __name__ == '__main__':
    main()
