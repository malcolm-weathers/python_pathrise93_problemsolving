# Given a series of meeting times, find the time slot that is available to
# everyone.

# Say that meeting slots are in 15-minute increments from 0-10. Find the
# longest contiguous meeting time available to everyone.
def findt(times):
    good = []
    for x in range(0, 11):
        if all(x in times[t] for t in times):
            good.append(x)

    best_t = 0
    best_len = 0
    for i in range(len(good)):
        j = i + 1
        while j < len(good):
            print(good[j], good[j-1])
            if good[j] != good[j - 1] + 1:
                break
            j += 1
        if j - i > best_len:
            best_len = j - i
            best_t = good[i]
    return best_t, best_len

def main():
    times = {
        'Greg': [0, 4, 5, 8, 9, 10],
        'Jeff': [1, 2, 3, 4, 5, 6, 8, 9, 10],
        'Gordon': [3, 4, 5, 6, 8, 9, 10],
        'Alice': [2, 4, 6, 9, 10]
    }
    print(findt(times))

if __name__ == '__main__':
    main()
