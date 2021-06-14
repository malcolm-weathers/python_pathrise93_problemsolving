# Given a start and end position on a chessboard if you are only allowed to walk
# diagonally, how many steps do you need to take to get to the end position?

def steps(pos1, pos2):
    # Cannot move diagonally from a odd to b, d, f, or h odd.
    if ord(pos1[0]) % 2 != ord(pos2[0]) % 2 and \
       int(pos1[1]) % 2 == int(pos2[1]) % 2:
        return -1
    row_diff = abs(ord(pos2[0]) - ord(pos1[0]))
    height_diff = abs(int(pos2[1]) - int(pos1[1]))
    return max(row_diff, height_diff)

def main():
    # a1-h8
    print(steps('a1','h8'))
    print(steps('a1','b5'))
    print(steps('a1','a5'))
    print(steps('a1','f2'))
    print(steps('e2','b7'))

if __name__ == '__main__':
    main()
