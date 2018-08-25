import sys
import copy

nodes_explored = []
path = []

def answer(maze):
    height = len(maze)
    width = len(maze[0])
    shortest_path = sys.maxsize
    break_wall = False
    print(maze, "\n")

    for row in range(height):
        for col in range(width):
            temp_maze = copy.deepcopy(maze)

            if temp_maze[row][col] == 0:
                if break_wall: continue
                break_wall = True

            if temp_maze[row][col] == 1:
                temp_maze[row][col] = 0

            neighbors = [[0, 0]]
            global path
            path = [[1 for w in range(width)] for h in range(height)]
            global nodes_explored
            nodes_explored = []

            while neighbors:
                node = neighbors[0]
                neighbors.remove(node)

                if node == [height-1, width-1]:
                    shortest_path = min(shortest_path, path[-1][-1])
                    print("Path", row, col, shortest_path, "\n")
                    break
                elif node not in nodes_explored:
                    nodes_explored.append(node)
                    valid_neighbors = find_valid_neighbors(temp_maze, node)
                    neighbors.extend(valid_neighbors)
                    update_path(node, valid_neighbors)

            #print(row, col, temp_maze)

    return shortest_path

def find_valid_neighbors(maze, coords):
    node_row = coords[0]
    node_col = coords[1]
    height = len(maze)
    width = len(maze[0])
    neighbors = []

    # Add rows that are within the maze
    row_moves = list(filter(lambda x: 0<=x<height, [node_row-1, node_row+1]))
    neighbors.extend(list(map(lambda x: [x, node_col], row_moves)))

    # Add cols that are within the maze
    col_moves = list(filter(lambda x: 0<=x<width, [node_col-1, node_col+1]))
    neighbors.extend(list(map(lambda x: [node_row, x], col_moves)))

    possible_nodes = list(filter(lambda x: maze[x[0]][x[1]] == 0, neighbors))
    #print(possible_nodes)

    return list(filter(lambda x: x not in nodes_explored, possible_nodes))

def update_path(coords, valid_neighbors):
    global path
    for node in valid_neighbors: path[node[0]][node[1]] = path[coords[0]][coords[1]]+1


#test_maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
#test_maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
#print(answer(test_maze))
