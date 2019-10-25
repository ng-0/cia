#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="cia",
    version="0.0",

    packages=['cia'],
    scripts=['bin/hack'],
    install_requires=['colorama'],
    author="ng0",
    author_email="ng0@n0.is",
    description="Hack the CIA.",
    long_description="""Non-interactive hecking with 30 grains of salt.""",
    license="bsd-2",
    keywords="cia humor humour nonsense",
    url="https://n0.is/s/cia",
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'License :: BSD-2',
                 'Operating System :: OS Independent',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX'],
    platforms=['windows', 'Linux', 'MacOS X', 'Solaris', 'FreeBSD'],
)
