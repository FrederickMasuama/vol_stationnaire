import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eig


#Paramètres physique de l'avion

m = 12000                      #masse en kg
mi = 2500                      #moment d'inertie autour de l'axe de tangage, en kg.m^2
s = 16.2                       #surface des ailes, en m^2
c = 1.5                        #corde moyenne, en m
rho = 1.225                    #densité de l'air, en kg:m^3
v0 = 60                         #vitesse de vol, en m/s

#Coefficients aérodynamiques

cxv = -0.03                   #variation de la traînée par rapport à la vitesser longitudinale (v)
czv = -0.4                    #variation de la portance verticale par rapport à v
cztetha = -5.5                #variation de la portance par rapport à l'angle d'attaque tétha (en général entre -4 et -6 pour avion classique)
czq = -12.5                   #influence du taux de tangage q sur la force verticale
cmtetha = -1.0                #variation du moment de tangage par rapport à tetha
cmq = -5.0                    #influence le taux de tangage q sur le moment de tangage

#Matrice A pour le modèle longiudinal
"""elle décrit comment les petites perturbations dans les variables d'état évoluent dans le temps"""
"""variables d'état : [v, tetha, q, alpha]"""

A = np.array([[cxv / m, 0, 0, -9.81],                                               #éq. de Newton selon x 
              [czv / (m*v0), cztetha / (m*v0), czq*c / (2*m*v0), 0],                #éq. de Newton selon z
              [0, cmtetha / mi, cmq*c / (2*mi), 0],                                 #éq.d'Euler
              [0, 0, 1, 0]])                                                        #cinématique

"""cette construction nous permet d'avoir le système x' = Ax """

#Calcul des valeurs propres du système
val_prop, vect_prop = eig(A)
print ("Valeurs propres du système: ", val_prop) 
