from setuptools import setup, find_packages

with open('README.md') as file:
    readme = file.read()

setup(
    name='src',
    version='0.0.1',
    description='Selenium tests',
    long_description=readme,
    author='Hanna Grodzicka',
    author_email='226154@student.pwr.edu.pl',
    url='https://github.com/hvvka/selenium',
    packages=find_packages(), install_requires=['selenium', 'TestLink-API-Python-client']
)
