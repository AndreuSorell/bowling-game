class Bolos:
    def __init__(self, pins = []):
        self.pins = list(pins)
        self.score = 0

    def check_no_strike(self):
        if self.pins.count('X') == 0:
            return False
        return True
    
    def check_no_split(self):
        if self.pins.count('/') == 0:
            return False
        return True

    def simple_pins(self):
        if Bolos.check_no_strike(self) or Bolos.check_no_split(self):
            return 'No es un calculo simple'
        for char in self.pins:
                if char == '-':
                    continue
                else:
                    self.score += int(char)
        return self.score


if __name__ == '__main__':
    tiradas1 = Bolos('5/5/5/5/5/5/5/5/5/5/5')
    print(tiradas1.simple_pins())