
# windows
from distutils.core import setup, Extension
import os

# check for windows vs linux/osx
if os.name != "nt":
    LargeVis = Extension('LargeVis',
                    sources = ['LargeVis.cpp', 'LargeVismodule.cpp'],
                    depends=['LargeVis.h'],
                    include_dirs = ['/usr/local/include'],
                    library_dirs = ['/usr/local/lib'],
                    libraries=['gsl', 'gslcblas'],
                    extra_compile_args=['-lm -pthread -lgsl -lgslcblas -Ofast -march=native -ffast-math'])
else:
    LargeVis = Extension('LargeVis',
                        sources = ['largevis_src/LargeVis.cpp', 'largevis_src/LargeVismodule.cpp'],
                        depends=['LargeVis.h'],
                        include_dirs = [os.environ['BOOST_HOME'], 'annoy/src'],
                        library_dirs = [os.environ['BOOST_HOME']],
                        extra_compile_args=['/Ox'])

setup (name = 'LargeVis',
       version = '1.0',
       description = 'LargeVis',
       ext_modules = [LargeVis])
