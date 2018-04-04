"""
callable_pip setup script
Supports setuptools or even distutils
The entire package consists of a single file and is mostly documentation
"""

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


LONG_DESCRIPTION = open(
    os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name='callable-pip',
    version='1.0.0',
    description='callable-pip patches over the wide use of pip.main()',
    long_description=LONG_DESCRIPTION,
    packages=['callable_pip'],
    author='Stephen Rosen',
    author_email='sirosen@uchicago.edu',
    url='https://github.com/sirosen/callable-pip',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
