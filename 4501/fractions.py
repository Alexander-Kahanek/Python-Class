class Fraction:
    '''
    a representation of two integers, as opposed to decimals.

    input : integers
    '''

    def __init__(self, numerator, denominator):
        '''data'''
        # try:
        #     numerator/denominator
        # except ZeroDivisionError as err:
        #     print('the denominator of a fraction cannot equal 0.')
        #     raise err

        self.n = numerator
        self.d = denominator

        self.remainder = numerator - (denominator * (numerator // denominator))
        self.whole = numerator // denominator
        self.float = numerator / denominator

    def __str__(self):
        '''printing'''
        return f'{self.n}/{self.d} or {self.whole}({self.remainder}/{self.d})'

    def __add__(self, other):
        '''addition'''
        return Fraction((self.n*other.d) + (other.n*self.d), self.d*other.d)

    def __sub__(self, other):
        '''subtraction'''
        return Fraction((self.n*other.d) - (other.n*self.d), self.d*other.d)

    def __mul__(self, other):
        '''multiplication'''
        return Fraction(self.n*other.n, self.d*other.d)

    def __truediv__(self, other):
        '''division'''
        # if type(other) is Fraction:
        return Fraction(self.n*other.d, self.d*other.n)
        # elif type(other) is int:
        # return Fraction(self.d * other, self.n)


print()
#######################
# setup
f1, f2 = Fraction(1, 2), Fraction(1256, 23)

print(f'fraction 1 : f1 = {f1}')
print(f'fraction 2 : f2 = {f2}')
print(f'f1 = {f1.float}, f2 = {f2.float}')
print('----------------------------')
######################

# addition
print(f'f1 + f2 = {f1 + f2}')

# subtraction
print(f'f1 - f2 =  {f1 - f2}')

# multiplication
print(f'f1 * f2 =  {f1 * f2}')

# division
print(f'f1 / f2 =  {f1 / f2}')

# invertion
# print(f'1 / f1 = {1/f1}')

# divide by 0?
# intert?
# power?
# do docstrings really need more detail?
# floor division? //
# modulo? %
# simplify?

print()
