class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit.lower()

    def inches(self):
        if self.unit == 'inches':
            return self.length
        elif self.unit == 'feet':
            return self.length * 12

    def feet(self):
        if self.unit == 'feet':
            return self.length
        elif self.unit == 'inches':
            return self.length / 12


c = Converter(9, 'inches')
print("c.feet = ", c.feet())

c2 = Converter(1, 'feet')
print("c2.feet = ", c2.feet())
