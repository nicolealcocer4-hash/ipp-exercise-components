"""
This module contains temperature conversion functions.
"""

min_indoor_temp_F = 65.0
max_indoor_temp_F = 85.0


def isDesiredIndoorTempRange(temp: float, is_celsius: bool) -> bool:
    """
    Determines whether a temperature is within the desired indoor range.

    :param temp: Temperature value to evaluate
    :param is_celsius: Boolean indicating if the temperature is in Celsius
    :return: True if temperature is within range, otherwise False
    """
    if min_indoor_temp_F <= temp <= max_indoor_temp_F:
        return True
    else:
        return False

print(isDesiredIndoorTempRange(70.0, False))
print(isDesiredIndoorTempRange(50.0, False))


"""
This module contains temperature conversion functions.
"""

def convertTempFtoC(tempInF: float = 0.0) -> float:
    """
    Converts Fahrenheit to Celsius.
    """
    celsius = (5 / 9) * (tempInF - 32)
    celsius = round(celsius, 1)
    print(f"{tempInF}°F is {celsius}°C")
    return celsius


def convertTempCtoF(tempInC: float = 0.0) -> float:
    """
    Converts Celsius to Fahrenheit.
    """
    fahrenheit = (tempInC * 9 / 5) + 32
    fahrenheit = round(fahrenheit, 1)
    print(f"{tempInC}°C is {fahrenheit}°F")
    return fahrenheit


if __name__ == "__main__":
    orig_f_val = 72.0
    c_val = convertTempFtoC(orig_f_val)
    f_val = convertTempCtoF(c_val)

    if orig_f_val == f_val:
        print("The temp converter works!")
    else:
        print("The temp converter failed!")
