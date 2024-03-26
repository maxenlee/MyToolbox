from setuptools import setup, find_packages 

setup(
    name='Toolbox-', 
    version='0.1.0',
    author='Jacob Raffety',
    author_email='jacobraffety@gmail.com',
    packages=find_packages(),
    url='https://github.com/JacobRaffety/Toolbox-',
    license='LICENSE.txt',  # Make sure to specify the correct license file name
    description='This is my data science toolbox for useful code.',
    long_description=open('README.md').read(),
    install_requires=[
        'numpy >= 1.11.1'
    ],
)
