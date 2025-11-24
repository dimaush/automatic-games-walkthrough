import pyautogui as pag
from time import sleep
from threading import Thread


rows, cols = 5, 18  # size of grid
w, h = 30, 41  # width of card

_coords = {
    "out": (1350, 450),
    "zoom": (472, 400),
    "broom": (500, 270),
    "grid": (500, 310),
    "plus5": (1100, 570),
    "machine": (547, 375),
    "machine_big": (660, 330),
    "esc": (915, 470),
    "trash": (800, 260),
}  # important coordinates

dh = {
    0.5: 5,
    0.4: 6,
    0.3: 10,
    0.2: 14,
    0.18: 20,
    0.16: 21,
}  # length of grab gap depending on time of grab

gift = (191, 188, 182, 255)
craft = (93, 93, 152, 255)

black = (62, 62, 70, 255)
black_known = (131, 136, 158, 255)
black_gold = (157, 157, 161, 255)

white = (254, 248, 239, 255)
white_known = (194, 197, 213, 255)
white_gold = (255, 252, 247, 255)

good = (craft, black, white)


def click(place, clicks=1):
    for _ in range(clicks):
        pag.click(*_coords[place])
    sleep(0.5)


def hide_terminal():
    click("out")


def clean_field():
    click("broom")


def fill_field():
    click("plus5", 20)


def make_grid():
    click("grid")


def zoom_out():
    pag.moveTo(*_coords["zoom"])
    for _ in range(10):
        pag.scroll(-1)
    sleep(0.5)


def prepare_game():
    make_grid()
    zoom_out()


def deactivate_machine():
    click("machine_big")
    click("esc")


def coords(i, j):
    s_x, s_y = _coords["machine"]
    return s_x + w * i, s_y + h * j


def move_to_card(i, j):
    pag.moveTo(*coords(i, j), 0.1)


def grab(action=None):
    pag.move(0, -dh[T])
    pag.mouseDown()
    pag.move(0, dh[T] + h, T)
    pag.move(0, -h, 0.1)
    if action:
        action()
    pag.mouseUp()


def coords_screenshot(i, j):
    x, y = coords(i, j)
    return 2 * x, 2 * y


def shot(i, j):
    screenshot = None

    def capture():
        nonlocal screenshot
        sleep(T + 0.45)
        screenshot = pag.screenshot()

    pag.moveTo(*coords(i, j))
    capture_thread = Thread(target=capture)
    capture_thread.start()
    grab()
    capture_thread.join()
    return screenshot


def get_breed_list(i, j, is_job):
    screenshot = shot(i, j)
    breed_list = []
    for i1 in range(i, -1, -1):
        r = j - 1 if i1 == i else rows - 1
        for j1 in range(r, -1, -1):
            test_pixel_coords = coords_screenshot(i1, j1)
            test_pixel = screenshot.getpixel(test_pixel_coords)
            if is_job and test_pixel in good or test_pixel == black:
                if len(breed_list) == M:
                    return breed_list, True
                breed_list.append((i1, j1))
    return breed_list, False


def play(i, j):
    card_color = pag.screenshot().getpixel(coords_screenshot(i, j))
    if card_color not in good:
        return False
    is_job = (card_color == black)
    breed_list, again = get_breed_list(i, j, is_job)
    if breed_list:
        while True:
            for card in breed_list:
                grab(lambda: move_to_card(*card))
                sleep(0.2)
            card_color = pag.screenshot().getpixel(coords_screenshot(*card))
            is_job = (card_color == black)
            if again:
                breed_list, again = get_breed_list(*card, is_job)
            else:
                break
    return True


# hyperparameters
T = 0.3
M = 5


hide_terminal()
clean_field()
make_grid()
deactivate_machine()
fill_field()
prepare_game()
for i in range(cols - 1, -1, -1):
    for j in range(rows - 1, -1, -1):
        if play(i, j):
            grab(lambda: pag.moveTo(*_coords["trash"], duration=0.1))
        prepare_game()
