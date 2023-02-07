import math
def f(x,y):
   f=math.log(x+2*y)
   return f

def trapecio_doble(a,b,c,d,n,m):
   '''
   Esta función realiza doble integración numérica a una función de dos variables
   Inputs:
      a,b: limites de integración de x
      c,d: limities de integración de y
      n: particiones de la región en x
      m: particiones de la región en y
   '''
   sumx=0
   sumy=0
   hx=(b-a)/n
   hy=(d-c)/m
   for i in range(0,n+1): #ciclo de x
      for j in range(1,m): #ciclo de y
            sumy=sumy+f(a+i*hx,c+j*hy)
            integral=hy/2*( f(a) )
         print(j*hy)

      sumy=0
return