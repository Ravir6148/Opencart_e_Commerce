import random
import string

def random_string_generator(size = 5, char =string.ascii_lowercase + string.digits):
    return ''.join(random.choice(char) for x in range(size))