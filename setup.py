"""
sffloat package setup for pypi
"""

import setuptools
from sffloat.__version__ import VERSION

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sffloat",
    include_package_data=True,
    version=VERSION,
    author="Eric Dennison",
    author_email="ericd@netdenizen.com",
    description="SFFloat class for floating point computations that account for precision or 'sig figs'.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tiggerntatie/sffloat",
    packages=setuptools.find_packages(),
    install_requires=['sigfig>=1.1.8',],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)