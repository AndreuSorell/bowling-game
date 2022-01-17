class Bowling:
    def __init__(self, pins = []):
        self.pins = list(pins)
        self.score = 0
        self.previous_pin = 0
        self.next_pin = 1
        self.last_frame = 20

    def spare(self):
        if self.pins[self.next_pin] == 'X':
            self.score += ((10 - int(self.pins[self.previous_pin])) + 10)
        else:
            self.score += ((10 - int(self.pins[self.previous_pin])) + int(self.pins[self.next_pin]))

    def strike(self):
        if self.pins[self.next_pin] == 'X':
            if self.pins[self.next_pin+1] == 'X':
                self.score += 30
            else:
                self.score += (20 + int(self.pins[self.next_pin+1]))
        else:
            if self.pins[self.next_pin+1] == '/':
                self.score += 20
            else:
                self.score += (10 + int(self.pins[self.next_pin]) + int(self.pins[self.next_pin+1]))
    
    def nulo(self):
        i = 0
        for char in self.pins:
            if char == '-':
                self.pins[i] = '0'
                i += 1
            else:
                i += 1

    def punctuation(self):
        Bowling.nulo(self)
        i = 0
        while i < self.last_frame:
            if self.pins[i] == '/':
                Bowling.spare(self)
                i += 1
                self.previous_pin = i-1
                self.next_pin = i+1
            elif self.pins[i] == 'X':
                Bowling.strike(self)
                i += 1
                self.previous_pin = i-1
                self.next_pin = i+1
                self.last_frame -= 1
            else:
                self.score += int(self.pins[i])
                i += 1
                self.previous_pin = i-1
                self.next_pin = i+1

        return self.score


if __name__ == '__main__':
    tiradas1 = Bowling('8/X9-XX5/53639/9/-')
    print(tiradas1.punctuation())