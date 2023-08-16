import random
import turtle
import math
from turtle import *

compliments = [
    "Ты самая красивая девушка в мире!",
    "Твоя улыбка светит ярче самого яркого солнца!",
    "Ты такая умная и обаятельная!",
    "С тобой все проблемы кажутся ничтожными!",
    "Твоя креативность всегда вдохновляет меня!",
]
compliment = random.choice(compliments)
print(compliment)

def xt(t):
    return 16 * math.sin(t) ** 3
def yt(t):
    return 13 * math.cos(t) - 5 \
           * math.cos(2 * t) - 2 * \
           math.cos(3 * t) - math.cos(4 * t)
