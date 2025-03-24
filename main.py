#!/usr/bin/env python
import tomllib as toml

def main():
    with open("cobalt.toml", "rb") as f:
        data = toml.load(f)
        print(data)

def generate_kitty_theme(toml_data):
    background    = toml_data['colors']['primary']['background']
    foreground    = toml_data['colors']['primary']['foreground']

    # todo: figure out better values for these
    selection_background = foreground
    selection_foreground = background

    cursor_text   = toml_data['colors']['cursor']['text']
    cursor_cursor = toml_data['colors']['cursor']['cursor']

    # todo figure out color mapping...
    color0 = toml_data['colors']['normal']['black']
    color1 = toml_data['colors']['normal']['red']
    color2 = toml_data['colors']['normal']['green']
    color3 = toml_data['colors']['normal']['yellow']
    color4 = toml_data['colors']['normal']['blue']
    color5 = toml_data['colors']['normal']['magenta']
    color6 = toml_data['colors']['normal']['cyan']
    color7 = toml_data['colors']['normal']['white']

    color8 = toml_data['colors']['bright']['black']
    color9 = toml_data['colors']['bright']['red']
    color10 = toml_data['colors']['bright']['green']
    color11 = toml_data['colors']['bright']['yellow']
    color12 = toml_data['colors']['bright']['blue']
    color13 = toml_data['colors']['bright']['magenta']
    color14 = toml_data['colors']['bright']['cyan']
    color15 = toml_data['colors']['bright']['white']



if __name__ == '__main__':
    main()
