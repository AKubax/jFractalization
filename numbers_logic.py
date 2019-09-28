import decimal

decimal.setcontext(decimal.ExtendedContext)

#Utility:

def u_pi():
    decimal.getcontext().prec += 2  
    three = decimal.Decimal(3)      
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    decimal.getcontext().prec -= 2
    return +s               

def u_exp(x):
    x = decimal.Decimal(x)
    decimal.getcontext().prec += 2
    i, lasts, s, fact, num = 0, 0, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x
        s += num / fact
    decimal.getcontext().prec -= 2
    return +s

def u_cos(x):
    x = decimal.Decimal(x)
    decimal.getcontext().prec += 2
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    decimal.getcontext().prec -= 2
    return +s

def u_sin(x):
    x = decimal.Decimal(x)
    decimal.getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    decimal.getcontext().prec -= 2
    return +s

class cnumber:

    #decimal Re
    #decimal Im
    
    #bool nan
    #bool inf

    def __init__(self, real, imag = decimal.Decimal(0)):
        self.Re = decimal.Decimal(real)
        self.Im = decimal.Decimal(imag)

        self.nan = decimal.Decimal.is_nan(self.Re) or decimal.Decimal.is_nan(self.Im)
        self.inf = decimal.Decimal.is_infinite(self.Re) or decimal.Decimal.is_infinite(self.Im)

    def is_nan(self):
        return self.nan

    def is_inf(self):
        return self.inf

    def is_zero(self):
        return self.Re == 0 and self.Im == 0

    def __str__(self):
        if self.is_nan():  return 'NaN'
        if self.is_inf():  return 'Infinity'
        if self.is_zero(): return '0'
        
        re = ''
        sgn = ''
        im = ''
        
        if self.Re != decimal.Decimal(0):
            re = str(self.Re)
        if not (self.Re.is_zero() or self.Im.is_zero()):
            sgn = ' - '
            if self.Im > 0: sgn = ' + '
        if self.Im != decimal.Decimal(0):
            if abs(self.Im) != decimal.Decimal(1): im += str(abs(self.Im))
            im += 'i'
        
        return re + sgn + im

    def __repr__(self):
        return str(self)

    #operators:
    def __add__(self, z):
        if self.is_nan() or z.is_nan(): return cnumber.NaN
        if self.is_inf() or z.is_inf(): return cnumber.Infinity

        return cnumber(self.Re + z.Re, self.Im + z.Im)

    def __neg__(self):
        if self.is_nan(): return cnumber.NaN
        if self.is_inf(): return cnumber.NaN

        return cnumber(-self.Re, -self.Im)

    def __sub__(self, z):
        return self + (-z)

    def __mul__(self, z):
        if self.is_nan() or z.is_nan(): return cnumber.NaN
        if self.is_inf() or z.is_inf():
            if not (self.is_zero() or z.is_zero()): return cnumber.Infinity
            else: return cnumber.NaN

        return cnumber(self.Re * z.Re - self.Im * z.Im, self.Re * z.Im + self.Im * z.Re)

    def __truediv__(self, z):
        if self.is_nan() or z.is_nan(): return cnumber.NaN
        if z.is_inf():
            if not self.is_inf(): return cnumber(0)
            else: return cnumber.NaN
        if z.is_zero():
            if not self.is_zero(): return cnumber.Infinity
            else: return cnumber.NaN

        else: return cnumber( (self.Re * z.Re + self.Im * z.Im) / (z.Re * z.Re + z.Im * z.Im),
                             (self.Im * z.Re - self.Re * z.Im) / (z.Re * z.Re + z.Im * z.Im))

    def exp(z):
        return cnumber(u_cos(z.Im), u_sin(z.Im)) * cnumber(u_exp(z.Re))
        


cnumber.NaN = cnumber(decimal.Decimal('NaN'))
cnumber.Infinity = cnumber(decimal.Decimal('Infinity'))

        
        
        
        
        
