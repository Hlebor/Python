def time_to_travel_around_planet(robot_speed,planet_diameter):
    if robot_speed <= 0 or planet_diameter <= 0:
        return "Скорость и диаметр должны быть положительными числами!"
    time = 3.14159 * planet_diameter / robot_speed
    return time

calculation_1 = time_to_travel_around_planet(0, 100)

result = time_to_travel_around_planet(8, 10)
if isinstance(result, str):
        print(result)
else:
        print(f"Время для объезда планеты: {result:.2f} часов")
