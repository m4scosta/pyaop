# coding: utf-8
import os
import codecs

from setuptools import setup, find_packages

import pyaop

here = os.path.abspath(os.path.dirname(__file__))

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()


def long_description():
    with codecs.open('README.rst', encoding='utf8') as f:
        return f.read()

setup(
    name='pyaop',
    version=pyaop.__version__,
    url='',
    download_url='',
    license='Apache Software License',
    author='Marcos Costa Pinto',
    install_requires=[],
    author_email='marcos@gtacsolutions.com',
    description='Aspect Oriented Programming python micro framework',
    long_description=README,
    packages=find_packages('pyaop'),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    tests_require=[],
)