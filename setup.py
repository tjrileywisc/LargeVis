
# windows
from distutils.core import setup, Extension
import os

# check for windows vs linux/osx
if os.name != "nt":
    LargeVis = Extension('LargeVis',
                    sources = ['largevis_src/LargeVis.cpp', 'largevis_src/LargeVismodule.cpp'],
                    depends=['largevis_src/LargeVis.h', 'annoy/src/annoylib.h'],
                    include_dirs = ['/usr/local/include'],
                    library_dirs = ['/usr/local/lib'],
                    extra_compile_args=['-std=c++11', '-lm', '-Ofast', '-march=native', '-ffast-math', '-pthread'])
else:
    LargeVis = Extension('LargeVis',
                        sources = ['largevis_src/LargeVis.cpp', 'largevis_src/LargeVismodule.cpp'],
                        depends=['largevis_src/LargeVis.h', 'annoy/src/annoylib.h'],
                        extra_compile_args=['/Ox'])

setup (name = 'LargeVis',
       version = '1.0',
       description = 'LargeVis',
       ext_modules = [LargeVis])
