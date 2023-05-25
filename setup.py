#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
try:
    from pipenv.project import Project
    from pipenv.utils import convert_deps_to_pip

    pfile = Project().parsed_pipfile
    requirements = convert_deps_to_pip(pfile['packages'], r=False)
    test_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)
except ImportError:
    # get the requirements from the requirements.txt
    requirements = [line.strip()
                    for line in open('requirements.txt').readlines()
                    if line.strip() and not line.startswith('#')]
    # get the test requirements from the test_requirements.txt
    test_requirements = [line.strip()
                         for line in
                         open('dev-requirements.txt').readlines()
                         if line.strip() and not line.startswith('#')]

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')
version = open('.VERSION').read()


setup(
    name='''wikiseriesevilib''',
    version=version,
    description='''Library to use Wikipedia to query tv series episodes lists''',
    long_description=readme + '\n\n' + history,
    author='''Evi Vanmechelen''',
    author_email='''evi_github@gmail.com''',
    url='''https://github.com/evanme20/wikiseriesevilib''',
    packages=find_packages(where='.', exclude=('tests', 'hooks', '_CI*')),
    package_dir={'''wikiseriesevilib''':
                 '''wikiseriesevilib'''},
    include_package_data=True,
    install_requires=requirements,
    license='MIT',
    zip_safe=False,
    keywords='''wikiseriesevilib wikipedia''',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
        ],
    test_suite='tests',
    tests_require=test_requirements
)
