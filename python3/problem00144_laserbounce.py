import math

x, y = 0, 10.1
m = (-9.6-y)/(1.4-x)

def travel(x, y, m):
    '''
    intersection between `y = m * x + b` and `4*x**2 + y**2 = 100`
    '''
    b = y - m * x
    A, B, C = 4+m**2, 2*m*b, b**2-100
    LHS, RHS = -B/(2*A), math.sqrt(B**2-4*A*C)/(2*A)
    x = sorted([LHS-RHS, LHS+RHS], key=lambda v: abs(x-v))[1]
    y = m*x+b
    return x, y

def reflect(p, q):
    '''
    p is the angle of incidence
    q is the angle with horizontal at point of contact
    '''
    if abs(p+0.443) < 0.01:
        r = math.pi/2 + q
        s = p - r
        t = r - s
    else:
        r = math.pi - p - q
        s = math.pi/2 - r
        t = 2*s + r + q - math.pi
    return t

for _ in range(4):
    print("at ({:>6.2f}, {:>6.2f}) angled {:>8.3f}".format(x, y, math.degrees(math.atan(m))))
    x, y = travel(x, y, m)
    p = math.atan(m)
    q = math.atan(-4*x/y)
    m = math.tan(reflect(p, q))
