'''
Find shortest path from top-left to bottom-right moving freeform
'''

from problem00081_pathsumtwoway import matrix, graph_from_matrix, shortest_path

graph = graph_from_matrix(matrix, [( 1, 0), (-1, 0), ( 0, 1), ( 0,-1)])
ans = shortest_path(graph, [( 0, 0)], [(79,79)])
print(ans)
