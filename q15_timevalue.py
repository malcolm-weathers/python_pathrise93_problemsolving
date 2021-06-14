# You have a set of (time, value) pairs. How can you find the first and last
# values in the time interval [a, b]?

# Assume time is in UNIX time.
def vals(tv_arr, a, b):
    least_time = b
    least_val = -1
    most_time = a
    most_val = -1
    for tv in tv_arr:
        if tv[0] < least_time and tv[0] >= a:
            least_time = tv[0]
            least_val = tv[1]
        if tv[0] > most_time and tv[0] <= b:
            most_time = tv[0]
            most_val = tv[1]
    return least_val, most_val

def main():
    tv_arr = [(305, -7), (303, 2), (901, 5), (40, -7), (450, 50), (451, 8)]
    print(vals(tv_arr, 304, 450)) # Should return -7, 50

if __name__ == '__main__':
    main()
