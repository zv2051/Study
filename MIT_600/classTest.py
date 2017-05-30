class intSet(object):
    def __init__(self):
        self.vals = []

    def insert(self, e):
        if e not in self.vals:
            self.vals.append(e)

    def __str__(self):
        self.vals.sort()
        return ",".join(str(e) for e in self.vals)
    def member(self, e):
        if e in self.vals:
            return True
        else:
            return False

    def remove(self, e):
        if self.member(e):
            self.vals.remove(e)
            self.__str__()
