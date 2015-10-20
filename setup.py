# content of setup.py
from setuptools import setup

if __name__ == "__main__":
    setup(
        name='tox-pythonz',
        description='tox plugin decsription',
        license="MIT license",
        version='0.1',
        py_modules=['tox_pythonz'],
        entry_points={'tox': ['pythonz = tox_pythonz']},
        install_requires=['tox>=2.0',
                          'whichcraft'],
    )
