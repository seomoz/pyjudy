#!/usr/bin/env python

# Copyright (c) 2013 SEOmoz
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


# for fast spearman
ext_modules = [
    Extension('pyjudy.judysl',
        sources=["pyjudy/judysl.pyx"],
        include_dirs = ['/usr/local/include'],
        library_dirs=['/usr/local/lib'],
        libraries=['Judy']
    )]



setup(
    name             = 'pyjudy',
    version          = '0.0.1',
    description      = 'Python bindings to libJudy',
    author           = 'Matt Peters',
    author_email     = 'matt@seomoz.org',
    url              = 'http://github.com/seomoz/pyjudy',
    packages         = ['pyjudy'],
    license          = 'MIT',
    platforms        = 'Posix; MacOS X',
    cmdclass         = {'build_ext': build_ext},
    ext_modules      = ext_modules,
    classifiers      = [
        'License :: OSI Approved :: MIT License',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        ],
)
