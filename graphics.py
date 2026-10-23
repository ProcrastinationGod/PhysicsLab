import withAirResistance, withoutAirResistance
import matplotlib.pyplot as plt

# Без сопротивления воздуха
plt.plot(*zip(*withoutAirResistance.list_coords), color="blue")

# С сопротивлением воздуха
plt.plot(*zip(*withAirResistance.list_coords), color="red")

plt.xlabel("Координата X, м")
plt.ylabel("Координата Y, м")
plt.grid(True)
plt.show()
