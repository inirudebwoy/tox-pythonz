from tox import hookimpl


@hookimpl
def tox_configure(config):
    for py in config.envlist:
        print(py)
