from abc import ABC, abstractmethod

class Geometriya(ABC):
    @abstractmethod
    def maydon(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Kvadrat(Geometriya):
    def __init__(self, tomon):
        self.tomoni = tomon

    def maydon(self):
        return self.tomoni ** 2

    def perimeter(self):
        return 4 * self.tomoni

class OltiBurchak(Geometriya):
    def __init__(self, tomon, yuz):
        self.tomoni = tomon
        self.yuzi = yuz

    def maydon(self):
        return (self.tomoni ** 2) * self.yuzi / 4

    def perimeter(self):
        return 5 * self.tomoni

kvadrat = Kvadrat(5)
olti_burchak = OltiBurchak(4, 5)

print(f"Kvadratning maydoni: {kvadrat.maydon()}")
print(f"Kvadratning perimetri: {kvadrat.perimeter()}")

print(f"Olti burchakning maydoni: {olti_burchak.maydon()}")
print(f"Olti burchakning perimetri: {olti_burchak.perimeter()}")
