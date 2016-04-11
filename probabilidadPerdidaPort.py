# -*- coding: utf-8 -*-
"""


@author: daniel
"""
import numpy as np


medias=.032,.31
TiempoFinal=100
comosicion=.5,.5
precioInicial=10,10
var=.0034,.0021
matrizcov=[[.0034,.000341],[.000341,.0021]]

pp=0
def ProbabilidadPerdida(pp,matrizcov,var,precioInicial,comosicion,TiempoFinal,medias):
    import numpy as np
    #funcion para calcular la probabilidad de que el valor caiga un porcentaje
    #pp. porcentaje que se quiere saber que pueda caer el portafolio
    #matrizcov. matriz de varianzas y covarianzas de los activos que conforman el port
    #var. vector de varianzas de los activos que conforman el port
    #precioInicial. precios iniciales de los activos que conforman el port
    #comosicion. composicion de los activos que conforman el port
    #TiempoFinal. Tiempo en el que se quiere saber cuando el portafolio caiga de pp
    #medias. medias de los activos que conforman el port
    n=10000
    l=0
    simulaciones=np.zeros([n,len(var)])
    Zt=np.random.random((n,len(var)))
    for i in range(1,len(var)):
        simulaciones[,i]=precioInicial[i]*np.exp((medias[i]-var[i]/2)*(TiempoFinal-0)+(np.sqrt(var[i]*(TiempoFinal-0))*Zt[,i]))
        
    valoractual<-np.sum(precioInicial*comosicion)
    composicioL=[[comosicion for i in range(5)] for j in range(5)]
    ValorPort=np.sum((composicioL.T*simulaciones),axis=1)
    t=(ValorPort-valoractual)/valoractual
    for i in range(1,len(t)):
        if t[i]<pp:
            l=l+1
        ProbabilidadPerdida=l/len(ValorPort)
    return(ProbabilidadPerdida)

