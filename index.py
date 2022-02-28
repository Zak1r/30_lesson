# 121

# from random import randint, randrange

# print(randrange(1, 49 + 1))
# print(randint(1, 49))


# ! КОД

# from random import randint

# MIN_NUM = 1
# MAX_NUM = 49
# NUM_NUMS = 6

# ticket_nums = []

# for i in range(NUM_NUMS):
#     rand = randint(MIN_NUM, MAX_NUM)
#     while rand in ticket_nums:
#         rand = randint(MIN_NUM, MAX_NUM)
#     ticket_nums.append(rand)

# ticket_nums.sort()
# for tn in ticket_nums:
#     print(tn, end=' ')


# 123
# vowels = ["a", "e", "i", "o", "u"]
# consonats = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

# human_text = input('Type yor text here: ')
# words = human_text.split(' ')
# for word in words:
#     for letter in word:
#         print(letter)

# vowels = ["a", "e", "i", "o", "u"]
# consonats = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

# human_text = input('Type yor text here: ')
# words = human_text.split(' ')
# pig_text_list =[]
# for word in words:
#     if word[0].lower() in vowels:
#         pig_word = word + 'way'
#         word + 'way'
#         continue
#     end_letters = []
#     for letter in word:
#         if not(letter in vowels):
#             end_letters.append(letter.lower())
#         else:   break
#     pig_word = word[len(end_letters):] + ''.join(end_letters) + 'ay'
#     pig_text_list.append(pig_word)
# print(''.join(pig_text_list))


# 124

points_num = int(input('How many points are you going to create: '))

points = []
for i in range(points_num):
    pair = []
    x = float(input('Enter x: '))
    y = float(input('Enter y: '))
    points.append([x, y])

#  sum X
sumX = 0
sumY = 0
sumXY = 0
sumX_squared = 0
for pair in points:
    sumX = sumX + pair[0]
    sumY = sumY + pair[1]
    sumXY = sumXY + pair[0] * pair[1]
    sumX_squared = sumX_squared + pair[0] ** 2

n = points_num
m = (sumXY - (sumX * sumY)/(n))/(sumX_squared - (sumX ** 2) / (n))

meanX = sumX / n
meanY = sumY / n

b = meanY - m * meanX 

m = round(m, 2)
b = round(b, 2)

print(f'y = {m}x + {b}')