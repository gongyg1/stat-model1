import os.path

curdir = os.path.abspath(os.path.dirname(__file__))

import sys
sys.path.insert(0, os.path.normpath(os.path.join(curdir,
                                        '..', '..', 'tools')))
from _build import cython, has_c_compiler
sys.path.pop(0)
del sys

import numpy as np
from numpy.distutils.system_info import get_info

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration('src', parent_package, top_path)
    # Tokyo Extension
    blas_info = get_info('blas_opt', 0)
    ext_kwds = {'include_dirs' : [np.get_include(), './'],
                'extra_info' : blas_info}

    if has_c_compiler():
        cython(['tokyo.pyx'], working_path = curdir)
        config.add_extension('tokyo', sources=['tokyo.c'],
                         **ext_kwds)
    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**(configuration(top_path='').todict()))
