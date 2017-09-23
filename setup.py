# -*- coding: utf-8 -*-
import io
import os
import re

from setuptools import setup, find_packages


# Convert description from markdown to reStructuredText
try:
    import pypandoc
    description = pypandoc.convert('README.md', 'rst', 'markdown')
except (OSError, ImportError):
    description = ''


# Get package version number
# Source: https://packaging.python.org/single_source_version/
def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='monz',
    url='https://github.com/pawelad/monz',
    download_url='https://github.com/pawelad/monz/releases/latest',
    bugtrack_url='https://github.com/pawelad/monz/issues',
    version=find_version('src', 'monz', '__init__.py'),
    license='MIT License',
    author='Paweł Adamczak',
    author_email='pawel.ad@gmail.com',
    maintainer='Paweł Adamczak',
    maintainer_email='pawel.ad@gmail.com',
    description='Simple (and awesome) command line interface for quickly '
                'accessing your (equally awesome) Monzo account info, its '
                'current balance, latest transactions and more.',
    long_description=description,
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    zip_safe=False,
    install_requires=[
        'Babel>=2.5.1',
        'click>=6.7',
        'click-default-group>=1.2',
        'pymonzo>=0.10.0',
    ],
    entry_points={
        'console_scripts': [
            'monz=monz.__main__:main',
        ],
    },
    keywords=['monzo', 'cli', 'script', 'mondo'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
)
