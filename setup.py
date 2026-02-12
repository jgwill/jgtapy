#!/usr/bin/env Python
"""
jgtapy
"""

from setuptools import find_packages, setup
import re
from pathlib import Path

def read_version():
    """Read version from __init__.py without importing."""
    init_file = Path(__file__).parent / "jgtapy" / "__init__.py"
    content = init_file.read_text()
    match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', content)
    if match:
        return match.group(1)
    return "0.0.0"

version = read_version()

INSTALL_REQUIRES = [
    'pandas>=0.25.1',
]

EXTRAS_DEV_LINT = [
    "flake8>=3.6.0,<3.7.0",
    "isort>=4.3.4,<4.4.0",
]

EXTRAS_DEV_TEST = [
    "coverage",
    "pytest>=3.10",
]

EXTRAS_DEV_DOCS = [
    "readme_renderer",
    "sphinx",
    "sphinx_rtd_theme>=0.4.0",
]

setup(
    name='jgtapy',
    version=version,
    description='JGT Technical Indicators for the Pandas\' Dataframes',
    long_description=open('README.rst').read(),
    author='Dmitrii Kurlov/(forked:JGWill)',
    author_email='dmitriik@tutanota.com',
    url='https://github.com/jgwill/jgtapy',
    packages=find_packages(exclude=['*test*']),
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'dev': (EXTRAS_DEV_LINT + EXTRAS_DEV_TEST + EXTRAS_DEV_DOCS),
        'dev-lint': EXTRAS_DEV_LINT,
        'dev-test': EXTRAS_DEV_TEST,
        'dev-docs': EXTRAS_DEV_DOCS,
    },
    license='MIT',
    keywords='technical analyse indicators pandas forex stocks',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
