# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 08:51:19 2021

@author: misael
Programa 7: paquetes y módulos
"""
import math
print(math.pi)
from math import pi
print(pi)
import math as mate
print(mate.pi)

import matplotlib.pyplot as plt
cooperacion = [20, 10, 25, 30]
nombres = ["Hugo", "Paco", "Luis", "Donald"]
plt.pie(cooperacion, labels = nombres)
plt.show()
#
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y = x*np.cos(x)
#Plotter
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Uso de modulo matplotlib y numpy')
plt.show()