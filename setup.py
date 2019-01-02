# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from io import open
from os import path

from setuptools import setup


HERE = path.dirname(path.abspath(__file__))

with open(path.join(HERE, 'datadog_checks', 'shared', '__about__.py'), 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line.startswith('__version__'):
            VERSION = line.split('=')[1].strip(' \'"')
            break
    else:
        VERSION = '0.0.1'

with open(path.join(HERE, 'README.md'), 'r', encoding='utf-8') as f:
    README = f.read()


setup(
    name='datadog_checks_shared',
    version=VERSION,

    description='The Datadog Checks Shared Tools',
    long_description=README,
    long_description_content_type='text/markdown',
    keywords='datadog agent checks shared tools',

    url='https://github.com/DataDog/datadog-checks-shared',
    author='Datadog',
    author_email='packages@datadoghq.com',
    license='BSD',

    # See https://pypi.org/classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=['datadog_checks', 'datadog_checks.shared'],
    install_requires=['click', 'pylint'],
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'ddshared = datadog_checks.shared.cli:ddshared',
        ],
    },
)
