from resistor_values import color_values, multipliers, tolerance, temperature_coef

def calculate_resistor(colors, number_bands):

    if number_bands == 4:

        band1 = color_values[colors[0]]
        band2 = color_values[colors[1]]
        multiplier = multipliers[colors[2]]
        tol = tolerance[colors[3]]
        temp_coef = None

        value = (band1 * 10 + band2) * multiplier


    elif number_bands == 5:

        band1 = color_values[colors[0]]
        band2 = color_values[colors[1]]
        band3 = color_values[colors[2]]
        multiplier = multipliers[colors[3]]
        tol = tolerance[colors[4]]
        temp_coef = None

        value = (band1 * 100 + band2 * 10 + band3) * multiplier


    elif number_bands == 6:

        band1 = color_values[colors[0]]
        band2 = color_values[colors[1]]
        band3 = color_values[colors[2]]
        multiplier = multipliers[colors[3]]
        tol = tolerance[colors[4]]
        temp_coef = temperature_coef[colors[5]]

        value = (band1 * 100 + band2 * 10 + band3) * multiplier

    return value, tol, temp_coef