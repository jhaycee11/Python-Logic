import os
import sys

from cx_Freeze import setup, Executable

'''how to run
1. Setting up the directory of tcl and tk you are using
2. Setting up the filename and location of your code
3. run python setup.py build
4. run python setup.py bdist_msi
5. locate the installer inside dist folder
'''


####### Setup Here ########
python_tcl_loc = r'C:\Python310\tcl'
python_file_name = 'hashlib_pass.py'
program_name = ''
ver = ''

###########################


os.environ['TCL_LIBRARY'] = python_tcl_loc + '\\tcl8.6'
os.environ['TK_LIBRARY'] = python_tcl_loc + '\\tk8.6'

build_exe_options = {}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'


directory_table = [
    (
        'ProgramMenuFolder',
        'TARGETDIR',
        '.',
    ),
    (
        'CalMyProgramMenu',
        'ProgramMenuFolder',
        program_name,
    )
]

msi_data = {
    'Directory' : directory_table,
}

setup(
    name = program_name,
    version = ver,
    description = 'My Calculator',
    options = {'build_exe' : build_exe_options,
                'bdist_msi' : {'data' : msi_data}
    },
    executables = [
        Executable(
            python_file_name,
            base=base,
            shortcutName = program_name,
            shortcutDir = 'CalMyProgramMenu',
        )
    ]
)

