
from collections import deque
import collections


class Node():
    def __init__(self, data):
        self.data = data
        self.neighbors = set()

    ################################################################
    # Breadth First Traversal
    ################################################################

    def printBFS(self, graph):
        '''
        Iterative implementation, assumes graph is acyclic.
        Worst Case: O(n^2) time, O(n) space
        '''
        q = deque(self.data)
        while q:
            current = graph[q.pop()]
            print(f'{current.data}')
            for neighbor in current.neighbors:
                q.appendleft(neighbor)

    def hasPathBFS(self, graph, dest):
        '''
        Iterative implementation, assumes graph is acyclic.
        Worst Case: O(n^2) time, O(n) space
        '''
        q = deque(self.data)
        while q:
            current = graph[q.pop()]
            if current.data == dest:
                return True
            for neighbor in current.neighbors:
                q.appendleft(neighbor)
        return False

    def hasUndirectedPathBFS(self, dest, visited):
        '''
        Iterative implementation, assumes graph is undirected.
        Worst Case: O(e) = O(n^2) time, O(n) space
        '''
        visitQueue = deque([self])
        while visitQueue:
            current = visitQueue.pop()
            if current in visited:
                continue

            if current.data == dest:
                return True

            visited.add(current)
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    visitQueue.appendleft(neighbor)
        return False

    ################################################################
    # Depth First Traversal
    ################################################################

    def printDFS(self, graph):
        '''
        Iterative implementation, assumes graph is acyclic.
        Worst Case: O(n^2) time, O(n) space
        '''
        stack = [self.data]
        while stack:
            current = graph[stack.pop()]
            print(f'{current.data}')

            for neighbor in current.neighbors:
                stack.append(neighbor)

    def recursivelyPrintDFS(self, graph):
        '''
        Recursive implementation, assumes graph is acyclic.
        Worst Case: O(n^2) time, O(n) space
        '''
        print(f'{self.data}')
        for neighbor in self.neighbors:
            graph[neighbor].depthFirstPrint(graph)

    def hasPathDFS(self, graph, dest):
        '''
        Recursive implementation, assumes graph is acyclic.
        Worst Case: O(n^2) time, O(n) space
        '''
        if self.data == dest:
            return True
        for neighbor in self.neighbors:
            if graph[neighbor].hasPath(graph, dest):
                return True
        return False

    def hasUndirectedPathDFS(self, dest, visited):
        '''
        Recursive implementation, assumes graph is undirected.
        Worst Case: O(e) = O(n^2) time, O(n) space
        '''
        if self in visited:
            return False

        if self.data == dest:
            return True

        visited.add(self)
        for neighbor in self.neighbors:
            if neighbor not in visited and neighbor.hasUndirectedPathDFS(dest, visited):
                return True
        return False

# End of Node

###################### Graph Functions ##########################


def buildUndirectedGraph(edges):
    graph = {}
    for leftKey, rightKey in edges:
        if leftKey not in graph:
            graph[leftKey] = Node(leftKey)
        if rightKey not in graph:
            graph[rightKey] = Node(rightKey)
        graph[leftKey].neighbors.add(graph[rightKey])
        graph[rightKey].neighbors.add(graph[leftKey])

    return graph


def printGraph(graph):
    '''
    Print the adjacent list of a provided key-value graph
    '''
    for key, node in graph.items():
        print(
            f'{key} -> {[neighbor.data for neighbor in node.neighbors]}')


def exploreDeep(graph, startKey, visited):
    '''
    Search deep for nodes connected to startKey and add them to the
    visited set
    '''
    unexplored = deque([startKey])
    while unexplored:
        current = unexplored.pop()
        if current in visited:
            continue
        visited.add(current)
        for neighbor in graph[current]:
            unexplored.append(neighbor)


def countConnectedComponentsOfUndirectedGraph(graph):
    '''
    Count the number of segmented graph components by performing depth first
    traversal on everynode and counting unique paths
    O(N) Space | O(E) Time
    '''
    components = 0
    visited = set()
    for key in graph:
        if key not in visited:
            exploreDeep(graph, key, visited)
            components += 1
    return components


def largestComponentsOfUndirectedGraph(graph):
    '''
    Count the number of segmented graph components by performing depth first
    traversal on everynode and counting unique paths
    O(N) Space | O(E) Time
    '''
    largestComponent = float('-inf')
    visited = set()
    for key in graph:
        originalSize = len(visited)
        if key not in visited:
            exploreDeep(graph, key, visited)
            componentsInTraversal = len(visited) - originalSize
            print(f"Found {componentsInTraversal} in traversal")
            largestComponent = max(componentsInTraversal, largestComponent)
    return largestComponent

