import math
import matplotlib.pyplot as plt
from constants import *

S = math.pi * (D / 2) ** 2
# Перевод alpha в радианы
alpha = math.radians(alpha)

y = y_0
x = x_0
v_x = v_0 * math.cos(alpha)
v_y = v_0 * math.sin(alpha)
t = 0.0

list_coords = []

while y >= 0:
    list_coords.append((x, y))

    v = math.sqrt(v_x ** 2 + v_y ** 2)

    a_x = 0.0
    a_y = -g
    x += v_x * dt
    y += v_y * dt

    v_x += a_x * dt
    v_y += a_y * dt
    t += dt
