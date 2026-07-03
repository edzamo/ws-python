# Este script agrega el directorio 'extra' a la ruta de Python para poder importar módulos desde allí.
# Luego, importa funciones de cuatro módulos diferentes (sigma, alpha, iota, beta)
# y finalmente imprime el resultado de cada función en la consola.


#from sys import path
 
#path.append('..∖∖extra')
 
import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import FunI
from extra.good.beta import FunB
 
print(sig.FunS())
print(alp.FunA())
print(FunI())
print(FunB())
