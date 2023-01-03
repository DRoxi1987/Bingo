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

    return card


m = create_card()
print(m)

q = []
for i in range(0, 3):
    for k, value in m.items():
        q.append(m[k][i])

print(q)
z = [q[0:9], q[9: 18], q[18:28]]
for i in z:
    print(i)

    r = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for k in range(0, 4):
        t = choice(r)
        r.remove(t)
        print(t)
        if t not in r and i[t] != 0:
            i[t] = 0
    print(z)

