import random


def roll_d6(dice_amount: int) -> int:
    sum_value = 0
    for i in range(dice_amount):
        dice = random.randint(1, 6)
        sum_value += dice
    return sum_value


def roll_d10(dice_amount: int) -> int:
    sum_value = 0
    for i in range(dice_amount):
        dice = random.randint(1, 10)
        sum_value += dice
    return sum_value


def roll_d66() -> int:
    return (random.randint(1, 6) * 10) + random.randint(1, 6)


def roll_d100() -> int:
    return random.randint(1, 100)
