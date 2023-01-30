program main
   implicit none
   real::   romberg
   write(*,*) romberg(1.0,3.0,3,3)
end program main

real function f(x)
   implicit none
   real:: x

   f=1/x
end function f

real function romberg(a, b, i, j)
   implicit none
   real  :: f, a, b, sum, h
   integer  :: i, j, k, l, m
   real  :: r(i,j)

   
   sum=0
   do k=1,i
      do l=1,k
         if ( k==1 .and. l==1 ) then
            h = (b-a)/k
            r(1,1) = h/2 *( f(a) + f(b) )

         else if ( k>=2 .and. l==1 ) then
            do m=1, 2**(i-2)
               sum = sum + f(a + (2*m-1)*h/2 )
            end do
            r(k,1) =  0.5 * ( r(k-1,1) + h*sum )
            h = (b-a)/k
            sum=0
         else
            r(k,l) = ( 4**(l-1)*r(k,l-1)-r(k-1,l-1) )/( 4**(l-1)-1 )
         end if

      end do
   end do
   romberg=r(i,j)
end function romberg