################# TESTS ##########################


def connectedComponentTest():
    graph = {
        1: [2],
        2: [1],
        3: [],
        4: [6],
        5: [6],
        6: [4, 5, 7, 8],
        7: [6],
        8: [6]
    }

    print(countConnectedComponentsOfUndirectedGraph(graph))


def findPathTest():
    edges = [
        ['i', 'j'],
        ['k', 'i'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'n'],
    ]

    visited = set()
    graph = buildUndirectedGraph(edges)
    printGraph(graph)
    # hasPath = graph['i'].hasUndirectedPathDFS('l', visited)
    hasPath = graph['i'].hasUndirectedPathBFS('l', visited)

    print(f'{hasPath = }')
    print(f'visited =  {[visitee.data for visitee in visited]}')


def largestComponentTest():
    graph = {
        0: [8, 1, 5],
        1: [0],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2],
        5: [0, 8],
        8: [0, 5],
    }

    print(
        f'Largest Component size is: {largestComponentsOfUndirectedGraph(graph)}')


def findShortestPath(graph, src, dst):
    if src == dst:  # Check if it's already solved
        return 0

    visited = set(src)
    path = deque([(src, 0)])
    while path:
        key, depth = path.pop()
        for neighbor in graph[key]:
            if neighbor not in visited:
                if neighbor == dst:
                    return depth + 1
                else:
                    visited.add(neighbor)
                    path.appendleft((neighbor, depth + 1))

    return None


def findShortestPathTest():
    '''
    Find the shortest path betwwen two nodes
    '''
    edges = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v'],
    ]

    # Build the graph from edges
    graph = {}
    for leftKey, rightKey in edges:
        graph.setdefault(leftKey, [])
        graph.setdefault(rightKey, [])
        graph[leftKey].append(rightKey)
        graph[rightKey].append(leftKey)

    print(f'{graph = }')
    shortestPath = findShortestPath(graph, 'w', 'z')
    print(f'{shortestPath = }')


def exploreIsland(world, visited, startPosition):
    '''
    Visit all land (L) tiles connected to startPosition
    where (0,1) = (row,col)
    '''
    previouslyVisited = len(visited)
    path = [startPosition]

    while path:
        row, col = path.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        # print(f"exploring: {row}, {col}")

        # Check neighbor above current tile
        if 0 <= row - 1 < len(world) and (row - 1, col) not in visited and world[row - 1][col] == 'L':
            path.append((row - 1, col))
        # Check neighbor below current tile
        if 0 <= row + 1 < len(world) and (row + 1, col) not in visited and world[row + 1][col] == 'L':
            path.append((row + 1, col))
        # Check neighbor left of current tile
        if 0 <= col - 1 < len(world[row]) and (row, col - 1) not in visited and world[row][col - 1] == 'L':
            path.append((row, col - 1))
        # Check neighbor right of current tile
        if 0 <= col + 1 < len(world[row]) and (row, col + 1) not in visited and world[row][col + 1] == 'L':
            path.append((row, col + 1))

    islandSize = len(visited) - previouslyVisited
    print(f"Finished exploring island of size {islandSize}")
    return islandSize


def countIslands(world):
    smallest = float('inf')
    largest = float('-inf')
    islands = 0
    visited = set()
    for i, row in enumerate(world):
        for j, tile in enumerate(row):
            if tile == 'L' and (i, j) not in visited:
                print(f"New Land at {i},{j}")
                islands += 1
                islandSize = exploreIsland(world, visited, (i, j))
                smallest, largest = min(
                    smallest, islandSize), max(largest, islandSize)

    return islands, smallest, largest


def islandCountTest():
    '''
    Find the number of connected land('L') components in the grid.
    '''
    world = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W']
    ]

    islands = countIslands(world)
    print(f'total Islands = {islands[0]}')


def smallestIslandTest():
    '''
    Find the number of connected land('L') components in the grid.
    '''
    world = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W']
    ]

    # Debug: Print world
    for row in world:
        for tile in row:
            print(tile, end=' ')
        print()

    results = countIslands(world)
    print(f'smallest island is of size {results[1]}')


if __name__ == "__main__":
    # islandCountTest()
    smallestIslandTest()
