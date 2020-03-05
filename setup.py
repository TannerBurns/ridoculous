import os
from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), 'RIDOCULOUS_README_GENERATED_FOR_DISTUTILS.md')) as readme:
    README = readme.read()


setup(
    name='ridoculous',
    version='0.0.2',
    packages=find_packages(exclude=['examples']),
    include_package_data=True,
    description='Easily document any object to a markdown file',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://www.github.com/tannerburns/ridoculous',
    author='Tanner Burns',
    author_email='tjburns102@gmail.com',
    install_requires=[],
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
    ],
)