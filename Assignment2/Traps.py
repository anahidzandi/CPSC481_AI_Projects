#Anahid Zandi
from collections import deque as queue

# check if specified row and column are valid matrix index
def isValid(i, j, N, M):
	return (0 <= i < M) and (0 <= j < N)

def isSafe(i, j, mat, result):
    return mat[i][j] == 'O' and result[i][j] == -1


# Replace all O's in a matrix with their shortest distance
# from the nearest trap
def shortestDistanceToTraps(mat):
	# start writing from here
	# base case
    if not mat or not len(mat):
        return []
 
    # `M × N` matrix
    (M, N) = (len(mat), len(mat[0]))
 
    result = [[0 for x in range(N)] for y in range(M)]
 
    # initialize an empty queue
    q = queue()
 
    # find all mines location and add them to the queue
    for i in range(M):
        for j in range(N):
            # if the current cell represents a mine
            if mat[i][j] == 'T':
                q.append((i, j, 0))
 
                # update mine distance as 0
                result[i][j] = 0
 
            # otherwise, initialize the mine distance by -1
            else:
                result[i][j] = -1
 
    # lists to get indices of four adjacent cells of a given cell
    row = [0, -1, 0, 1]
    col = [-1, 0, 1, 0]
 
    # do for each in the queue
    while q:
 
        # dequeue front cell
        x, y, distance = q.popleft()
 
        # update the four adjacent cells of the front node in the queue
        for i in range(len(row)):
            # enqueue adjacent cell if it is valid, unvisited,
            # and has a path through it
            if isValid(x + row[i], y + col[i], N, M) and \
                    isSafe(x + row[i], y + col[i], mat, result):
                result[x + row[i]][y + col[i]] = distance + 1
                q.append((x + row[i], y + col[i], distance + 1))
 
    return result
 
	


if __name__ == '__main__':

	mat = [
		['O', 'O', 'T', 'O', 'O'],
		['O', 'W', 'O', 'T', 'O'],
		['W', 'T', 'O', 'O', 'W'],
		['O', 'O', 'O', 'O', 'O']
	]

	result = shortestDistanceToTraps(mat)

	# print results
	for r in result:
		print(r)