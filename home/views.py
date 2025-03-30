from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import toml
import json

from home.models import ColorScheme 

# Create your views here.
@require_http_methods(["GET"])
def home(request: HttpRequest) -> HttpResponse:
    f = open('example_themes/alacritty.toml', 'rb')
    left_text = f.read().decode('utf8')
    f.close()

    f = open('example_themes/alacritty.toml', 'rb')
    right_text = f.read().decode('utf8')
    f.close()

    return render(request, 'home.html', {
        "right_text": right_text,
        "left_text": left_text,
    })

@require_http_methods(["GET"])
def theme_list(request: HttpRequest) -> HttpResponse:
    colorschemes = ColorScheme.objects.order_by('name').all()
    context = {
        "colorschemes": colorschemes,
    }
    return render(request, "themes.html", context)

@require_http_methods(["GET"])
async def theme_view(request: HttpRequest, slug: str) -> HttpResponse:
    queryset = ColorScheme.objects.raw(
        """
        SELECT *
        FROM home_colorscheme
        WHERE LOWER(REPLACE(name, ' ', '-')) = %s
        """, [slug]
    )
    colorscheme = None
    async for scheme in queryset:
        colorscheme = scheme

    context = { "colorscheme": colorscheme }
    return render(request, "themeinfo.html", context)

@require_http_methods(["GET"])
async def download_theme_windows_terminal(request: HttpRequest, slug: str) -> HttpResponse:
    queryset = ColorScheme.objects.raw(
        """
        SELECT *
        FROM home_colorscheme
        WHERE LOWER(REPLACE(name, ' ', '-')) = %s
        """, [slug]
    )
    colorscheme = None
    async for scheme in queryset:
        colorscheme = scheme
    if not colorscheme:
        raise ObjectDoesNotExist()
        # throw an error or something

    filename = "%s.json" % slug

    json_text = json.dumps({
        "name": colorscheme.name,
        "cursorColor": colorscheme.cursor_foreground,
        "selectionBackground": colorscheme.cursor_background,
        "background": colorscheme.background,
        "foreground": colorscheme.foreground,
        "black": colorscheme.color0,
        "blue": colorscheme.color1,
        "cyan": colorscheme.color2,
        "green": colorscheme.color3,
        "purple": colorscheme.color4,
        "red": colorscheme.color5,
        "white": colorscheme.color6,
        "yellow": colorscheme.color7,

        "brightBlack": colorscheme.color8,
        "brightBlue": colorscheme.color9,
        "brightCyan": colorscheme.color10,
        "brightGreen": colorscheme.color11,
        "brightPurple": colorscheme.color12,
        "brightRed": colorscheme.color13,
        "brightWhite": colorscheme.color14,
        "brightYellow": colorscheme.color15,
    })

    response = HttpResponse(json_text.encode('utf8'), content_type="application/json")
    response["Content-Disposition"] = 'attachment; filename="%s"' % filename

    return response

@require_http_methods(["GET"])
async def download_theme_alacritty(_: HttpRequest, slug: str) -> HttpResponse:
    queryset = ColorScheme.objects.raw(
        """
        SELECT *
        FROM home_colorscheme
        WHERE LOWER(REPLACE(name, ' ', '-')) = %s
        """, [slug]
    )
    colorscheme = None
    async for scheme in queryset:
        colorscheme = scheme
    if not colorscheme:
        raise ObjectDoesNotExist()
        # throw an error or something

    filename = "%s.toml" % slug

    data = {
        "colors": {
            "primary": {
                "background": colorscheme.background,
                "foreground": colorscheme.foreground,
            },
            "cursor": {
                "text": colorscheme.cursor_foreground,
                "cursor": colorscheme.cursor_background,
            },
            "normal": {
                "black": colorscheme.color0,
                "red": colorscheme.color1,
                "green": colorscheme.color2,
                "yellow": colorscheme.color3,
                "blue": colorscheme.color4,
                "magenta": colorscheme.color5,
                "cyan": colorscheme.color6,
                "white": colorscheme.color7,
            },
            "bright": {
                "black": colorscheme.color8,
                "red": colorscheme.color9,
                "green": colorscheme.color10,
                "yellow": colorscheme.color11,
                "blue": colorscheme.color12,
                "magenta": colorscheme.color13,
                "cyan": colorscheme.color14,
                "white": colorscheme.color15,
            },
        }
    }

    toml_text = toml.dumps(data)

    response = HttpResponse(toml_text.encode('utf8'), content_type="application/toml")
    response["Content-Disposition"] = 'attachment; filename="%s"' % filename

    return response

@require_http_methods(["GET"])
async def download_theme_kitty(_: HttpRequest, slug: str) -> HttpResponse:
    queryset = ColorScheme.objects.raw(
        """
        SELECT *
        FROM home_colorscheme
        WHERE LOWER(REPLACE(name, ' ', '-')) = %s
        """, [slug]
    )
    colorscheme = None
    async for scheme in queryset:
        colorscheme = scheme
    if not colorscheme:
        raise ObjectDoesNotExist()
        # throw an error or something

    filename = "%s.conf" % slug

    data = f"""background {colorscheme.background}
foreground {colorscheme.foreground}
cursor {colorscheme.cursor_background}
selection_background {colorscheme.color11}
selection_foreground {colorscheme.background}
color0 {colorscheme.color0}
color8 {colorscheme.color8}
color1 {colorscheme.color1}
color9 {colorscheme.color9}
color2 {colorscheme.color2}
color10 {colorscheme.color10}
color3 {colorscheme.color3}
color11 {colorscheme.color11}
color4 {colorscheme.color4}
color12 {colorscheme.color12}
color5 {colorscheme.color5}
color13 {colorscheme.color13}
color6 {colorscheme.color6}
color14 {colorscheme.color14}
color7 {colorscheme.color7}
color15 {colorscheme.color15}
"""

    response = HttpResponse(data.encode('utf8'), content_type="text/plain")
    response["Content-Disposition"] = 'attachment; filename="%s"' % filename

    return response
