# Given an array of integers, return an array where each element is the product
# of every element in the array except for its corresponding element in the
# first. Make the solution in O(n) time.

import random
import time

# Brute force method: calculate every element of the corresponding array manually.
def brute(a):
    soln = []
    for x in range(len(a)):
        soln.append(1)
        for y in range(len(a)):
            if y != x:
                soln[x] *= arr[y]
    return soln

# Sped up the process but I made this way too complicated.
def clever(a):
    soln = []
    for x in range(len(a)):
        soln.append(1)

    #   1   3   5   2   4
    #   1--------------->
    #           3------->
    #              15--->
    #                  30

    # Since 1x3 is added to every element after 3, we only need
    # to calculate it once and this will be the first factor for
    # every other element. The second factor for every element
    # (except the 3rd) will be 3*5, so 15 is now applicable to
    # the rest of the elements.
    for x in range(1, len(a)):
        soln[x] *= soln[x-1] * a[x-1]

    # We now have this.
    #   1   3   5   2   4
    #   1   1   3  15  30
    # The 2nd to last element is only missing *4, so we do that.
    # Since every element remaining is also missing *4, we save this
    # as our "multiplication value," the variable I've named "mv".
    
    #   1   1   3  60  30
    # 3rd element is missing *4 and *2, new mv=8. Each time, mv
    # is updated to the previous mv * the element we just finished.
    #   1   1  24  60  30           mv=8*5=40
    #   1  40  24  60  30           mv=40*3=120
    # 120  40  24  60  30
    mv = a[len(a)-1]
    for x in range(len(a)-2, -1, -1):
        soln[x] *= mv
        mv *= a[x]

    # We've reduced operations from O(n^2) to ~O(2n).
    return soln

# I made the clever() function way more complicated than it needed to be.
# Just multiply every element together and then the solution for each spot
# is that divided by the number in the array at the same location.
# So for [1, 2, 3, 4, 5], 5*4*3*2*1=120
# so the solution is [120/1, 120/2, 120/3, 120/4, 120/5]
def simple(a):
    num = 1
    for x in a:
        num *= x
    soln = []
    for x in a:
        soln.append(int(num/x))
    return soln

if __name__ == '__main__':
    n = int(input('Enter number of items: '))

    arr = []
    for x in range(n):
        arr.append(random.randint(1,50))

    print(simple(arr))
    print(clever(arr))
    print(brute(arr))
