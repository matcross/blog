Interface
  Subroutine nag_e04vhf(start,objadd,objrow,prob,usrfun,a,g,xlow,xupp,xnames, &
    flow,fupp,fnames,x,xstate,xmul,f,fstate,fmul,ns,ninf,sinf,comm,user,error)
!   .. Implicit None Statement ..
    Implicit None
!   .. Scalar Arguments ..
    Type (nag_sparse_matrix), Target, Optional, Intent (In) :: a, g
    Type (nag_comm), Intent (Inout) :: comm
    Type (nag_error), Optional, Intent (Inout) :: error
    Type (nag_user), Target, Optional, Intent (Inout) :: user
    Real (Kind=wp), Optional, Intent (In) :: objadd
    Real (Kind=wp), Optional, Intent (Out) :: sinf
    Integer, Optional, Intent (Out) :: ninf
    Integer, Optional, Intent (Inout) :: ns
    Integer, Intent (Inout) :: objrow
    Integer, Optional, Intent (In) :: start
    Character (8), Optional, Intent (In) :: prob
!   .. Array Arguments ..
    Real (Kind=wp), Target, Optional, Intent (Inout) :: f(:), fmul(:), x(:)
    Real (Kind=wp), Intent (In) :: flow(:), fupp(:), xlow(:), xupp(:)
    Real (Kind=wp), Optional, Intent (Out) :: xmul(:)
    Integer, Target, Optional, Intent (Inout) :: fstate(:), xstate(:)
    Character (8), Target, Optional, Intent (In) :: fnames(:), xnames(:)
!   .. Interface Blocks ..
    Interface
      Subroutine usrfun(status,x,f,g,cuser,iuser,ruser)
!       .. Implicit None Statement ..
        Implicit None
!       .. Scalar Arguments ..
        Integer, Intent (Inout) :: status
!       .. Array Arguments ..
        Real (Kind=wp), Optional, Intent (Inout) :: f(:), g(:)
        Real (Kind=wp), Intent (Inout) :: ruser(*)
        Real (Kind=wp), Intent (In) :: x(:)
        Integer, Intent (Inout) :: iuser(*)
        Character (8), Intent (Inout) :: cuser(*)
      End Subroutine usrfun
    End Interface
  End Subroutine nag_e04vhf
End Interface
