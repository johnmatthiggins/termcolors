from django.db.models import Q
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import toml
import json

from home.models import ColorScheme 

@require_http_methods(["GET"])
def theme_list(request: HttpRequest) -> HttpResponse:
    colorschemes = ColorScheme.objects.filter(
        ~Q(name__contains="(") & ~Q(name__contains=")")
    ).order_by('name')
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
async def download_theme_windows_terminal(_: HttpRequest, slug: str) -> HttpResponse:
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
        "selectionBackground": colorscheme.cursor_foreground,
        "background": colorscheme.background,
        "foreground": colorscheme.foreground,

        "black": colorscheme.color0,
        "red": colorscheme.color1,
        "green": colorscheme.color2,
        "yellow": colorscheme.color3,
        "blue": colorscheme.color4,
        "purple": colorscheme.color5,
        "cyan": colorscheme.color6,
        "white": colorscheme.color7,

        "brightBlack": colorscheme.color8,
        "brightRed": colorscheme.color9,
        "brightGreen": colorscheme.color10,
        "brightYellow": colorscheme.color11,
        "brightBlue": colorscheme.color12,
        "brightPurple": colorscheme.color13,
        "brightCyan": colorscheme.color14,
        "brightWhite": colorscheme.color15,
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
cursor {colorscheme.cursor_foreground}
selection_background {colorscheme.foreground}
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


@require_http_methods(["GET"])
async def download_theme_suckless(_: HttpRequest, slug: str) -> HttpResponse:
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


    filename = "%s.h" % slug.replace("-", "_")

    data = f"""
static const char *colorname[] = {{
    /* 8 normal colors */
    "{colorscheme.color0}",
    "{colorscheme.color1}",
    "{colorscheme.color2}",
    "{colorscheme.color3}",
    "{colorscheme.color4}",
    "{colorscheme.color5}",
    "{colorscheme.color6}",
    "{colorscheme.color7}",

    /* 8 bright colors */
    "{colorscheme.color8}",
    "{colorscheme.color9}",
    "{colorscheme.color10}",
    "{colorscheme.color11}",
    "{colorscheme.color12}",
    "{colorscheme.color13}",
    "{colorscheme.color14}",
    "{colorscheme.color15}",

    [255] = 0,

    "{colorscheme.background}",
    "{colorscheme.foreground}",
    "{colorscheme.cursor_background}",
    "{colorscheme.cursor_foreground}",
}};

/*
 * Default colors (colorname index)
 * foreground, background, cursor, reverse cursor
 */
unsigned int defaultfg = 257;
unsigned int defaultbg = 256;
unsigned int defaultcs = 258;
static unsigned int defaultrcs = 259;
"""

    response = HttpResponse(data.encode('utf8'), content_type="text/plain")
    response["Content-Disposition"] = 'attachment; filename="%s"' % filename

    return response

