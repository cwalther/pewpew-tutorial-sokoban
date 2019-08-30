import pew

pew.init()
screen = pew.Pix.from_iter((
    (1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 1, 1, 1, 1, 1, 1, 1),
))

x = 4
y = 1

while True:
    screen.pixel(x, y, 0)
    keys = pew.keys()
    if keys & pew.K_UP:
        y -= 1
    elif keys & pew.K_DOWN:
        y += 1
    elif keys & pew.K_LEFT:
        x -= 1
    elif keys & pew.K_RIGHT:
        x += 1
    screen.pixel(x, y, 3)
    pew.show(screen)
    pew.tick(1/6)
