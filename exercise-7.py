import random

def random_password(): return ''.join(chr(random.randrange(33, 126, 2)) for _ in range(random.randrange(7, 10, 2)))