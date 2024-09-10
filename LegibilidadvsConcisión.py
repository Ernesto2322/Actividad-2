class Calculator:
    def multiply_or_divide(self, multiplier, divisor):
        if divisor != 0:
            return multiplier * divisor
        else:
            return multiplier / divisor
