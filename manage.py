#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from django.core.management import execute_from_command_line
from dotenv import load_dotenv


def main():
    """Run administrative tasks."""
    ROOT_DIR = os.path.dirname(__file__)
    env_path = os.path.join(ROOT_DIR, ".env")
    load_dotenv(env_path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "resume.config.prod")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
