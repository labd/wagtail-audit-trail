#!/usr/bin/env python
from setuptools import find_packages, setup

install_requires = [
    'wagtail>=2.0',
]

docs_require = [
    'sphinx>=1.4.0',
]

tests_require = [
    'pytest-cov==2.4.0',
    'pytest-django==3.1.2',
    'pytest==3.0.5',
    'requests-mock==1.1.0',

    # Linting
    'isort==4.2.5',
    'flake8==3.0.3',
    'flake8-blind-except==0.1.1',
    'flake8-debugger==1.4.0',
    'flake8-imports==0.1.0',
]

setup(
    name='wagtail-audit-trail',
    version='1.3.0',
    description="Wagtail audit trail",
    long_description=open('README.rst', 'r').read(),
    url='https://github.com/labd/wagtail-audit-trail',
    author="Lab Digital",
    author_email="opensource@labdigital.nl",
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'docs': docs_require,
        'test': tests_require,
    },
    entry_points={},
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=False,
)
