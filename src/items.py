class Item:
    def __init__(self, name, attribute, attribute_value, slot):
        self.name = name
        self.attribute = attribute
        self.attribute_value = attribute_value
        self.slot = slot

    def __str__(self):
        return f'Slot: {self.slot}\nStats: + {str(self.attribute_value)} {self.attribute}'
