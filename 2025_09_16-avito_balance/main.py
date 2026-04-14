import pyautogui as pag


def click(t, x, y):
    pag.moveTo(x, y, t)
    pag.click()


def find(items, time):
    for x, y in items:
        click(time, x, y)
        click(0.5, 720, 600)
    click(1, 720, 600)


def game(start_x, start_y, items, time, first_game=False):
    click(1, start_x, start_y)
    click(0.4, 720, 600)
    if first_game:
        click(0.4, 720, 600)
    find(items, time)


# exit from console
click(1, 200, 400)

# main menu
click(0.5, 435, 605)  # cookies
click(0.5, 955, 445)  # elevator call button
click(2.5, 720, 600)  # ok
click(0.4, 720, 600)  # ok

# cat game
game(640, 360, [
    (982, 600), (759, 538), (593, 500), (428, 467),
    (944, 575), (528, 533), (516, 382), (761, 328)
], 0.18, True)

# crab game
game(800, 360, [
    (392, 605), (880, 450), (998, 540), (815, 520),
    (1016, 467), (569, 359), (1096, 458), (386, 533)
], 0.15)

# kubernetes game
game(640, 430, [
    (799, 528), (1094, 435), (1055, 547), (869, 419),
    (467, 607), (376, 436), (403, 577), (763, 433)
], 0.15)

# swing game
game(800, 430, [
    (610, 499), (928, 472), (1083, 537), (688, 416),
    (820, 458), (474, 503), (764, 537), (885, 512)
], 0.15)

# coffee game
game(640, 500, [
    (373, 433), (696, 550), (1090, 556), (433, 611),
    (526, 543), (1028, 462), (523, 460), (1027, 571)
], 0.15)

# grass game
game(800, 500, [
    (1097, 454), (679, 415), (432, 617), (480, 501),
    (603, 495), (903, 433), (545, 373), (934, 429)
], 0.15)
