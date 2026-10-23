from simulateFlight import FlightSimulation
import matplotlib.pyplot as plt

withAirResistance = FlightSimulation()
withAirResistance.simulate(airResistance=True)

plt.plot(*zip(*withAirResistance.list_coords), color="blue")

withoutAirResistance = FlightSimulation()
withoutAirResistance.simulate(airResistance=False)

plt.plot(*zip(*withoutAirResistance.list_coords), color="red")

plt.xlabel("Координата X, м")
plt.ylabel("Координата Y, м")
plt.grid(True)
plt.show()