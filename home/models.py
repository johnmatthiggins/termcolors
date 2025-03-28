from django.db import models

# represents a theme
# this is basically a glorified cache for the media files we downloaded
class ColorScheme(models.Model):
    path = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)

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
