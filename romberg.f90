program main
   implicit none
   real::   romberg
   write(*,*) romberg(1.0,3.0,3,3)
end program main

real function f(x) !Función qu se desea integrar
   implicit none
   real:: x

   f=1/x
end function f

real function romberg(a, b, i, j)
!Esta función realiza integración numérica por medio del método de Romberg(extrapolación de Richardson)
!Inputs:
!   a: limite inferior de integración
!   b: limite superior de integración
!   i: 1,2,3, ... , n
!   j: 1,2,3, ... , i
!Output:
!   r: valor de la integral 
   implicit none
   real  :: f, a, b, sum, h
   integer  :: i, j, k, l, m
   real  :: r(i,j)


   if (j>i) then
      write(*,*) 'Error, j es mayor a i'
      return 
   end if

   if (i<=0 .or. j<=0) then
      write(*,*) 'Error, i y j tienen que ser mayores a cero'
      return
   end if

   sum=0 !se almacena el valor de la sumatoria
   do l=1,j !ciclo para movernos entre columnas
      do k=1,i !ciclo para movernos entre filas

         if ( k<l ) cycle !solamente calculamos los elementos de la matriz triangular

         if ( k==1 .and. l==1 ) then   !calcula r11
            h = (b-a)/k
            r(1,1) = h/2 *( f(a) + f(b) )

         else if ( k>=2 .and. l==1 ) then !calcula ri1
            do m=1, 2**(k-2)
               sum = sum + f(a + (2*m-1)*h/2 )
            end do
            r(k,1) =  0.5 * ( r(k-1,1) + h*sum )
            h = (b-a)/k
            sum=0

         else  !calcula rij, i>=2 j>2
            r(k,l) = ( 4**(l-1)*r(k,l-1)-r(k-1,l-1) )/( 4**(l-1)-1 )
         end if

      end do
   end do
   romberg=r(i,j)
end function romberg