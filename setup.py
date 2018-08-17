#!/usr/bin/env python
"""python module to manage RSVP"""

import os
from setuptools import setup, find_packages


with open(
        os.path.join(os.path.dirname(__file__), "requirements.txt"), 'rb'
) as require:
    REQUIRE = require.read().decode('utf-8').splitlines() + ['setuptools']


setup(
    name='rsvp',
    version='0.1.0',
    description="Python module to manage RSVP",
    platforms=["Linux"],
    packages=find_packages(),
    author="Sundeep Anand",
    author_email="sundeep.co.in@gmail.com",
    license="Apache License 2.0",
    install_requires=REQUIRE,
    setup_requires=["flake8"],
    test_suite="test_rsvp.rsvp_test_suit",
    classifiers=[
        'License :: OSI Approved :: Apache License 2.0 (Apache-2.0)',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
