def read_map(file_path):
    with open(file_path, 'r') as file:
        lab_map = [list(line.strip()) for line in file.readlines()]
    return lab_map

def find_guard(lab_map):
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    for r, row in enumerate(lab_map):
        for c, cell in enumerate(row):
            if cell in directions:
                return (r, c, directions[cell])

def turn_right(direction):
    if direction == (-1, 0):  # Up
        return (0, 1)        
    if direction == (0, 1):  # Right
        return (1, 0)        
    if direction == (1, 0):  # Down
        return (0, -1)       
    if direction == (0, -1): # Left
        return (-1, 0)       # Up

def simulate_path(lab_map):
    rows, cols = len(lab_map), len(lab_map[0])
    r, c, direction = find_guard(lab_map)
    visited = set()
    
    while 0 <= r < rows and 0 <= c < cols:
        visited.add((r, c))
        dr, dc = direction
        next_r, next_c = r + dr, c + dc
        
        if 0 <= next_r < rows and 0 <= next_c < cols and lab_map[next_r][next_c] == '#':
            # Turn right
            direction = turn_right(direction)
        else:
            # Move forward
            r, c = next_r, next_c
    
    return visited

# Main execution
lab_map = read_map('input.txt')
visited_positions = simulate_path(lab_map)
print(f"Distinct positions visited: {len(visited_positions)}")
