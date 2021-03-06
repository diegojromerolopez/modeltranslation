# -*- coding: utf-8 -*-

# Copyright (c) 2015 by intelligenia <info@intelligenia.es>
#
# The MIT License (MIT)
#
# Copyright (c) 2016 intelligenia soluciones informáticas

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

data_files = []
for dirpath, dirnames, filenames in os.walk('.'):
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        continue
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

setup(
    name="modeltranslation",
    version="0.1",
    author="intelligenia S.L.",
    author_email="diego@intelligenia.es",
    description="Modeltranslation is an utility to translate Django model fields.",
    long_description=(read('README.md') + '\n\n' + read('CHANGES.md')),
    classifiers=[
        'Development Status :: 1 - Alfa',
        'Framework :: Django',
        'License :: OSI Approved :: The MIT License (MIT)',
    ],
    license="MIT",
    keywords="modeltranslation translations",
    url='https://github.com/intelligenia/modeltranslation',
    packages=find_packages('.'),
    data_files=data_files,
    include_package_data=True,
)
