
def EulerMaruyama(r, sigma, Spot, Tau, nStep, R):
    dt = Tau/nStep
    dB = numpy.sqrt(dt) * numpy.random.standard_normal((nStep,))
    Dt = R * dt
    k = int(Tau/Dt)
    EM = numpy.zeros((k + 1))
    EM[0] = Spot
    for i in range(1,k+1):
        dBEM = sum(dB[((i - 1) * R + 1):(i * R + 1)])
        EM[i] = EM[i - 1] + r * EM[i - 1] * Dt + sigma * EM[i - 1] * dBEM
    return EM[len(EM)-1]
  
    
    


def Milstein(r, sigma, Spot, Tau, nStep, R):
    dt = Tau/nStep
    dB = numpy.sqrt(dt) * numpy.random.standard_normal((nStep,))    
    Dt = R * dt
    k = int(Tau/Dt)
    
    M = numpy.zeros((k + 1))
    M[0] = Spot
    for i in range(1,k + 1):
        dBEM = sum(dB[((i - 1) * R + 1):(i * R + 1)])
        M[i] = M[i - 1] + r * M[i - 1] * Dt + sigma * M[i - 1] * dBEM + 0.5 * sigma**2 * M[i - 1] * (dBEM**2 - Dt)
    return M[len(M)-1]

    