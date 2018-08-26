#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages


def get_version(filename):
    """Extract the package version"""
    with open(filename) as in_fh:
        for line in in_fh:
            if line.startswith('__version__'):
                return line.split('=')[1].strip()[1:-1]
    raise ValueError("Cannot extract version from %s" % filename)


with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = []

dev_requirements = [
    'coverage', 'pytest', 'pytest-cov', 'pytest-xdist', 'twine', 'pep8',
    'flake8', 'wheel', 'sphinx', 'sphinx-autobuild', 'sphinx_rtd_theme']

version = get_version('./src/python_unpaywall/__init__.py')

setup(
    author="Michael R. Plews",
    author_email='michael.plews@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Python package allowing direct interaction with the Unpaywall REST API ",
    install_requires=requirements,
    extras_require={
        'dev': dev_requirements,
    },
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='python_unpaywall',
    name='python_unpaywall',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url='https://github.com/michaelplews/python_unpaywall',
    version=version,
    zip_safe=False,
)
