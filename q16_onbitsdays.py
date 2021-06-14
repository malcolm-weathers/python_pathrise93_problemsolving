# Convert an integer with on bits corresponding to valid days of a week to
# strings of valid days.

def valid(num):
    days = 'Sunday Monday Tuesday Wednesday Thursday Friday Saturday'.split()
    valid_days = []
    while num > 0:
        mod = num % 2
        if mod == 1:
            valid_days.append(days[-1])
        del days[-1]
        num = num // 2
    return list(reversed(valid_days))

def main():
    print(valid(int('1100110', 2)))
    print(valid(int('0001010', 2)))

if __name__ == '__main__':
    main()
