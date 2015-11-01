'''
Find the minimal path sum, in matrix.txt, a 31K text file containing a
80 by 80 matrix, from the left column to the right column.
'''

from collections import namedtuple

Node = namedtuple("Node", "weight neighbors")

def graph_from_matrix(matrix, freedom):
    graph = {}
    for y, row in enumerate(matrix):
        for x, weight in enumerate(row):
            neighbors = [(x+dx, y+dy) for dx, dy in freedom]
            graph[(x, y)] = Node(weight, neighbors)
    return graph

def shortest_path(graph, starts, ends):
    travel_cost = {node: graph[node].weight for node in starts}
    boundary = set(starts)
    studied = set()
    while not all(node in studied for node in ends):
        current = min(boundary, key=travel_cost.get)
        boundary.remove(current)
        for neighbor in graph[current].neighbors:
            if neighbor in studied or neighbor not in graph: continue
            boundary.add(neighbor)
            old_cost = travel_cost.get(neighbor, float('inf'))
            new_cost = travel_cost[current] + graph[neighbor].weight
            travel_cost[neighbor] = min(old_cost, new_cost)
        studied.add(current)
    return travel_cost[min(ends, key=travel_cost.get)]

with open('../resources/p081_matrix.txt') as fp:
    matrix = [[int(n) for n in line.strip().split(',')]
                for line in fp.readlines()]


if __name__ == '__main__':
    graph = graph_from_matrix(matrix, [(1, 0), (0, 1)])
    ans = shortest_path(graph, [(0, 0)], [(79, 79)])
    print(ans)
