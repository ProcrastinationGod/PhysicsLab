import math
import matplotlib.pyplot as plt


class FlightSimulation:

    def __init__(self, airResistance, C_w=0.25, p=1.29, g=9.81, x_0=0.0, y_0=0.0, dt=0.001, m=0.22, D=0.27, v_0=17.6, alpha=63):
        # Вычисление площади поперечного сечения тела
        S = math.pi * (D / 2) ** 2
        # Перевод alpha в радианы
        alpha = math.radians(alpha)

        # Если сопротивление среды есть, то вычисляется коэффициент k, если нет, то k = 0 и сила сопротивления воздуха тоже будет равна 0
        if airResistance: 
            k = C_w * p * S / 2
        else:
            k = 0

        t = 0.0
        # x и y в момент t = 0
        y = y_0
        x = x_0

        # Проекции изначальной скорости на OX и OY
        v_x = v_0 * math.cos(alpha)
        v_y = v_0 * math.sin(alpha)

        # Список в который будут записываться переменные системы
        listVariables = []

        while y >= 0:
            # Находим скорость по формуле
            v = math.sqrt(v_x ** 2 + v_y ** 2)

            # Добавляем в список переменные система в момент времени t
            listVariables.append({
                            "coordinates" : (x, y),
                            "speed" : v,
                            "time" : t
                            })
            

            # Находим проекции ускорения на OX и OY
            a_x = -(k / m) * v * v_x
            a_y = -g - (k / m) * v * v_y

            # По формулам Эйлера меняем переменные
            x += v_x * dt
            y += v_y * dt

            v_x += a_x * dt
            v_y += a_y * dt
            t += dt

        self.list_coords = [item["coordinates"] for item in listVariables]
        self.T = listVariables[-1]["time"]
        self.L = listVariables[-1]["coordinates"][0]
        self.v_end = listVariables[-1]["speed"]

        max_height_item = max([item for item in listVariables], key=lambda x: x["coordinates"][1])
        self.H = max_height_item["coordinates"][1]
        self.t_up = max_height_item["time"]
        self.t_down = self.T - self.t_up
