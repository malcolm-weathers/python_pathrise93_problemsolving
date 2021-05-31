# Remove duplicates from an array without using any extra space.

def rm_dup(arr):
    i = 0
    while i < len(arr) - 1:
        j = i + 1
        while j < len(arr):
            if arr[i] == arr[j]:
                del arr[j]
                j -= 1
            j += 1
        i += 1
    
    return arr

def main():
    arr = [1, 3, 2, 3, 3, 4, 2, 1, 2]
    print(rm_dup(arr))

if __name__ == '__main__':
    main()
