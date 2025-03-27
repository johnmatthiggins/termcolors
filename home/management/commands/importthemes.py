from django.core.management.base import BaseCommand
import os
from django.conf import settings

from home.models import ColorScheme
from home.convert import ThemeConverter, ThemeFormat

def _strip_file_ext(filename):
    filename_no_ext = filename.split('.')[0]
    return filename_no_ext

# takes in filepath and outputs proper name for theme
def _filename_to_proper_name(path):
    filename = os.path.basename(path)
    file_no_ext = _strip_file_ext(filename)
    segments = file_no_ext.split('_')
    words = []
    for segment in segments:
        words.append(segment[0:1].upper() + segment[1:])

    return " ".join(words)

class Command(BaseCommand):
    help = "Parses themes and installs them into the database"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # iterate through a bunch of alacritty color schemes
        # parse each one and save it to the database.
        theme_dir = settings.MEDIA_ROOT / "themes" / "themes"
        for theme_path in os.listdir(theme_dir):
            full_path = theme_dir / theme_path
            # print(full_path, _filename_to_proper_name(theme_path))

            with open(full_path, "rb") as f:
                theme_text = f.read()
                try:
                    ThemeConverter(theme_text.decode("utf8"), ThemeFormat.ALACRITTY_TOML)
                    print("Successfully parsed %s" % full_path)
                except Exception:
                    print("Theme found at %s could not be parsed!" % full_path)
