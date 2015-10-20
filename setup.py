# content of setup.py
from setuptools import setup

if __name__ == "__main__":
    setup(
        name='tox-missingpython',
        description='tox plugin decsription',
        license="MIT license",
        version='0.1',
        py_modules=['tox_missingpython'],
        entry_points={'tox': ['missingpython = tox_missingpython']},
        install_requires=['tox>=2.0'],
    )
