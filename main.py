from random import randrange, choice

NUMS_PER_LETTER = 10


def create_card():
    card = {}
    lower = 1
    upper = 1 + NUMS_PER_LETTER

    for letter in range(1, 10):
        card[letter] = []

        while len(card[letter]) != 3:
            next_num = randrange(lower, upper)
            if next_num not in card[letter]:
                card[letter].append(next_num)

        lower = lower + NUMS_PER_LETTER
        upper = upper + NUMS_PER_LETTER

    horizontal_line = []
    for i in range(0, 3):
        for k, value in card.items():
            horizontal_line.append(card[k][i])

    split_horizontal_card = [horizontal_line[0:9], horizontal_line[9: 18],
                             horizontal_line[18:28]]

    for i in split_horizontal_card:
        random_number = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for k in range(0, 4):
            t = choice(random_number)
            random_number.remove(t)
            i[t] = 0

    return split_horizontal_card


et = create_card()
for i in et:
    print(i)
