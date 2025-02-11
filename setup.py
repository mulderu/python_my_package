#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ["glob2", "numpy", "names"]

test_requirements = []

def get_version(rel_path):
    for line in open(rel_path).read().splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name='my_package',
    version=get_version("my_package/__init__.py"),
    author="Mulder Yu",
    author_email='mulderu@gmail.com',
    packages=find_packages(include=['my_package', 'my_package.*']),
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Demo Library to study",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='addsub',
    url='https://github.com/mulderu/addsub_study',
    zip_safe=False,
)