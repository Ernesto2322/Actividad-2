# command_line_calculator.py
import sys

class Calculator:
    def multiply_or_divide(self, multiplier, divisor):
        """
        Realiza una multiplicación si el divisor no es cero,
        de lo contrario realiza una división.

        :param multiplier: El número que se multiplicará o dividirá.
        :param divisor: El número que se usa para la multiplicación o división.
        :return: El resultado de la multiplicación o división.
        """
        if divisor != 0:
            return multiplier * divisor
        else:
            return multiplier / divisor

def main():
    if len(sys.argv) != 3:
        print("Uso: python command_line_calculator.py <multiplicador> <divisor>")
        sys.exit(1)

    try:
        multiplier = float(sys.argv[1])
        divisor = float(sys.argv[2])
    except ValueError:
        print("Por favor ingrese números válidos.")
        sys.exit(1)

    calc = Calculator()
    try:
        result = calc.multiply_or_divide(multiplier, divisor)
        print(f"El resultado es: {result}")
    except ZeroDivisionError:
        print("Error: División por cero.")

if __name__ == "__main__":
    main()
