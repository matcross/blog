    Program str_read
!     .. Implicit None Statement ..
      Implicit None
!     .. Local Scalars ..
      Real (Kind=kind(0.0D0)) :: rval
      Integer :: ioerr
      Character (200) :: my_str
!     .. Intrinsic Procedures ..
      Intrinsic :: kind
!     .. Executable Statements ..
      my_str = '1.0D400'
      Read (my_str,'(E16.0)',Iostat=ioerr) rval
      Print *, 'ioerr = ', ioerr
      If (ioerr==0) Then
        Print *, 'rval = ', rval
      End If
    End Program str_read
