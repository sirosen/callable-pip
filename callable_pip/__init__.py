"""
Drop-in replacement for ``pip.main`` + a known-dangerous patch (which is
appropriately named) which will *try* to patch ``pip.main`` to make it work on
all versions of ``pip``
"""


def main(*args):
    """
    Invoke pip in a subprocess, with semantics very similar to `pip.main()`

    Why use check_call instead of check_output?
    It's behavior is slightly closer to the older `pip.main()` behavior,
    printing output information directly to stdout.

    check_call was added in py2.5 and is supported through py3.x , so it's more
    compatible than some alternatives like subprocess.run (added in py3.5)
    """
    import subprocess
    import sys

    try:
        subprocess.check_call([sys.executable, "-m", "pip"] + list(args))
        return 0
    except subprocess.CalledProcessError as err:
        return err.returncode


def dangerous_patch():
    """
    Import ``pip`` and patch ``callable_pip.main`` into it as ``pip.main``
    """
    # defer this import until the patch is invoked -- it may fail with an
    # ImportError in certain (functioning and valid!) versions of pip and we
    # don't want that to kill the whole callable_pip package
    import pip

    # ta-da! That's it
    pip.main = main


__all__ = ("dangerous_patch", "main")
