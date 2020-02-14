import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

build_exe

executables = [
    Executable('ipgui.py', base=base)
]

setup(name='IP GUI',
      version='1.0',
      description='App pings ECMHSP centers',
      executables=executables
      )
