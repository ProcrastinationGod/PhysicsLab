from simulateFlight import FlightSimulation
import matplotlib.pyplot as plt

withAirResistance = FlightSimulation(airResistance=True)
print("Полет с сопротивлением воздуха:")
print(f"\tДальность полета (L, м): {withAirResistance.L}")
print(f"\tМаксимальная высота полета (H, м): {withAirResistance.H}")
print(f"\tПолное время полета (T, c): {withAirResistance.L}")
print(f"\tКонечная скорость в момент соприкосновения с землей (v_max, м/с): {withAirResistance.v_end}")

withoutAirResistance = FlightSimulation(airResistance=False)
print("Полет без сопротивлением воздуха:")
print(f"\tДальность полета (L, м): {withoutAirResistance.L}")
print(f"\tМаксимальная высота полета (H, м): {withoutAirResistance.H}")
print(f"\tПолное время полета (T, c): {withoutAirResistance.L}")
print(f"\tКонечная скорость в момент соприкосновения с землей (v_max, м/с): {withoutAirResistance.v_end}")

plt.plot(*zip(*withAirResistance.list_coords), color="blue")
plt.plot(*zip(*withoutAirResistance.list_coords), color="red")

plt.xlabel("Координата X, м")
plt.ylabel("Координата Y, м")
plt.grid(True)
plt.show()