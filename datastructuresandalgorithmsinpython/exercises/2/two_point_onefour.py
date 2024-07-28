class Vector:
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        total = 0
        for i in range(len(self)):
            product = self[i] * other[i]
            total += product
        return total