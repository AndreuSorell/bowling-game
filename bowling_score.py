class Bolos:
    def __init__(self, pins = []):
        self.pins = list(pins)
        self.score = 0
        self.previous_pin = 0
        self.next_pin = 1
        self.row = 20

    def check_there_strike(self):
        if self.pins.count('X') == 0:
            return False
        return True
    
    def check_there_spare(self):
        if self.pins.count('/') == 0:
            return False
        return True

    def spare(self): ##
        self.score += ((10 - int(self.pins[self.previous_pin])) + int(self.pins[self.next_pin]))

    def strike(self):
        if self.pins[self.next_pin] == 'X':
            if self.pins[self.next_pin+1] == 'X':
                self.score += 30
            else:
                self.score += (20 + int(self.pins[self.next_pin+1]))
        else:
            self.score += (10 + int(self.pins[self.next_pin]))
    
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

    def score_bolos(self):
        Bolos.nulo(self)
        i = 0
        while i < self.row:
            if self.pins[i] == '/':
                Bolos.spare(self)
                i += 1
                self.previous_pin = i-1
                self.next_pin = i+1
            elif self.pins[i] == 'X':
                Bolos.strike(self)
                i += 1
                self.previous_pin = i-1
                self.next_pin = i+1
                self.row -= 1
            else:
                self.score += int(self.pins[i])
                i += 1
                self.previous_pin = i-1
                self.next_pin = i+1

        return self.score


if __name__ == '__main__':
    tiradas1 = Bolos('8/549-XX5/53639/9/X')
    print(tiradas1.score_bolos())