from Cython.Build import cythonize
from setuptools import setup, Extension, find_packages
from Cython.Distutils import build_ext
import numpy
import  platform

# make if clause here, for use of openMP if available
USE_CYTHON = True
USE_OPENMP = True

ext = '.pyx' if USE_CYTHON else '.c'

# No openMP support on MAC compile without openMP flags
if ('Darwin' in platform.platform()) or (USE_OPENMP is False):

    ext_modules = [
        Extension(
            "lom._cython.matrix_updates", ["lom/_cython/matrix_updates"+ext],
            include_dirs=[numpy.get_include()],
            extra_compile_args = ["-Ofast", "-ffast-math", "-march=native"]#, "-fopenmp"],
            #extra_link_args=['-fopenmp'],
            ),
        Extension(
            "lom._cython.tensor_updates", ["lom/_cython/tensor_updates"+ext],
            include_dirs=[numpy.get_include()],
            extra_compile_args = ["-Ofast", "-ffast-math", "-march=native"]#, "-fopenmp"],
            #extra_link_args=['-fopenmp'],
            )
        ]

else:
    ext_modules = [
    Extension(
        "lom._cython.tensor_updates", ["lom/_cython/tensor_updates"+ext],
        include_dirs=[numpy.get_include()],
        extra_compile_args = ["-Ofast", "-ffast-math", "-march=native", "-fopenmp"],
        extra_link_args=['-fopenmp'],
        ),
    Extension(
        "lom._cython.matrix_updates", ["lom/_cython/matrix_updates"+ext],
        include_dirs=[numpy.get_include()],
        extra_compile_args = ["-Ofast", "-ffast-math", "-march=native", "-fopenmp"],
        extra_link_args=['-fopenmp'],
        )
    ]


if USE_CYTHON:
    from Cython.Build import cythonize
    ext_modules = cythonize(ext_modules)



setup(
    name='LogicalOperatorMachines',
    version='0.2',
    author='Tammo Rukat',
    author_email='tammorukat@gmail.com',
    packages=find_packages(exclude=('tests')),
    # package_dir = {'': 'lom'},
    # py_modules=['wrappers','experiments','lib','lom','lom_sampling'],
    # py_modules=['src.*','src.cython.*'],
    # install_requires=['numpy','Cython'],
    ext_modules=ext_modules,
)