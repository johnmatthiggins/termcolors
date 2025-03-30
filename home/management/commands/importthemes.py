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

def _convert(filepath, format):
    with open(filepath, "rb") as f:
        try:
            data = ThemeConverter(f.read().decode('utf8'), format).dict()
            if not data["cursor_bg"] or not data["cursor_fg"]:
                raise Exception("Oh no! Could not parse the file!")

            new_scheme = ColorScheme(
                path=filepath,
                name=_filename_to_proper_name(filepath),
                background=data["background"],
                foreground=data["foreground"],
                cursor_foreground=data["cursor_fg"],
                cursor_background=data["cursor_bg"],
                color0=data["color0"],
                color1=data["color1"],
                color2=data["color2"],
                color3=data["color3"],
                color4=data["color4"],
                color5=data["color5"],
                color6=data["color6"],
                color7=data["color7"],
                color8=data["color8"],
                color9=data["color9"],
                color10=data["color10"],
                color11=data["color11"],
                color12=data["color12"],
                color13=data["color13"],
                color14=data["color14"],
                color15=data["color15"],
                contrast_ratio=data["contrast_ratio"],
            )
            print("Successfully parsed %s" % filepath)
            return new_scheme
        except Exception as err:
            print("Theme found at %s could not be parsed!" % filepath)
            print(err)

            return None

class Command(BaseCommand):
    help = "Parses themes and installs them into the database"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        schemes = []

        # iterate through a bunch of alacritty color schemes
        # parse each one and save it to the database.
        theme_dir = settings.MEDIA_ROOT / "themes" / "alacritty" / "themes"
        for theme_path in os.listdir(theme_dir):
            full_path = theme_dir / theme_path

            scheme = _convert(full_path, ThemeFormat.ALACRITTY_TOML)
            if scheme:
                if not any([colorscheme for colorscheme in schemes if colorscheme.name == scheme.name]):
                    schemes.append(scheme)

        theme_dir = settings.MEDIA_ROOT / "themes" / "kitty" / "themes"
        for theme_path in os.listdir(theme_dir):
            full_path = theme_dir / theme_path

            scheme = _convert(full_path, ThemeFormat.KITTY)
            if scheme:
                if not any([colorscheme for colorscheme in schemes if colorscheme.name == scheme.name]):
                    schemes.append(scheme)

        print("Successfully parsed %d themes..." % len(schemes))
        ColorScheme.objects.bulk_create(schemes)
