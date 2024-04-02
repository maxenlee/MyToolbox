from setuptools import setup, find_packages

# Read the contents of your requirements.txt file
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='MyToolbox',
    version='0.1.0',
    author='Maxen Niedermier',
    author_email='m.lee@maxime.group',
    packages=find_packages(),
    url='https://github.com/maxenlee/MyToolbox',
    license='LICENSE.txt',  # Make sure to specify the correct license file name
    description='This is my data science toolbox for useful code.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # If your README.md is in markdown
    install_requires=required,
)
