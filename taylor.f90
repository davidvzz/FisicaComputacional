program main
   implicit none
   real  :: e,factorial,senh
   write(*,*) senh(5.0,10)
end program main

real function factorial(n)
   integer  :: n
   
   factorial=gamma(n+1.0)
   
end function factorial

real function e(x,n)
   real  :: x,factorial
   integer  :: n
   e=0
   do i=0,n
      e=e+x**i/factorial(i)
   end do
   return
end function e

real function senh(x,n)
   real  :: x, factorial
   integer  :: n
   senh=0
   do i=0,n
      senh=senh+x**(2*i+1)/factorial(2*i+1)
   end do
   return
end function senh

real function cosh(x,n)
   real  :: x,factorial
   integer  :: n
   cosh=0
   do i=0, n
      cosh=cosh+x**(2*i)/factorial(2*i)
   end do
end function cosh
