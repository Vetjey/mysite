import random
count_multipy = 0
right_multipy = 0

def multiplicate():
    first_int = random.randint(2, 9)
    second_int = random.randint(2, 9)
    multipy = first_int*second_int
    print('%s*%s=...' % (first_int, second_int))
    user_answer = int(input())
    if multipy == user_answer:
        print('Верно!')
    else:
        print('Ты ошибся... Правильный ответ:%s' % (multipy))
    print(' ')
    print(' ')

for i in range(100):
    multiplicate()