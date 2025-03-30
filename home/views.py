from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from home.models import ColorScheme 

# Create your views here.
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

def theme_list(request: HttpRequest) -> HttpResponse:
    colorschemes = ColorScheme.objects.order_by('name').all()
    context = {
        "colorschemes": colorschemes,
    }
    return render(request, "themes.html", context)

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
