# Anahid Zandi
class Graph:
    # example of adjacency list (or rather map)
    # adjacency_list = {
    # 'A': [('B', 1), ('C', 3), ('D', 7)],
    # 'B': [('D', 5)],
    # 'C': [('D', 12)]
    # }

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1,
            'E': 1,
            'F': 1,
            'G': 1,
            'H': 1,
            'I': 1,
            'J': 1,
            'K': 1
        }

        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None
            # start writing from here
            for v in open_list:
                # find the minimum f(n)
                if n == None or (g[v]+self.h(v)) < (g[n]+self.h(n)):
                    n = v

            if n == None:
                print("Path does not exist")
                return None

            if n == stop_node:
                # if the current node is stop node then backtrack the path
                backtrack_path = []

                # append the parents into list
                while parents[n] != n:
                    backtrack_path.append(n)
                    n = parents[n]
                backtrack_path.append(start_node)

                backtrack_path.reverse()
                # Display the path from first
                print('Path found : {}'.format(backtrack_path))
                return backtrack_path
             # Iterate to every child of the node
            for (child, weight) in self.get_neighbors(n):
                # if child is not present in open list and closed list
                if child not in open_list and child not in closed_list:
                    # Add the child to open list
                    open_list.add(child)
                    # Make n as it's parent
                    parents[child] = n
                    g[child] = g[n]+weight

                else:
                    # Check if it's faster to visit n then m
                    if g[child] > g[n]+weight:
                        # Update n
                        g[child] = g[n]+weight
                        parents[child] = n
                        # If the node is in closed list, move it to open list
                        if child in closed_list:
                            closed_list.remove(child)
                            open_list.add(child)
            # All the children are now visited. So move the node from open list to closed list
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None


if __name__ == '__main__':

    adjacency_list1 = {
        'A': [('B', 1), ('C', 3), ('D', 7)],
        'B': [('D', 5)],
        'C': [('D', 12)]
    }

adjacency_list2 = {
    'A': [('B', 1)],
    'B': [('C', 3)],
    'C': [('D', 2)],
    'D': [('E', 5), ('K', 11)],
    'E': [('G', 7), ('F', 8)],
    'F': [('I', 4), ('J', 9)],
    'G': [('H', 11), ('I', 8)],
    'H': [('I', 4)],
    'J': [('I', 13)],
    'K': [('J', 3)]
}

graph1 = Graph(adjacency_list1)
graph1.a_star_algorithm('A', 'D')

graph1 = Graph(adjacency_list2)
graph1.a_star_algorithm('A', 'I')