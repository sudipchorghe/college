print("Enter a choice of code")
print("1. Audio frequency check")
print("2. Frequency band classification")
print("3. Resistor value by color")
print("4. Battery voltage checker")
print("5. Tolerance checker")

choice = int(input("Enter your choice (1-5): "))

match choice:
    case 1:
        # Audio frequency check
        f = float(input("Enter the frequency in Hz: "))
        if f <= 20000:
            print("Audio frequency is (AM)")
        else:
            print("Audio frequency is (RF)")

    case 2:
        # Frequency band classification
        f = float(input("Enter frequency in Hz: "))
        if 30000 <= f <= 300000:
            print("VLF band")
        elif 300000 <= f <= 3000000:
            print("LF band")
        elif 3000000 <= f <= 30000000:
            print("HF band")
        elif 30000000 <= f <= 300000000:
            print("VHF band")
        else:
            print("Frequency not in standard range")

    case 3:
        # Resistor value by color
        color = input("Enter the color of band: ").lower()
        if color == "black":
            print("The value of band is = 0")
        elif color == "brown":
            print("The value of band is = 1")
        elif color == "red":
            print("The value of band is = 2")
        elif color == "orange":
            print("The value of band is = 3")
        elif color == "yellow":
            print("The value of band is = 4")
        elif color == "green":
            print("The value of band is = 5")
        elif color == "blue":
            print("The value of band is = 6")
        elif color == "violet":
            print("The value of band is = 7")
        elif color == "grey":
            print("The value of band is = 8")
        elif color == "white":
            print("The value of band is = 9")
        else:
            print("Enter a valid color")

    case 4:
        # Battery voltage checker
        voltage = float(input("Enter the voltage of battery: "))
        if 1 <= voltage <= 3.7:
            print("Battery is charging")
        elif 3.7 <= voltage <= 4.2:
            print("Battery is charged")
        else:
            print("Over/under voltage, battery is damaged!!!")

    case 5:
        # Tolerance checker
        nominal_resistance = 100
        tolerance_percent = 5
        measured_resistance = float(input("Enter measured resistance: "))

        tolerance = nominal_resistance * (tolerance_percent / 100)
        lower_limit = nominal_resistance - tolerance
        upper_limit = nominal_resistance + tolerance

        if lower_limit <= measured_resistance <= upper_limit:
            print("The resistor is within tolerance")
        else:
            print("The resistor is outside tolerance range")

    case _:
        print("Invalid choice")