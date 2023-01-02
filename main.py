from random import randint, sample

bingo_card_dict = {
    9: [0, 0, 0],
    8: [0, 0, 0],
    7: [0, 0, 0],
    6: [0, 0, 0],
    5: [0, 0, 0],
    4: [0, 0, 0],
    3: [0, 0, 0],
    2: [0, 0, 0],
    1: [0, 0, 0],
}


dict1 = bingo_card_dict.copy()

for k, value in dict1.items():
    a = sample(range(1 + 10 * (k - 1), 11 + 10 * (k - 1)), k=3)
    dict1[k] = sample(range(1 + 10 * (k - 1), 11 + 10 * (k - 1)), k=3)


