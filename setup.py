from setuptools import setup, find_packages

setup(
    name='dbutils',
    version='0.0.1',
    url='https://github.com/mypackage.git',
    author='Eugeny Prochan',
    author_email='prochanev@gmail.com',
    description='utils for work with database',
    packages=find_packages(),    
    install_requires=['psycopg2 >= 2.8.4'],
)