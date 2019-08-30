import pew

pew.init()
screen = pew.Pix.from_iter((
    (1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 3, 0, 2, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 1, 1, 1, 1, 1, 1, 1),
))

x = 4
y = 1
blink = True

while True:
    screen.pixel(x, y, 0)
    keys = pew.keys()
    dx = 0
    dy = 0
    if keys & pew.K_UP:
        dy = -1
    elif keys & pew.K_DOWN:
        dy = 1
    elif keys & pew.K_LEFT:
        dx = -1
    elif keys & pew.K_RIGHT:
        dx = 1
    target = screen.pixel(x+dx, y+dy)
    behind = screen.pixel(x+dx+dx, y+dy+dy)
    if target in {0, 2}:
        x += dx
        y += dy
    elif target == 3 and behind in {0, 2}:
        screen.pixel(x+dx+dx, y+dy+dy, 3)
        x += dx
        y += dy
    screen.pixel(x, y, 3 if blink else 2)
    blink = not blink
    pew.show(screen)
    pew.tick(1/6)
