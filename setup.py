from setuptools import setup, find_packages
import os
from os import path
import template_demo

# Model package name
NAME = template_demo.__name__

# Default package dir
PKG_DIR = path.basename(path.dirname(template_demo.__file__))

# Current Version
VERSION = os.environ.get('APP_VERSION', 'latest')

# Dependecies for the package
with open('requirements.txt') as r:
    DEPENDENCIES = [
        dep for dep in map(str.strip, r.readlines())
        if all([not dep.startswith("#"),
                not dep.endswith("#dev"),
                len(dep) > 0])
    ]

# Project descrpition
with open("README.md") as f:
    LONG_DESCRIPTION = f.read()


setup(
    name=NAME,
    version=VERSION,
    description='<@description>',
    long_description=LONG_DESCRIPTION,
    author='Vitor Hugo',
    author_email='vitor.deluca@neoway.com.br',
    license='MIT',
    packages=find_packages(exclude=("tests", "docs")),
    entry_points={
        'console_scripts': [
            '{name}={dir}.main:cli'.format(
                name=NAME,
                dir=PKG_DIR
            )
        ],
    },
    # external packages as dependencies
    install_requires=DEPENDENCIES
)
