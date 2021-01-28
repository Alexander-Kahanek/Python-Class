class Fraction:
    '''
    a representation of two integers, as opposed to decimals.

    input : integers
    '''

    def __init__(self, numerator, denominator):
        '''data'''
        try:
            numerator/denominator
        except ZeroDivisionError as err:
            print('ERROR: the denominator of a fraction cannot equal 0.')
            raise err

        if type(numerator) is not int or type(denominator) is not int:
            print('values are not integers.')
            raise TypeError

        self.n = numerator
        self.d = denominator

        self.remainder = numerator - (denominator * (numerator // denominator))
        self.whole = numerator // denominator
        self.float = numerator / denominator

    def __str__(self):
        '''printing'''
        return f'{self.n}/{self.d}'

    def reduce(self):
        '''reduce to a + remainder'''
        return f'{self} reduces to  {self.whole} + ({self.remainder}/{self.d})'

    def simplify(self):
        # how to simplify a fraction: n/d
        # check all numbers in [d, .., i, .., 1]
        # if n % i and d % i
        # then i is common factor
        # else no common factors -- simplified
        for i in [self.d-k if self.d < 100 else k+1 for k in range(self.d)]:
            if self.n % i == 0 and self.d % i == 0:
                if i != 1:
                    # no need for recursively simplify
                    # with greatest common factor
                    return Fraction(self.n//i, self.d//i).simplify()
                else:
                    # gcd is 1 and cannot be simplified
                    return Fraction(self.n, self.d)

        return Fraction((self.whole*self.d) + self.remainder, self.d)

    def invert(self):
        '''flips fraction from a/b to b/a'''
        return Fraction(self.d, self.n)

    def __add__(self, other):
        '''addition + '''
        return Fraction((self.n*other.d) + (other.n*self.d), self.d*other.d)

    def __sub__(self, other):
        '''subtraction - '''
        return Fraction((self.n*other.d) - (other.n*self.d), self.d*other.d)

    def __mul__(self, other):
        '''multiplication * '''
        return Fraction(self.n*other.n, self.d*other.d)

    def __truediv__(self, other):
        '''division / '''
        return Fraction(self.n*other.d, self.d*other.n)

    def __mod__(self, other):
        '''modulo % '''
        return self - other * (self // other)

    def __floordiv__(self, other):
        '''floor division // '''
        return Fraction((self/other).whole, 1)

    def __pow__(self, other):
        '''exponentiation ** '''
        a, b = ((self.n**other.n)**(1/other.d)).as_integer_ratio()
        c, d = ((self.d**other.n)**(1/other.d)).as_integer_ratio()
        print(a, b, c, d)
        return Fraction(a*d, c*b).simplify()
