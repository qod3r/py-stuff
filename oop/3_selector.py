class Selector:
    def __init__(self, l):
        self.l = l

    def get_odds(self):
        return [*(filter(lambda x: x % 2, self.l))]

    def get_evens(self):
        return [*(filter(lambda x: not x % 2, self.l))]


s = Selector([1, 2, 3, 4, 5, 6])
print(s.get_odds())
print(s.get_evens())