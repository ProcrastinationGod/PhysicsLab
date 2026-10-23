from simulateFlight import FlightSimulation

flightResults = []
for angle in range(10, 81):
    print(f"Угол {angle}. Дальность полета: ", end="")
    L = FlightSimulation().simulate(airResistance=True, alpha=angle).L
    print(L)
    flightResults.append((L, angle))
print(max(flightResults))