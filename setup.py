from setuptools import setup, find_packages

setup(
    name='HistoryAlert',
    version='1.0',
    packages=find_packages(),
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'HistoryAlert=main:main',  # Command name and entry function
        ],
    },
)
