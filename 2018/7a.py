"""
This one didn't work out!  See 7a_2nd_try.py for a working solution.
"""


class Level:
    def __init__(self, name):
        self.prev = None
        self.next = None
        self.letters = []

    def search_together(self, name):
        return name in self.letters

    def search_before(self, name):
        if self.prev:
            if self.prev.search_together(name):
                return True
            return self.prev.search_before(name)
        else:
            return False

    def search_after(self, name):
        if self.next:
            if self.next.search_together(name):
                return True
            return self.next.search_after(name)
        else:
            return False


class Leveller:
    def __init__(self):
        self.start_level = Level()
        # {name: Node object in the tree}
        self.d = {}

    def add(self, antacedent, consequent):
        self.levels.append()


t = Tree()
with open("7.txt") as f:
    for l in f:
        antacedent = l[5]
        consequent = l[36]
