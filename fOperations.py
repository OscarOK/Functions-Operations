####################################################################################################################
# El siguiente codigo calcula la integral de una funcion f(x) en un intervalo [a,b], es necesario                  #
# definir el numero de rectangulos para la suma de Riemman, conforme n sea mayor la suma converge a la integral    #
#                                                                                                                  #
# La funcion f define la funcion matematica a integrar (en este caso x^2)                                          #
# La funcion integrate recibe tres parametros: a (cota inferior de integracion), b (cota superior de integracion)  #
# y n (numero de rectangulos para la suma de Riemann                                                               #
#####################################################################################################################

import sympy as sy #MAKING FUNCTIONS INPUT EASIER
from math import acos, degrees #FOR fAngle FUNCTION

def f(formula, **kwargs): #EVALUATE kwargs AS FORM ARGUMENTS
    expr = sy.sympify(formula)
    return expr.evalf(subs = kwargs)

def integrate(a,b,n,formula): #INTEGRATE USING RIEMANN SUMS FROM a TO b, n TIMES
    dx = float(b-a)/float(n)
    aux = a
    integral = 0
    for i in range(0,n+1,1):
        integral = integral + f(formula, x = aux)*dx
        aux = aux+dx
    return integral

def fInnerProduct(a, b, n, fOne, fTwo): #CALCULATE INNER PRODUCT FROM TO FUNCTIONS
    f = fOne + '*' + fTwo #MERGE fOne & fTwo INTO fOne*fTwo
    return integrate(a,b,n,f) #CALLS INTEGRATE FUNCTION

def fNorm(a, b, n, f): #CALCULATE THE NORM OF A FUNCTION
    return fInnerProduct(a, b, n, f, f)**0.5 #THE NORM IS sqrt(<f,f>)

def fAngle(a, b, n, fOne, fTwo):
    innerProduct = fInnerProduct(a, b, n, fOne, fTwo)
    norms = fNorm(a, b, n, fOne) * fNorm(a, b, n, fTwo)

    if norms != 0:#INCASE WE HAVE A FUNCTION EQUAL 0
        return degrees(acos(innerProduct/norms))
    else:
        return
