# interactive_calculator.py

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

    def run_interactive(self):
        """
        Permite al usuario ingresar valores por teclado y muestra el resultado
        de la multiplicación o división.
        """
        try:
            multiplier = float(input("Ingrese el primer número (multiplicador): "))
            divisor = float(input("Ingrese el segundo número (divisor): "))
            result = self.multiply_or_divide(multiplier, divisor)
            print(f"El resultado es: {result}")
        except ValueError:
            print("Por favor ingrese números válidos.")
        except ZeroDivisionError:
            print("Error: División por cero.")

if __name__ == "__main__":
    calc = Calculator()
    calc.run_interactive()
