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

async def theme_list(request: HttpRequest) -> HttpResponse:
    queryset = ColorScheme.objects.all()
    colorschemes = []
    async for colorscheme in queryset:
        colorschemes.append(colorscheme)
        
    context = {
        "colorschemes": colorschemes,
    }
    return render(request, "themes.html", context)
