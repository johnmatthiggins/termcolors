from django.core.management.base import BaseCommand

import subprocess

class Command(BaseCommand):
    help = "Formats Python code"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        subprocess.run(["poetry", "run", "ruff", "format"], shell=True, check=True)

