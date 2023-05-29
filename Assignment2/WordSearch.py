# Anahid Zandi
# Below lists detail all eight possible movements from a cell
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]


# Function to check if it is possible to go to position next
# from the current position. The function returns false if next is
# not in a valid position, or it is already visited
def isValid(mat, x, y, path):
	return (0 <= x < len(mat)) and (0 <= y < len(mat[0])) and (x, y) not in path


def DFS(mat, word, i, j, path=[], index=0):

	# return if characters don't match
	if mat[i][j] != word[index]:
		return
 
	# include the current cell in the path
	path.append((i, j))
 
	# if all words are matched, print the result and return
	if index == len(word) - 1:
		for i in range(len(word)):
			print(word[i] + str(path[i]), end = ' ')
		print()
	else:
		# check all eight possible movements from the current cell
		# and recur for each valid movement
		for k in range(len(row)):
			# check if it is possible to go to the next position
			# from the current position
			if isValid(mat, i + row[k], j + col[k], path):
				DFS(mat, word, i + row[k], j + col[k], path, index + 1)
 
	# backtrack: remove the current cell from the path
	path.pop()

def WordSearch(mat, word):
	# base case
	if not mat or not len(mat) or not len(word):
		return

	for i in range(len(mat)):
		for j in range(len(mat[0])):
			DFS(mat, word, i, j)


if __name__ == '__main__':

	mat = [
		['A', 'D', 'E', 'B', 'C'],
		['O', 'O', 'C', 'A', 'X'],
		['S', 'C', 'D', 'K', 'C'],
		['O', 'D', 'E', 'H', 'L']
	]
	word = 'CODE'

	WordSearch(mat, word)