from setuptools import setup, find_packages

setup(
    name='HistoryAlert',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['main', 'show_todays_history', 'get_database', 'update_events'],
    entry_points={
        'console_scripts': [
            'historyalert=main:main',
        ],
    },
    install_requires=[
        'pandas',
        'pyfiglet',
        'colorama',
    ],
    description='A CLI app for discovering historical events.',
    url='https://github.com/lennovative/history_alert',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
