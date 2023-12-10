temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit of the temperature (C/F): ")

if unit.upper() == "C":
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature} Celsius = {fahrenheit} Fahrenheit")
elif unit.upper() == "F":
    celsius = (temperature - 32) * 5/9
    print(f"{temperature} Fahrenheit = {celsius} Celsius")
else:
    print("Invalid unit. Please enter either C or F.")
