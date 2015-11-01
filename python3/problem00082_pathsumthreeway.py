'''
Find shortest path from the left column to the right column.
'''

from problem00081_pathsumtwoway import matrix, graph_from_matrix, shortest_path

graph = graph_from_matrix(matrix, [( 1, 0), ( 0, 1), ( 0,-1)])
left_col = [(0, i) for i in range(80)]
right_col = [(79, i) for i in range(80)]
ans = shortest_path(graph, left_col, right_col)
print(ans)
