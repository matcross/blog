Interface
  Function nag_multi_normal_f90(tail,a,b,xmu,sig,tol,lwk,ifail)
!   .. Implicit None Statement ..
    Implicit None
!   .. Function Return Value ..
    Real (Kind=wp) :: nag_multi_normal_f90
!   .. Scalar Arguments ..
    Real (Kind=wp), Optional, Intent (In) :: tol
    Integer, Optional, Intent (Inout) :: ifail
    Integer, Optional, Intent (In) :: lwk
    Character (1), Intent (In) :: tail
!   .. Array Arguments ..
    Real (Kind=wp), Intent (In) :: a(:), b(:), sig(:,:), xmu(:)
  End Function nag_multi_normal_f90
End Interface
