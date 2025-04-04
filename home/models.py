import json

from django.db import models

# represents a theme
# this is basically a glorified cache for the media files we downloaded
class ColorScheme(models.Model):
    path = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)

    is_dark = models.BooleanField(default=True, null=False)

    background = models.CharField(max_length=8)
    foreground = models.CharField(max_length=8)

    cursor_background = models.CharField(max_length=8)
    cursor_foreground = models.CharField(max_length=8)

    # normal colors
    color0 = models.CharField(max_length=8)
    color1 = models.CharField(max_length=8)
    color2 = models.CharField(max_length=8)
    color3 = models.CharField(max_length=8)
    color4 = models.CharField(max_length=8)
    color5 = models.CharField(max_length=8)
    color6 = models.CharField(max_length=8)
    color7 = models.CharField(max_length=8)

    # bright colors
    color8 = models.CharField(max_length=8)
    color9 = models.CharField(max_length=8)
    color10 = models.CharField(max_length=8)
    color11 = models.CharField(max_length=8)
    color12 = models.CharField(max_length=8)
    color13 = models.CharField(max_length=8)
    color14 = models.CharField(max_length=8)
    color15 = models.CharField(max_length=8)

    # useful for finding high contrast themes
    contrast_ratio = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self) -> str:
        dict_data = {
            "path": str(self.path),
            "name": self.name,
            "background": self.background,
            "foreground": self.foreground,
            "cursor_background": self.cursor_background,
            "cursor_foreground": self.cursor_foreground,
            "color0": self.color0,
            "color1": self.color1,
            "color2": self.color2,
            "color3": self.color3,
            "color4": self.color4,
            "color5": self.color5,
            "color6": self.color6,
            "color7": self.color7,
            "color8": self.color8,
            "color9": self.color9,
            "color10": self.color10,
            "color11": self.color11,
            "color12": self.color12,
            "color13": self.color13,
            "color14": self.color14,
            "color15": self.color15,
        }
        return json.dumps(dict_data, indent=4)
