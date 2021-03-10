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

