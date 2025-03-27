from django.core.management.base import BaseCommand
from django.conf import settings

import sys

import subprocess

GITHUB_REPO_URL = "https://github.com/alacritty/alacritty-theme.git"

class Command(BaseCommand):
    help = "Downloads alacritty themes from GitHub repository"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        destination = settings.MEDIA_ROOT / "themes"
        CMD = "git clone %s %s" % (GITHUB_REPO_URL, destination)
        try:
            subprocess.run(CMD, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            print("Command exited with non-zero status code! (%d)" % (err.returncode))
            sys.exit(1)

        # remove git directory after cloning
        CMD = "rm -Irf %s" % (destination / ".git")
        try:
            subprocess.run(CMD, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            print("Command exited with non-zero status code! (%d)" % (err.returncode))
            sys.exit(1)
