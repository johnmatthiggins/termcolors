from django.core.management.base import BaseCommand

import subprocess


class Command(BaseCommand):
    help = "Formats Python code"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        CMD = "poetry run ruff check"
        try:
            subprocess.run(CMD, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            print("Command exited with non-zero status code! (%d)" % (err.returncode))
