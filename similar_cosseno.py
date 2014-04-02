import math
import numpy
import scipy
import pylab as py
from sympy import Matrix

def cos():
    print('teste ainda')
for i in py.frange (0,180,0.5):
        print('Angulo: %.2f' %i)
        print('Seno: ',numpy.sin(i))
        print('Cosseno: ',numpy.cos(i))
        print('Tangente: ',math.tan(i))
        print('--------------------------\n\n')

somatorio = lambda x,y,z :pow(x,y)/25+z**2
print(somatorio(10,2,4))