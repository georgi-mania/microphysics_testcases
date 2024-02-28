'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- Microphysics Test Cases -----
File: setup.py
Project: microphysics_testcases
Created Date: Tuesday 27th February 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Wednesday 28th February 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
'''


from setuptools import setup, find_packages

setup(
    name='Microphysics Test Cases',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'pytest',
        'sphinx',
    ],
)
