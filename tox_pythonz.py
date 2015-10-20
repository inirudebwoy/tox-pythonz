from whichcraft import which

from tox import hookimpl


@hookimpl
def tox_configure(config):
    for py in config.envlist:
        interpreter = py[py.index('py'): py.index('py') + 4]

        if not which('python%s.%s' % tuple(interpreter[2:])):
            # install interpreter
            print(interpreter)
