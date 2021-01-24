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
            print('the denominator of a fraction cannot equal 0.')
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
        for i in [self.d-k for k in range(self.d)]:
            if self.n % i == 0 and self.d % i == 0:
                if i != 1:
                    # recursively simplify
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
        ###########
        # maybe not correct?
        ##########
        return Fraction((self/other).remainder, (self/other).d)

    def __floordiv__(self, other):
        '''floor division // '''
        return (self/other).whole


print()

#######################
print('--- setup -----------------')

try:
    print(f'attempt with 0 in denominator...')
    Fraction(17, 0)
except:
    print()
    pass

f1, f2 = Fraction(1, 2), Fraction(6, 4)
print(f'fraction 1 : f1 = {f1}')
print(f'fraction 2 : f2 = {f2}')

######################
print('--- math -------------------')

# addition
print(f'{f1} + {f2} = {f1 + f2}')
# subtraction
print(f'{f1} - {f2} =  {f1 - f2}')
# multiplication
print(f'{f1} * {f2} =  {f1 * f2}')
# division
print(f'{f1} / {f2} =  {f1 / f2}')

# floor division
print(f'{f2} // {f1} = {f2 // f1}')
# modulo
print(
    f'FIX? {Fraction(7,2)} % {Fraction(2,1)} = {Fraction(7,2) % Fraction(2,1)}')

#####################
print('--- simplifying ------------')

print(f'{f1} = {f1.simplify()}')
print(f'{f2} = {f2.simplify()}')

print(f'21/48 = {Fraction(21,48).simplify()}')
print(f'0/13 = {Fraction(0,10).simplify()}')

####################
print('--- other things -----------')

print(f'convert to float ... {f1} = {f1.float}, {f2} = {f2.float}')
print(f'inverting a fraction ... {f1} inverts to {f1.invert()}')

####################
print()
