class Bolos:
    def __init__(self, pins = []):
        self.pins = list(pins)
        self.score = 0

    def check_there_strike(self):
        if self.pins.count('X') == 0:
            return False
        return True
    
    def check_there_spare(self):
        if self.pins.count('/') == 0:
            return False
        return True
    
    def nulo(self):
        i = 0
        for char in self.pins:
            if char == '-':
                self.pins[i] = '0'
                i += 1
            else:
                i += 1

    def simple_pins(self):
        Bolos.nulo(self)
        if Bolos.check_there_strike(self) or Bolos.check_there_spare(self):
            return 'No es un calculo simple'
        for char in self.pins:
            self.score += int(char)
        return self.score

    def pins_with_spares(self):
        Bolos.nulo(self)
        if Bolos.check_there_strike(self):
            return 'Hay uno o mas strikes en esta jugada'
        i = 0
        for char in self.pins:
            if char == '/':
                self.score = (self.score + 10 + int(self.pins[i + 1]))
                i += 1
            else:
                """ if self.pins[i + 1] == '/':
                    i += 1
                    continue
                self.score += int(char) """
                i += 1
        return self.score


if __name__ == '__main__':
    tiradas1 = Bolos('5/5/5/5/5/5/5/5/5/5/5')
    print(tiradas1.pins_with_spares())