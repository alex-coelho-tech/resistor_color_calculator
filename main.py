from resistor_logic import calculate_resistor

n_bands = int(input("Enter number of resistor bands: "))
colors = input("Enter resistor colors: ").lower().split()

value, tol, t_cf = calculate_resistor(colors, n_bands)

if n_bands <= 5:
    print(f"Resistance: {value} Ω ±{tol}%")
else:
    print(f"Resistance: {value} Ω ±{tol}% {t_cf} ppm/°C")