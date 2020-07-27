# -*- coding: utf-8 -*-
# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='MetabaseClient',
    version='0.1.0',
    description='Metabase python wrapper is built upon Metabase restful API to help its users in extending features and adding more capability.',
    long_description=readme,
    author='Rahul Rathi',
    author_email='VanGiex.RR@Gmail.com',
    url='https://github.com/vangiex/metabaseclient',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    classifiers=[
        'Development Status :: 0.1.0 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Metabase Api :: Python Wrapper',
        'License :: OSI Approved :: GNU General Public License (GPL)',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

)
