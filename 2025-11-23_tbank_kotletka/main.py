names = [
    "Идея-огонь",
    "Топливо энтузиазма",
    "Прогрев перед запуском",
    "Пожар дедлайнов",
    "Искра брейншторма",
    "Генератор смыслов",
    "Флешка-факел",
    "Пылающий инсайт"
]

price_coefs = {
    "Идея-огонь": (7.5, 1.15),
    "Топливо энтузиазма": (13.5, 1.15),
    "Прогрев перед запуском": (24.3, 1.15),
    "Пожар дедлайнов": (60.8, 1.2),
    "Искра брейншторма": (212.8, 1.2),
    "Генератор смыслов": (744.8, 1.2),
    "Флешка-факел": (1862, 1.22),
    "Пылающий инсайт": (3724, 1.22),
}

stars_coefs = {
    "Идея-огонь": (2, 3),
    "Топливо энтузиазма": (3, 3),
    "Прогрев перед запуском": (4, 3),
    "Пожар дедлайнов": (5, 4),
    "Искра брейншторма": (6, 4),
    "Генератор смыслов": (7, 5),
    "Флешка-факел": (8, 5),
    "Пылающий инсайт": (9, 5),
}

income_coefs = {
    "Идея-огонь": 1.4,
    "Топливо энтузиазма": 11 / 6,
    "Прогрев перед запуском": 7 / 3,
    "Пожар дедлайнов": 4.5,
    "Искра брейншторма": 9,
    "Генератор смыслов": 18,
    "Флешка-факел": 36,
    "Пылающий инсайт": 72,
}


def price(name, level):
    a, b = price_coefs[name]
    return round(a * (b ** level))


def stars(name, level):
    a, b = stars_coefs[name]
    if level < 20:
        return round(a + b * level)
    else:
        return round(a + b * 19 + (b - 2) * (level - 19))


def income(name, level):
    a = income_coefs[name]
    return round(a * level)


def payback_period(name, level):
    return price(name, level) / income(name, level)


levels = list(map(int, input().split()))
assert len(levels) == 8
for i in range(8):
    print(
        names[i],
        income(names[i], levels[i]),
        stars(names[i], levels[i]),
        price(names[i], levels[i]),
    )
print()

while True:
    i_, p_ = 0, payback_period(names[0], levels[0])
    for i in range(1, 8):
        p = payback_period(names[i], levels[i])
        if p < p_:
            i_, p_ = i, p
    levels[i_] += 1
    print(names[i_], p_, end="")
    input()
