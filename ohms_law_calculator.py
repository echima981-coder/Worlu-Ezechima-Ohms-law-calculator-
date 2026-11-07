# Ohm's Law and Power Calculator
# Author: [Worlu Eze Chima]
# ND1 Mechatronics Engineering, YabaTech

def get_float(prompt):
    """Ask the user for a number and keep asking until a valid float is entered."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number (e.g. 12 or 3.5).")


def calculate():
    """Main calculation function. Returns a dictionary with the result or None if cancelled."""
    print("\nWhat do you want to calculate?")
    print("1. Voltage (V)")
    print("2. Current (I)")
    print("3. Resistance (R)")
    print("4. Power (P)")
    print("5. Quit")

    choice = input("Enter 1-5: ").strip()

    if choice == "5":
        return None

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please select 1, 2, 3, 4 or 5.")
        return "invalid"

    # ----- Voltage -----
    if choice == "1":
        print("\nCalculate Voltage (V = I × R)")
        current = get_float("Enter current in Amperes (I): ")
        resistance = get_float("Enter resistance in Ohms (R): ")
        voltage = current * resistance
        result = {
            "type": "Voltage",
            "value": voltage,
            "unit": "V",
            "formula": "V = I × R",
            "details": f"I = {current} A, R = {resistance} Ω"
        }
        print(f"\nVoltage = {voltage:.4f} V")
        print(f"Formula used: {result['formula']}")
        return result

    # ----- Current -----
    elif choice == "2":
        print("\nCalculate Current (I = V / R)")
        voltage = get_float("Enter voltage in Volts (V): ")
        resistance = get_float("Enter resistance in Ohms (R): ")
        if resistance == 0:
            print("Error: Resistance cannot be zero (division by zero).")
            return "invalid"
        current = voltage / resistance
        result = {
            "type": "Current",
            "value": current,
            "unit": "A",
            "formula": "I = V / R",
            "details": f"V = {voltage} V, R = {resistance} Ω"
        }
        print(f"\nCurrent = {current:.4f} A")
        print(f"Formula used: {result['formula']}")
        return result

    # ----- Resistance -----
    elif choice == "3":
        print("\nCalculate Resistance (R = V / I)")
        voltage = get_float("Enter voltage in Volts (V): ")
        current = get_float("Enter current in Amperes (I): ")
        if current == 0:
            print("Error: Current cannot be zero (division by zero).")
            return "invalid"
        resistance = voltage / current
        result = {
            "type": "Resistance",
            "value": resistance,
            "unit": "Ω",
            "formula": "R = V / I",
            "details": f"V = {voltage} V, I = {current} A"
        }
        print(f"\nResistance = {resistance:.4f} Ω")
        print(f"Formula used: {result['formula']}")
        return result

    # ----- Power -----
    elif choice == "4":
        print("\nCalculate Power")
        print("a) Using P = V × I")
        print("b) Using P = I² × R")
        print("c) Using P = V² / R")
        power_choice = input("Choose a, b or c: ").strip().lower()

        if power_choice == "a":
            voltage = get_float("Enter voltage in Volts (V): ")
            current = get_float("Enter current in Amperes (I): ")
            power = voltage * current
            formula = "P = V × I"
            details = f"V = {voltage} V, I = {current} A"
        elif power_choice == "b":
            current = get_float("Enter current in Amperes (I): ")
            resistance = get_float("Enter resistance in Ohms (R): ")
            power = (current ** 2) * resistance
            formula = "P = I² × R"
            details = f"I = {current} A, R = {resistance} Ω"
        elif power_choice == "c":
            voltage = get_float("Enter voltage in Volts (V): ")
            resistance = get_float("Enter resistance in Ohms (R): ")
            if resistance == 0:
                print("Error: Resistance cannot be zero (division by zero).")
                return "invalid"
            power = (voltage ** 2) / resistance
            formula = "P = V² / R"
            details = f"V = {voltage} V, R = {resistance} Ω"
        else:
            print("Invalid power option.")
            return "invalid"

        result = {
            "type": "Power",
            "value": power,
            "unit": "W",
            "formula": formula,
            "details": details
        }
        print(f"\nPower = {power:.4f} W")
        print(f"Formula used: {result['formula']}")
        return result


def main():
    """Main program loop. Keeps running until the user chooses to quit."""
    print("=" * 50)
    print("   OHM'S LAW AND POWER CALCULATOR")
    print("   ND1 Mechatronics Engineering - YabaTech")
    print("=" * 50)

    history = []   # This list stores every successful calculation (the twist)

    while True:
        result = calculate()

        if result is None:          # User chose to quit
            break
        elif result == "invalid":   # Bad input – just ask again
            continue
        else:
            history.append(result)  # Save successful calculation

        # Ask if user wants to do another calculation
        again = input("\nDo another calculation? (y/n): ").strip().lower()
        if again != "y":
            break

    # ----- Session summary (the personal twist) -----
    print("\n" + "=" * 50)
    print("SESSION SUMMARY")
    print("=" * 50)

    if not history:
        print("No calculations were performed.")
    else:
        print(f"You performed {len(history)} calculation(s):\n")
        for i, calc in enumerate(history, 1):
            print(f"{i}. {calc['type']}: {calc['value']:.4f} {calc['unit']}")
            print(f"   Formula: {calc['formula']}")
            print(f"   Inputs:  {calc['details']}")
            print()

    print("Thank you for using the calculator. Goodbye!")
    print("=" * 50)


# Start the program
if __name__ == "__main__":
    main()