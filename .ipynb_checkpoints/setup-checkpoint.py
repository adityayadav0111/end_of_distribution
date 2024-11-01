from setuptools import setup, find_packages

setup(
    name='end_of_distribution',
    version='0.1',
    packages=find_packages(include=['lib', 'lib.*']),
    description='A library to detect the end of distribution in datasets',
    author='Aditya Yadav',  
    author_email='aditya.yadav.bse@gmail.com',  
    url='https://github.com/adityayadav0111/end_of_distribution',  
)

