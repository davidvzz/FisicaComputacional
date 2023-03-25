import numpy as np
from matplotlib import pylab as plt

#Parámetros (definir arbitrariamnete junto con unidad de tiempo)
pi=10    #birth rate
alpha=3.2e-3 #total destruction rate of a Zombie
beta=2.95e-3  #rate of becoming a Zombie after contact with a Zombie 
delta=1e-3 #natural mortality rate
Zeta=8e-2  #Resurrection rate into Zombie after death


#ED Individuos
def fS(t,S,Z,R):
    return pi-beta*S*Z-delta*S

#ED Zombies
def fZ(t,S,Z,R):
    return beta*S*Z+Zeta*R-alpha*Z*S

#ED Removed individuals
def fR(t,S,Z,R):
    return delta*S+alpha*Z*S-Zeta*R

#Resolver ED mediante método de Euler mejorado
def predictor(f,h,t=0,S=0,Z=0,R=0):
    'Método de Euler Simple'
    return S+Z+R+f*h

def corrector(f,fc,h,t=0,S=0,Z=0,R=0):
    'Método de Euler Mejorado'
    return S+Z+R+0.5*( f + fc )*h

#Condiciones iniciales(arbitrarias)
t_0=0
S_0=1000
Z_0=0
R_0=0

#Rango: 
h=0.01
t_f=30
n=int(abs(t_f-t_0)/h)

#Inicializar variables
t=np.zeros(n+1)
S=np.zeros(n+1)
Z=np.zeros(n+1)
R=np.zeros(n+1)
t[0]=t_0
S[0]=S_0
Z[0]=Z_0
R[0]=R_0
n_iter=15

for i in range(n):
    f1_tSZR=fS( t[i],S[i],Z[i],R[i] )
    f2_tSZR=fZ( t[i],S[i],Z[i],R[i] )
    f3_tSZR=fR( t[i],S[i],Z[i],R[i] )
    
    euler1=predictor( f1_tSZR, h, S=S[i] )
    euler2=predictor( f2_tSZR, h, Z=Z[i] )
    euler3=predictor( f2_tSZR, h, R=R[i] )

    S_old=S[i]
    Z_old=Z[i]
    R_old=R[i]
    t[i+1]=t[i]+h

    f1c=fS( t[i], euler1, Z[i], R[i] )
    f2c=fZ( t[i], S[i], euler2, R[i] )
    f3c=fR( t[i], S[i], Z[i], euler3 )

    for j in range(n_iter):
        S[i+1]=corrector( f1_tSZR, f1c, h, S=S_old )
        Z[i+1]=corrector( f2_tSZR, f2c, h, Z=Z_old )
        R[i+1]=corrector( f3_tSZR, f3c, h, R=R_old )
        f1c=fS( t[i+1], S[i+1], Z[i], R[i] )
        f2c=fZ( t[i+1], S[i], Z[i+1], R[i] )
        f3c=fR( t[i+1], S[i], Z[i], R[i+1] )

plt.grid()
plt.plot(t,S,label='Susceptible',color="blue")
plt.plot(t,Z,label='Zombies',color="green")
plt.plot(t,R,label='Removed',color="gray")
plt.xlabel("Tiempo")
plt.ylabel("Individuos")
plt.legend()


plt.show()


