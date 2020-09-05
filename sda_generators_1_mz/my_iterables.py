class MyIterable:
    def __init__(self, amount):
        self.amount = amount
        self.created_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.created_value >= self.amount - 1:
            raise StopIteration
        self.created_value = self.created_value + 1
        return self.created_value
