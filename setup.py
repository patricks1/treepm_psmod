#!/usr/bin/env python
from distutils.core import setup

__version__ = '0.1'

setup(name = 'wTreepm',
      version = __version__,
      description = 'Hacked, light-weight, Python3 version of Andrew Wetzels TreePM code. Originally hacked by ChangHoon Hahn. Further modified by Patrick Staudt.',
      author='Patrick Staudt',
      author_email='patrickstaudt1@gmail.com',
      url='',
      platforms=['*nix'],
      license='GPL',
      requires = ['numpy', 'scipy'],
      provides = ['treepm_psmod'],
      packages = ['treepm_psmod', 'treepm_psmod.utility']
      )
