from simulateFlight import FlightSimulation
import matplotlib.pyplot as plt

flightResults = []

for angle in range(10, 81):
    L = FlightSimulation(airResistance=True, alpha=angle).L
    flightResults.append((L, angle))

optimalAngle = max(flightResults)[1]
print(f"Оптимальный угол полета: {optimalAngle}")

plt.plot(*zip(*map(lambda x: (x[1], x[0]),flightResults)), color="red")
plt.xlabel("угол a, градусы")
plt.ylabel("Дальность полета, м")
plt.grid(True)
plt.show()

vacuumOptimalFlight = FlightSimulation(airResistance=False, alpha=45)
withResistanceOptimalFlight = FlightSimulation(airResistance=True, alpha=optimalAngle)

plt.plot(*zip(*vacuumOptimalFlight.list_coords), color="red")
plt.plot(*zip(*withResistanceOptimalFlight.list_coords), color="blue")

plt.xlabel("Координата X, м")
plt.ylabel("Координата Y, м")
plt.grid(True)
plt.show()