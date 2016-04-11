
def OMonte(r, sigma, Tau, t, K, Spot, n):
    #Funcion para calcular los precios Put y Call de una opcion europea
    #usando simulaciones de Monte Carlo
    #r: tasa interes
    #sigma: Desviacion estandar
    #S0: Precio inicial

    #K: Precios strike
    #Tau: Tiempo para vencimiento
    #n: Numero de simulaciones 
    Zt=numpy.random.standard_normal((n,))
    St=Spot*numpy.exp((r-sigma**2/2)*(Tau-t) + sigma*numpy.sqrt(Tau-t)*Zt)
    
    CallEuropea=numpy.maximum(St-K,0)
    PutEuropea=numpy.maximum(K-St,0)
    montecarloCall=numpy.mean(CallEuropea)*numpy.exp(-r*(Tau-t))
    montecarloPut=numpy.mean(PutEuropea)*numpy.exp(-r*(Tau-t))
    
    op = dict(Call = montecarloCall, Put = montecarloPut)
    return op
   
def OIntegrate(r, sigma, Tau, t, K, Spot, n):
    #Funcion para calcular los precios Put y Call de una opcion europea
    #neutral al riesgo integrando
    #r: tasa interes
    #sigma: Desviacion estandar
    #S0: Precio inicial
    #K: Precios strike
    #Tau: Tiempo para vencimiento
    #n: Numero de simulaciones 
    a=numpy.log(K/Spot)
    b=(r-sigma**2/2)*(Tau-t) + numpy.sqrt(Tau-t)*sigma*6
    h = abs((b-a)/n)
    x = numpy.random.uniform(a,b,(n,))
    p=1/(sigma*numpy.sqrt(Tau-t)*numpy.sqrt(2*numpy.pi))*numpy.exp(-((x-(r-sigma**2/2)*(Tau-t))**2)/(2*sigma**2*(Tau-t)))
    St=Spot*numpy.exp(x)
    int=(St-K)*p
    int[int<0]=0
    montecarloCall=numpy.exp(-r*(Tau-t))*sum(int)*h
    
    b=numpy.log(K/Spot)
    a=(r-sigma**2/2)*(Tau-t) + numpy.sqrt(Tau-t)*-sigma*6 
    h = abs((b-a)/n)
    x = numpy.random.uniform(a,b,(n,))
    p=1/(sigma*numpy.sqrt(Tau-t)*numpy.sqrt(2*numpy.pi))*numpy.exp(-((x-(r-sigma**2/2)*(Tau-t))**2)/(2*sigma**2*(Tau-t)))  
    St=Spot*numpy.exp(x)
    int=(K-St)*p
    int[int<0]=0
    montecarloPut=numpy.exp(-r*(Tau-t))*sum(int)*h
    
    op = dict(Call = montecarloCall, Put = montecarloPut)
    return op


def OMonteAnti(r, sigma, Tau, t, K, Spot, n, nStep):
    #Funcion para calcular los precios Put y Call de una opcion Europea
    #usando simulaciones de Monte Carlo con variables antithetic y simulacion de caminos
    #S0: Precio inicial
    #K: Precios strike
    #Tau: Tiempo para vencimiento
    #n: Numero de simulaciones (nStep)
    #NbPas: numero de evaluaciones/caminos hasta Tau
    #Parametros iniciales
    DeltaT=Tau/nStep
    
    SPresent=Spot*numpy.ones((n*2))
    SNext=numpy.zeros((n*2))
    
    for i in range(1,nStep):
        temp = numpy.sqrt(DeltaT)*numpy.random.standard_normal((n,))
        dW = numpy.concatenate((temp, -temp))
        SNext = SPresent + (r)*SPresent*DeltaT + sigma*SPresent*dW
        SPresent = SNext
        
    #Calculacion de los precion
    montecarloCall = numpy.exp(-r*Tau)*numpy.mean(numpy.maximum(0,SPresent-K))
    montecarloPut = numpy.exp(-r*Tau)*numpy.mean(numpy.maximum(0,K-SPresent))
    
    op = dict(Call = montecarloCall, Put = montecarloPut)
    return op

