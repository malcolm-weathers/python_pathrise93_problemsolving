# Given a matrix of numbers. You start at the left top corner and stop at the
# right bottom corner. You can only move right or move down. Maximize the
# minimum number in the path.

def path(mat):
    dist = mat.copy()
    # Fill out top row and left column.
    for i in range(1, 4):
        dist[0][i] = min(dist[0][i], dist[0][i-1])
    for i in range(1, 4):
        dist[i][0] = min(dist[i][0], dist[i-1][0])
    
    # Fill out rest of matrix. Each position stores the best minumum number
    # it can be reached from. So if a position can be reached by minimums
    # of 3 on one path or 17 on another, it will choose 17. If the position
    # is lower than either of the paths, it will become that instead. So
    # a 15 path and a 12 path reaching a 3 tile will result in a value of
    # 3.
    for i in range(1, 4):
        for j in range(1, 4):
            dist[i][j] = min(max(dist[i][j-1], dist[i-1][j]), dist[i][j])
    # The resulting matrix will look like this:
    # [27,  8,  8,  8],
    # [19, 19, 17, 17],
    # [19,  3, 17, 17],
    # [19, 18, 16, 17]

    # The correct path back can be reached by simply picking the maximum
    # of either the above or left tile.
    ans = []
    i = j = 3
    while i != 0 or j != 0:
        ans.append((i, j))
        up = left = None
        if i > 0:
            up = dist[i - 1][j]
        if j > 0:
            left = dist[i][j - 1]
        if up and not left or up > left:
            i -= 1
        else:
            j -= 1
    ans.append((0, 0))
    return list(reversed(ans))

def main():
    mat = [
        [27,  8, 51, 20],
        [19, 20, 17, 44],
        [40,  3, 77, 55],
        [40, 18, 16, 88]
    ]
    print(path(mat))

if __name__ == '__main__':
    main()
