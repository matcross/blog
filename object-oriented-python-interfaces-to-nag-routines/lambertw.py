#!/usr/bin/env python
"""
An example Python interface to a NAG (Fortran) Library, using ctypes.
"""
class NagFunctionError(Exception):
    "A base NAG exception class."
    def __init__(self, function_name, code, message=None):
        "Here, message - if supplied - should be list."
        self.code = code
        self.function_name = function_name
        self.message = message

    def __str__(self):
        if (self.message is None):
            error_message = []
        else:
            error_message = self.message
        error_message.append('ABNORMAL EXIT, code ' + str(self.code) +
                             ', from NAG function ' + self.function_name + '.')
        return '\n** ' + '\n** '.join(error_message)

class NagLicenceError(NagFunctionError):
    "A NAG exception class for a missing licence."
    def __init__(self, function_name, code):
        super(self.__class__, self).__init__(function_name, code,
                                             ['Function call not licensed.'])

class NagTypeError(NagFunctionError):
    "A NAG exception class for an invalid argument instance."
    def __init__(self, function_name, msg):
        super(self.__class__, self).__init__(function_name, -199, msg)

class NagFunction(object):
    "A root NAG function class."
    from ctypes import c_int, Structure
    # The default error-handling mode for each (Fortran) Library call:
    ifail = c_int(1)

    class Complex(Structure):
        "A class to emulate a complex value using ctypes."
        from ctypes import c_double
        _fields_ = [("re", c_double), ("im", c_double)]

    def check_fortran_ifail(self):
        """
        Takes action based on the Fortran ifail value returned by a NAG Fortran
        Library call.
        """
        if (self.ifail.value == 0):
            return
        elif (self.ifail.value == -399):
            raise NagLicenceError(self.__class__.__name__, self.ifail.value)
        else:
            raise NagFunctionError(self.__class__.__name__, self.ifail.value)

    def check_type(self,
                   argument,
                   argument_name,
                   expected_type):
        "Verifies that argument is an instance of expected_type."
        if (isinstance(argument, expected_type)):
            return
        raise NagTypeError(self.__class__.__name__,
                           ['Invalid type ' + argument.__class__.__name__ +
                            ' for ' + argument_name + '.',
                            'Expected type ' + expected_type.__name__ + '.'])

class NagRootsLambertWComplex(NagFunction):
    "A NAG class for the complex Lambert W function, c05bb."
    def __init__(self, naglib_h):
        super(self.__class__, self).__init__()
        self.fcn_h = naglib_h.c05bbf_
        self.fcn_h.restype = None

    def evaluate(self, branch, offset, z):
        "The wrapper to the NAG Library call."
        from ctypes import byref, c_double, c_int
        self.check_type(branch, 'branch', int)
        self.check_type(offset, 'offset', bool)
        self.check_type(z, 'z', complex)
        branch_f = c_int(branch)
        if (offset):
            offset_f = c_int(1)
        else:
            offset_f = c_int(0)
        z_f = self.Complex(z.real, z.imag)
        w_f = self.Complex()
        resid_f = c_double()
        self.fcn_h(byref(branch_f),
                   byref(offset_f),
                   byref(z_f),
                   byref(w_f),
                   byref(resid_f),
                   byref(self.ifail))
        self.check_fortran_ifail()
        return complex(w_f.re, w_f.im), resid_f.value

def c_example():
    """
    Calls the Lambert W wrapper for a range of input values and prints the
    results.
    """
    def format_complex(z):
        "Formats a complex z for output as an (a, b) pair."
        return ''.join(['(',
                        format(z.real, '15.8e'),
                        ', ',
                        format(z.imag, '15.8e'),
                        ')'])

    from ctypes import cdll
    import sys
    naglib = '/path/to/libnag_nag.so'
    naglib_h = cdll.LoadLibrary(naglib)
    branch = 0
    offset = False
    sys.stdout.write('Lambert W function values for branch = ' + str(branch) +
                     ', offset = ' + str(offset) + ':\n')
    for z in [
            complex(0.5, -1.0),
            complex(1.0, 2.3),
            complex(4.5, -0.1),
            complex(6.0, 6.0)
    ]:
        w, resid = NagRootsLambertWComplex(naglib_h).evaluate(branch, offset, z)
        sys.stdout.write('z = ' + format_complex(z) +
                         ', W(z) = ' + format_complex(w) +
                         '. residual = ' + format(resid, '15.8e') + '\n')

if (__name__=='__main__'):
    c_example()
