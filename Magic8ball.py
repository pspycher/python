import random

# Gibt zufällig eine aus acht Antworten

def magic8():
    a = 'It is certain'
    b = 'It is decidedly so'
    c = 'Yessss'
    d = 'Reply hazy try again'
    e = 'Ask again'
    f = 'Concentrate'
    g = 'NO'
    h = 'Not so good'

    random_number = random.randint(1, 8)
    print(random_number)

    if random_number == 1:
        print(a)
    if random_number == 2:
        print(b)
    if random_number == 3:
        print(c)
    if random_number == 4:
        print(d)
    if random_number == 5:
        print(e)
    if random_number == 6:
        print(f)
    if random_number == 7:
        print(g)
    if random_number == 8:
        print(h)

magic8()