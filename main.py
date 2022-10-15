import string
import random
def random_char(num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(num))

print(random_char(5))
input()
