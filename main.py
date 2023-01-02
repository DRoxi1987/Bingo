from random import sample, randint

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
    dict1[k] = sample(range(1 + 10 * (k - 1), 11 + 10 * (k - 1)), k=3)
    for a in range(0, randint(0, 3)):
        dict1[k][randint(0, 2)] = 0

print(dict1)
