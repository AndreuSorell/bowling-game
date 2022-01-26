from traceback import print_stack


class Bowling:
    def __init__(self, pins = []):
        self.pins = list(pins)
        self.score = 0
        self.previous_pin = 0
        self.next_pin = 1
        self.last_row = 20

    def spare(self):
        TEN = 10
        if self.pins[self.next_pin] == 'X':
            self.score += ((TEN - int(self.pins[self.previous_pin])) + TEN)
        else:
            self.score += ((TEN - int(self.pins[self.previous_pin])) + int(self.pins[self.next_pin]))

    def strike(self):
        ONE_PIN = 1
        if self.pins[self.next_pin] == 'X':
            if self.pins[self.next_pin+1] == 'X':
                self.score += 30
            else:
                self.score += (20 + int(self.pins[self.next_pin + ONE_PIN]))
        else:
            if self.pins[self.next_pin+1] == '/':
                self.score += 20
            else:
                self.score += (10 + int(self.pins[self.next_pin]) + int(self.pins[self.next_pin+ ONE_PIN]))
        
    def null_to_zero(self):
        self.pins = list(map(lambda pin: '0' if pin == '-' else pin, self.pins))

    def punctuation(self):
        Bowling.null_to_zero(self)
        i = 0
        while i < self.last_row:
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
                self.last_row -= 1
            else:
                self.score += int(self.pins[i])
                i += 1
                self.previous_pin = i-1
                self.next_pin = i+1

        return self.score


if __name__ == '__main__':
    tiradas1 = Bowling('8/X9-XX5/53639/9/-')
    print(tiradas1.punctuation())