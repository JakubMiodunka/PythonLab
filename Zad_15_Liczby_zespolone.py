class Complex:
    def __init__(self, re: int, im: int) -> None:
        self.re = re
        self.im = im

    def __call__(self) -> str:
        return f"{self.re} + ({self.im})j"

    def __add__(self, other: object) -> object:
        re = self.re + other.re
        im = self.im + other.im
        return Complex(re, im)
    
    def __sub__(self, other: object) -> object:
        re = self.re - other.re
        im = self.im - other.im
        return Complex(re, im)

    def __mul__(self, other: object) -> object:
        re = (self.re * other.re - self.im * other.im)
        im = (self.re * other.im + self.im * other.re)
        return Complex(re, im)

    def __truediv__(self, other: object) -> object:
        re = (self.re * other.re + self.im * other.im) / (other.re ** 2 + other.im ** 2)
        im = (self.im * other.re - self.re * other.im) / (other.re ** 2 + other.im ** 2)
        return Complex(re, im)