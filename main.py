#!/usr/bin/python3

def countdown(n):
    while n >= 1:
        print(n)
        n -= 1

def countup(n):
    for i in range(1, n + 1):
        print(i)

def count_by_twos(n):
    for i in range(2, n + 1, 2):
        print(i)

def count_by_fives(n):
    for i in range(5, n + 1, 5):
        print(i)

def count_by_tens(n):
    for i in range(n, -1, -10):
        print(i)

# # countdown TEST
# test1 = countdown(5)
# test2 = countdown(10)
# test3 = countdown(20)

# print(test1)
# print(test2)
# print(test3)

# # countup TEST
# test1 = countup(5)
# test2 = countup(10)
# test3 = countup(20)

# print(test1)
# print(test2)
# print(test3)

# # count_by_twos TEST
# test1 = count_by_twos(6)
# test2 = count_by_twos(10)
# test3 = count_by_twos(20)

# print(test1)
# print(test2)
# print(test3)


# # count_by_fives TEST
# test1 = count_by_fives(15)
# test2 = count_by_fives(45)
# test3 = count_by_fives(120)

# print(test1)
# print(test2)
# print(test3)

# # count_by_tens TEST
# test1 = count_by_tens(40)
# test2 = count_by_tens(560)
# test3 = count_by_tens(210)

# print(test1)
# print(test2)
# print(test3)
