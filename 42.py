import math

def is_tri(t):
    root = int(math.sqrt(1+8*t))
    if (root+1)*(root+1) == 1+8*t:
        root += 1
    if root*root != 1+8*t:
        return False

    n = (-1+root)/2.0
    return abs(n-int(n)) < 1e-6


def convert(word):
    t = 0
    for char in word:
        t += ord(char)-ord('A')+1
    return t

ans = 0
words = open("42.txt").read().split(",")
for word in words:
    word = word.strip('"')
    t = convert(word)
    if is_tri(t):
        ans += 1
print ans