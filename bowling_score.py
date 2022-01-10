class Bolos:
    def __init__(self, pins = ''):
        self.pins = pins
        self.score = 0

    def simple_pins(self):
        pins = list(self.pins)
        if pins.count('X') != 0:
            return 'No es un calculo simple'
        elif pins.count('/') != 0:
            return 'No es un calculo simple'
        for char in pins:
                if char == '-':
                    continue
                else:
                    self.score += int(char)
        return self.score


if __name__ == '__main__':
    tiradas1 = Bolos('12345123451234512345')
    print(tiradas1.simple_pins())