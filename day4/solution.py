def read_grid_from_file(file):
    with open(file, 'r') as f:
        grid = [line.strip() for line in f.readlines()]
    return grid

def count_xmas_occurrences(grid):
    word = "XMAS"
    word_len = len(word)
    directions = [
        (0, 1), (1, 0), (1, 1), (1, -1),
        (0, -1), (-1, 0), (-1, -1), (-1, 1)  
    ]
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                if search_from(r, c, dx, dy):
                    count += 1

    return count

def count_x_mas_occurrences(grid):
    patterns = ["MAS", "SAM"]
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_x_mas(x, y):
        for pattern in patterns:
            if (is_valid(x-1, y-1) and is_valid(x, y) and is_valid(x+1, y+1) and
                grid[x-1][y-1] == pattern[0] and grid[x][y] == pattern[1] and grid[x+1][y+1] == pattern[2]):
                for pattern2 in patterns:
                    if (is_valid(x-1, y+1) and is_valid(x+1, y-1) and
                        grid[x-1][y+1] == pattern2[0] and grid[x][y] == pattern2[1] and grid[x+1][y-1] == pattern2[2]):
                        return True
        return False

    for r in range(1, rows-1):
        for c in range(1, cols-1):
            if search_x_mas(r, c):
                count += 1

    return count

grid = read_grid_from_file('input.txt')
print("XMAS occurrences:", count_xmas_occurrences(grid))
print("X-MAS occurrences:", count_x_mas_occurrences(grid))