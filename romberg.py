import numpy as np

def f(x):
   'Función que se desea integrar'
   f=1/x
   return f

def romberg(a, b, k, l):
   '''
   Esta función realiza integración numérica por medio del método de Romberg(extrapolación de Richardson)
   Inputs:
      a: limite inferior de integración
      b: limite superior de integración
      k: 1,2,3, n
      l: 1,2,..., k
   Output:
      r: valor de la integral 
   '''
   if l>k:
      print('Error, j es mayor a i')
      return 
   if l==0 or k==0:
      print('Error, i y j tienen que ser mayores a cero')
      return

   r=np.zeros((k,l)) #array donde se guardan los valores de rij
   sum=0
   for i in range(1,k+1):
      for j in range(1,l+1):
         if ( i==1 and j==1 ):   #Calcula R11
            h = (b-a)/i
            r[0,0] = h/2 *( f(a) + f(b) )

         elif ( i>=2 and j==1 ):   #Calcula Ri1
            for m in range(1,2**(i-2)+1): 
               sum=sum + f(a + (2*m-1)*h/2 ) #sumatoria 
            r[i-1,0] = 0.5 * ( r[i-2,0] + h*sum )
            h = (b-a)/i
            sum=0

         else: #Calcula Rij, i>=2 j>2
            r[i-1,j-1] = ( 4**(j-1)*r[i-1,j-2]-r[i-2,j-2] )/( 4**(j-1)-1 )

   return r[k-1,l-1]

print(romberg(1,3,3,3))