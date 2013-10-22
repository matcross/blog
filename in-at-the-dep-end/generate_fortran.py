#!/usr/bin/env python
"""
Generates the Fortran source for the dependency analysis discussed at
http://matcross.wordpress.com/2012/10/30/in-at-the-dep-end/.
"""

NFILES = 10

for i in range(NFILES):

    with open('module' + str(i) + '.f90', 'w') as file_fo:
        file_fo.writelines(['Module module' + str(i) + '\n',
                            'Contains\n',
                            '  Subroutine msub' + str(i) + '\n'])

        if (i in [0, NFILES - 1]):
            file_fo.write('    Print *, "OK' + str(i) + '"\n')
        else:

            if (i > NFILES / 2):
                m_no = i + 1
            else:
                m_no = i - 1

            file_fo.writelines(['    Use module' + str(m_no) + '\n',
                                '    Call msub' + str(m_no) + '\n'])

        file_fo.writelines(['  End Subroutine\n',
                            'End Module\n'])

with open('main.f90', 'w') as file_fo:
    file_fo.writelines(['Program main\n',
                        '  Use module' + str(NFILES / 2 + 1) + '\n',
                        '  Use module' + str(NFILES / 2) + '\n',
                        '  Call msub' + str(NFILES / 2 + 1) + '\n',
                        '  Call msub' + str(NFILES / 2) + '\n',
                        'End Program\n'])
