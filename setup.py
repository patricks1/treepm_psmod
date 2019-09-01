#!/usr/bin/env python
from distutils.core import setup

__version__ = '0.1'

setup(name = 'wTreepm3',
      version = __version__,
      description = 'Hacked, light-weight, Python3 version of Andrew Wetzels TreePM code. Originally hacked by ChangHoon Hahn. Converted to Python 3 by Patrick Staudt.',
      author='ChangHoon Hahn and Patrick Staudt',
      author_email='hahn.changhoon@gmail.com, patrickstaudt1@gmail.com',
      url='',
      platforms=['*nix'],
      license='GPL',
      requires = ['numpy', 'scipy'],
      provides = ['treepm3'],
      packages = ['treepm3', 'treepm3.utility']
      )
