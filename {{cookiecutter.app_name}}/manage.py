#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if os.environ.get("DJANGO_DEBUG")=='True':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.app_name}}.config")
        os.environ.setdefault("DJANGO_CONFIGURATION", "Local")

        # Only attach the debugger when we're the Django that deals with requests
        if os.environ.get('RUN_MAIN') or os.environ.get('WERKZEUG_RUN_MAIN'):
            import ptvsd
            ptvsd.enable_attach()

    try:
        from configurations.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django  # noqa
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
