from pandas.io.data import DataReader
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

#"act1 = DataReader("GENTERA.MX",  "yahoo", datetime(2015,1,1), datetime(2016,1,1))
#"act1=np.log(act1["Adj Close"])
#"act2 = DataReader("GFNORTEO.MX",  "yahoo", datetime(2015,1,1), datetime(2016,1,1))
#"act2=np.log(act2["Adj Close"])
#"act3 = DataReader("GFREGIOO.MX",  "yahoo", datetime(2015,1,1), datetime(2016,1,1))
#"act3=np.log(act3["Adj Close"])
#"act4 = DataReader("GRUMAB.MX",  "yahoo", datetime(2015,1,1), datetime(2016,1,1))
#"act4=np.log(act4["Adj Close"])
#"act5 = DataReader("GSANBORB-1.MX",  "yahoo", datetime(2015,1,1), datetime(2016,1,1))
#"act5=np.log(act5["Adj Close"])

#"activos=act1,act2,act3,act4,act5
#"activos=np.diff(activos,axis=1)
#"mean=np.mean(activos,axis=1)
#"cov=np.cov(activos)
mean=0.0002456,0.00023456
cov=[[0.000032,0.0000158619040471187],[0.0000158619040471187,0.00003145]]

def portafolios(mean,cov,numerPorta):
    #generador de posibles portafolios. entrega las medias y las varianzas de los posibles portafolios
    #vector de las medias de los activos del portafolio de sus ren ln
    #matriz de varianzas y covarianzas de los rendimentos ln del portafolio
    #numero de portafolios que se desea generar
    numerPorta=10000
    Zt=np.random.uniform(size=(numerPorta,2))
    l=np.sum(Zt,axis=1)
    for i in range(1,numerPorta):
        Zt[i,]=Zt[i,]/l[i]        
    Zt=np.asmatrix(Zt)
    mean=np.asmatrix(mean)
    cov=np.asmatrix(cov)
    portmean=Zt*mean.T
    portvar=np.diag(np.sqrt(Zt*cov*Zt.T))
    x,y=portvar,portmean
    return(x,y)

ll = plt.plot(x,y,'bo')
plt.axis([0.0045, .006, 0.00023, .00025])
plt.xlabel('Desviación')
plt.ylabel('Rendimiento')
plt.title('Nuve de portafolios')
plt.show()

