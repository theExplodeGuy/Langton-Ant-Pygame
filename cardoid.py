import pygame

col_1 = (55, 6, 23)
col_2 = (106, 4, 15)
col_3 = (157, 2, 8)
col_background = (255, 255, 255)
col_grid = (255, 255, 255)


class Ant:

    def __init__(self):
        self.x = 100
        self.y = 100
        self.angle = 90


def init(dimx, dimy):
    cells = [[0 for x in range(dimy)] for y in range(dimx)]
    return cells


def colour(cur, x, y):
    if cur[x][y] == 0:
        col = col_background
    elif cur[x][y] == 1:
        col = col_1
    elif cur[x][y] == 2:
        col = col_2
    elif cur[x][y] == 3:
        col = col_3
    else:
        cur[x][y] = 0
        col = col_background
    return col


def update(surface, cur, sz, ant):
    # clockwise

    if ant.angle == 90 and (
            (cur[ant.x][ant.y] == 0 or cur[ant.x][ant.y] == 1)):
        ant.angle += 90
        cur[ant.x][ant.y] += 1
        col = colour(cur, ant.x, ant.y)
        pygame.draw.rect(surface, col, (ant.y * sz, ant.x * sz, sz, sz))
        ant.x = (ant.x - 1) % len(cur[0])

    # anti-clockwise
    elif ant.angle == 90 and (cur[ant.x][ant.y] == 2 or cur[ant.x][ant.y] == 3):
        ant.angle -= 90
        cur[ant.x][ant.y] += 1
        col = colour(cur, ant.x, ant.y)
        pygame.draw.rect(surface, col, (ant.y * sz, ant.x * sz, sz, sz))
        ant.x = (ant.x + 1) % len(cur[0])

    # clockwise
    elif ant.angle == 180 and (
            (cur[ant.x][ant.y] == 0 or cur[ant.x][ant.y] == 1)):
        ant.angle += 90
        cur[ant.x][ant.y] += 1
        col = colour(cur, ant.x, ant.y)
        pygame.draw.rect(surface, col, (ant.y * sz, ant.x * sz, sz, sz))
        ant.y = (ant.y - 1) % len(cur)

    # anti-clockwise
    elif ant.angle == 180 and (cur[ant.x][ant.y] == 2 or cur[ant.x][ant.y] == 3):
        ant.angle -= 90
        cur[ant.x][ant.y] += 1
        col = colour(cur, ant.x, ant.y)
        pygame.draw.rect(surface, col, (ant.y * sz, ant.x * sz, sz, sz))
        ant.y = (ant.y + 1) % len(cur)

    # clockwise
    if ant.angle == 270 and (
            (cur[ant.x][ant.y] == 0 or cur[ant.x][ant.y] == 1)):
        ant.angle += 90
        cur[ant.x][ant.y] += 1
        col = colour(cur, ant.x, ant.y)
        pygame.draw.rect(surface, col, (ant.y * sz, ant.x * sz, sz, sz))
        ant.x = (ant.x + 1) % len(cur[0])

    elif ant.angle == 270 and (cur[ant.x][ant.y] == 2 or cur[ant.x][ant.y] == 3):
        ant.angle -= 90
        cur[ant.x][ant.y] += 1
        col = colour(cur, ant.x, ant.y)
        pygame.draw.rect(surface, col, (ant.y * sz, ant.x * sz, sz, sz))
        ant.x = (ant.x - 1) % len(cur[0])

    # clockwise
    elif ant.angle == 0 and (
            (cur[ant.x][ant.y] == 0 or cur[ant.x][ant.y] == 1)):
        ant.angle += 90
        cur[ant.x][ant.y] += 1
        col = colour(cur, ant.x, ant.y)
        pygame.draw.rect(surface, col, (ant.y * sz, ant.x * sz, sz, sz))
        ant.y = (ant.y + 1) % len(cur)

    elif ant.angle == 0 and (cur[ant.x][ant.y] == 2 or cur[ant.x][ant.y] == 3):
        ant.angle -= 90
        cur[ant.x][ant.y] += 1
        col = colour(cur, ant.x, ant.y)
        pygame.draw.rect(surface, col, (ant.y * sz, ant.x * sz, sz, sz))
        ant.y = (ant.y - 1) % len(cur)

    if ant.angle >= 360:
        ant.angle = 0

    if ant.angle == -90:
        ant.angle = 270

    if ant.angle == -180:
        ant.angle = 180

    print(ant.angle)
    return cur


def main(dimx, dimy, cellsize):
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("Langton's Ant")
    surface.fill(col_grid)
    cells = init(dimx, dimy)
    ant = Ant()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        cells = update(surface, cells, cellsize, ant)
        pygame.display.update()


if __name__ == "__main__":
    main(200, 200, 5)
