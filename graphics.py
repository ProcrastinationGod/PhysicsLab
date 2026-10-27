from simulateFlight import FlightSimulation
import matplotlib.pyplot as plt

# Этап 2. 
withAirResistance = FlightSimulation(airResistance=True)
print("Полет с сопротивлением воздуха:")
print(f"\tДальность полета (L, м): {withAirResistance.L}")
print(f"\tМаксимальная высота полета (H, м): {withAirResistance.H}")
print(f"\tПолное время полета (T, c): {withAirResistance.T}")
print(f"\tКонечная скорость в момент соприкосновения с землей (v_max, м/с): {withAirResistance.v_end}")
print(f"\tВремя подъёма и время спуска (t_up, t_down): {withAirResistance.t_up}, {withAirResistance.t_down}")

withoutAirResistance = FlightSimulation(airResistance=False)
print("Полет без сопротивлением воздуха:")
print(f"\tДальность полета (L, м): {withoutAirResistance.L}")
print(f"\tМаксимальная высота полета (H, м): {withoutAirResistance.H}")
print(f"\tПолное время полета (T, c): {withoutAirResistance.T}")
print(f"\tКонечная скорость в момент соприкосновения с землей (v_max, м/с): {withoutAirResistance.v_end}")
print(f"\tВремя подъёма и время спуска (t_up, t_down): {withoutAirResistance.t_up}, {withoutAirResistance.t_down}")

# Этап 1.
plt.plot(*zip(*withAirResistance.list_coords), color="blue")
plt.plot(*zip(*withoutAirResistance.list_coords), color="red")

plt.xlabel("Координата X, м")
plt.ylabel("Координата Y, м")
plt.grid(True)
plt.show()