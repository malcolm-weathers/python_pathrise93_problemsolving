# Explain bubble sort. Derive its time complexity.

# Time complexity is i*j = n*n = O(n^2).
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    arr = [9, 55, 7, 1, 3, 18]
    bubblesort(arr)
    print(arr)

if __name__ == '__main__':
    main()
