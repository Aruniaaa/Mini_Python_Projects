import pygame
import math
from queue import PriorityQueue

"""
🔦 USER GUIDE!! 🔦

1. To start, run the program and right click on any square to make it where the maze/path starts from.
2. Click on any other random square to make it the end/goal square that the path finder has to reach.
3. Now, feel free to add barriers anywhere you want, make sure to use left click to do all of the above.
NOTE - If you want to remove a barrier/start/end, just right click on that square and it should be removed.
4. After you have defined the start, end, and barriers (option), you can press the space bar and the program should 
start running, and the pathfinder will start highlighting squares as red and green.
Once the pathfinder finds the way, you can press 'r' to restart and play the game again, repeating all the steps from 
1-4 again.
"""


WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255, 179, 186)
GREEN = (186, 255, 201)
BLUE = (174, 198, 255)
YELLOW = (255, 255, 186)
WHITE = (255, 255, 255)
BLACK = (64, 64, 64)
PURPLE = (219, 190, 255)
ORANGE = (255, 223, 186)
GREY = (200, 200, 200)
TURQUOISE = (180, 255, 255)


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.color = WHITE
        self.total_rows = total_rows
        self.x = row * width
        self.y = col * width

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_barrier(self):
        return self.color == BLACK

    def is_open(self):
        return self.color == GREEN

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_closed(self):
        self.color = RED


    def make_barrier(self):
        self.color = BLACK

    def make_open(self):
        self.color = GREEN


    def make_start(self):
        self.color = ORANGE


    def make_end(self):
        self.color = TURQUOISE


    def make_path(self):
        self.color = PURPLE


    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows -1 and not grid[self.row + 1][self.col].is_barrier(): # down
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # up
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # right
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.row > 0 and not grid[self.row ][self.col - 1].is_barrier(): # left
            self.neighbors.append(grid[self.row ][self.col - 1])

    def __lt__(self, other):
        return False


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, end, draw):
    while end in came_from:
        end = came_from[end]
        end.make_path()
        draw()


def algorithm(draw, grid, start, end, ):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g = {node : float("inf") for row in grid for node in row}
    g[start] = 0
    f = {node: float("inf") for row in grid for node in row}
    f[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        for neighbor in current.neighbors:
            temp_g = g[current] + 1
            if temp_g < g[neighbor]:
                came_from[neighbor] = current
                g[neighbor] = temp_g
                f[neighbor] = temp_g + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()
        if current != start:
            current.make_closed()

    return False









def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			node = Node(i, j, gap, rows)
			grid[i].append(node)

	return grid


def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
	win.fill(WHITE)

	for row in grid:
		for node in row:
			node.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(win, width):
    ROWS = 30


    grid = make_grid(ROWS, width)

    start = None
    end = None
    started = False
    run = True

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(mouse_pos, ROWS, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.make_start()

                elif not end and node != start:
                    end = node
                    end.make_end()

                elif node != end and node != start:
                    node.make_barrier()



            elif pygame.mouse.get_pressed()[2]:
                mouse_pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(mouse_pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = end
                if node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                if event.key == pygame.K_r:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)





main(WIN, WIDTH)
pygame.quit()





