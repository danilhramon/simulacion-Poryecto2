# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 19:31:51 2016

@author: Daniel
"""

#NÚMEROS ALEATORIOS CORRELACIONADOS

def aleatoriosCorelacionados(Sigmas,NumeroAleatorios):
    #calculo de alatoreos correlacionados por el metodo de cholesky
    #sigmas. matriz de varianzas y covarianzas para generar con las correlaciones que tienen
    #estos datos los numeros aleatorios
    #NumeroAleatorios. cantidad de numeros aleatorios correlacionados que se desean generar
    #por cada columna del vector
    import numpy
    x=numpy.random.uniform(size=(NumeroAleatorios,2)*numpy.linalg.cholesky(Sigmas)
    return(x)
