

def Trapecio(f,a,b,n):
    h = abs((b-a)/n)
    i = numpy.arange(n+1)
    x = a + (i*h)
    sumatrapecios = 2*f(x)
    sumatrapecios = sum(sumatrapecios)*(h/2)
    return sumatrapecios

def Simpson(f, a, b, n):
    h = abs((b-a)/n)
    x1 = numpy.concatenate(([a], [b]))
    x2 = numpy.arange(a+h,b-h,2*h)
    x3 = numpy.arange(a+(2*h),b-(2*h),2*h)
    y1 = f(x1)
    y2 = f(x2)
    y3 = f(x3)
    sumasimpson = (sum(y1) + 4*sum(y2) + 2*sum(y3)) * (h/3)
    return sumasimpson

def MonteCarlo(f, a, b, n):
    x = a + numpy.random.random((n,))*(b-a)
    sumamontecarlo = f(x)
    sumamontecarlo = sum(sumamontecarlo)*(b-a)/(n-1)
    return sumamontecarlo


def MonteCarlo2grado(f, ax, bx, ay, by, n):
    hx = abs((bx-ax)/n)
    hy = abs((by-ay)/n)
    x = ax + numpy.random.random((n,))*(bx-ax)
    y = ay + numpy.random.random((n,))*(by-ay)  
    sumamontecarlo = f(x,y)
    sumamontecarlo = sum(sumamontecarlo)*hx*hy*n
    return sumamontecarlo

