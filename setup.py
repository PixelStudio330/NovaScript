#!/usr/bin/env python3
"""
Setup configuration for NovaScript-X runtime.

Install via: pip install .
or: pip install -e . (for development)

This creates the 'novax' command globally available on your system.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read version
version_file = Path(__file__).parent / 'novascriptx' / 'interpreter.py'
version = None

if version_file.exists():
    with open(version_file) as f:
        for line in f:
            if line.startswith('__version__'):
                version = line.split('"')[1]
                break

if not version:
    version = '1.0.0'

# Read README
readme_file = Path(__file__).parent / 'README.md'
long_description = ''

if readme_file.exists():
    with open(readme_file, 'r', encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='novascript-x',
    version=version,
    description='NovaScript-X - A lightweight, modern programming language runtime',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/YourRepo/NovaScript-X',
    license='MIT',
    python_requires='>=3.7',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'novax=novascriptx.novascriptx_cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Interpreters',
        'Topic :: Software Development :: Testing',
    ],
    keywords='interpreter programming-language runtime novascript language',
    project_urls={
        'Documentation': 'https://github.com/YourRepo/NovaScript-X#readme',
        'Source': 'https://github.com/YourRepo/NovaScript-X',
        'Issues': 'https://github.com/YourRepo/NovaScript-X/issues',
    },
)
