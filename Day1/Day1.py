class Safe_Dial:
    def __init__(self):
        self.dial_numbers = [i for i in range(100)]
        self.dial_pointer = 50
        self.zero_counter = 0

    def rotate_left(self, amount):
        number_rotations = 0

        for i in range(amount):
            self.dial_pointer -= 1
            if self.dial_pointer == 0:
                number_rotations += 1
            if self.dial_pointer < 0:
                self.dial_pointer = 99
        
        self.zero_counter += number_rotations

        return self.dial_pointer, number_rotations
    
    def rotate_right(self, amount):
        number_rotations = 0

        for i in range(amount):
            self.dial_pointer += 1
            if self.dial_pointer > 99:
                self.dial_pointer = 0
                number_rotations += 1
        
        self.zero_counter += number_rotations

        return self.dial_pointer, number_rotations

safe_dial = Safe_Dial()

with open('input.txt', 'r') as input, open('output_default.txt', 'w') as output:
    for line in input:
        output.write(line.removesuffix("\n"))
        
        direction = line[0]
        amount = int(line[1:])

        if direction == "L":
            output.write(f"{safe_dial.rotate_left(amount)}\n")
        elif direction == "R":
            output.write(f"{safe_dial.rotate_right(amount)}\n")

    output.write(f"zero counter: {safe_dial.zero_counter}")
