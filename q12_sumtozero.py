# If you have a large array of integers, write an algorithm that will find out
# if any 2 of them sum to zero. What is the Big O of the algorithm? Come up
# with ways that are not brute force that are faster.

# O(n^2)
def brute(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == 0:
                return True
    return False

# O(n log n) I think. Depends on big-O of Python's sort() function.
def sort(arr):
    arr.sort()
    i = 0
    j = len(arr) - 1
    while len(arr) > 0:
        if arr[i] + arr[j] == 0:
            return True
        if abs(arr[i]) > arr[j]:
            del arr[i]
            j -= 1
        else:
            del arr[j]
            j -= 1
    return False

def main():
    f = [-76, 43, -7, 8, 31, 99]
    t = [-76, 43, -7, 8, 31, 99, 76]
    print(brute(f))
    print(sort(f))
    print(brute(t))
    print(sort(t))

if __name__ == '__main__':
    main()
