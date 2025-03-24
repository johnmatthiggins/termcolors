#!/usr/bin/env python
import tomllib as toml

def main():
    with open("alacritty.toml", "rb") as f:
        data = toml.load(f)
        print(generate_kitty_theme(data))

def generate_kitty_theme(toml_data):
    background    = toml_data['colors']['primary']['background']
    foreground    = toml_data['colors']['primary']['foreground']

    cursor_text = background
    cursor_cursor = foreground
    if toml_data['colors'].get('cursor'):
        cursor_text   = toml_data['colors']['cursor'].get('text')
        cursor_cursor = toml_data['colors']['cursor'].get('cursor')

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

    kitty_config = f'''
background\t\t\t{background}
foreground\t\t\t{foreground}
selection_background\t\t\t{foreground}
selection_foreground\t\t\t{background}
cursor\t\t\t{cursor_cursor}
color0\t\t\t{color0}
color1\t\t\t{color1}
color2\t\t\t{color2}
color3\t\t\t{color3}
color4\t\t\t{color4}
color5\t\t\t{color5}
color6\t\t\t{color6}
color7\t\t\t{color7}
color8\t\t\t{color8}
color9\t\t\t{color9}
color10\t\t\t{color10}
color11\t\t\t{color11}
color12\t\t\t{color12}
color13\t\t\t{color13}
color14\t\t\t{color14}
color15\t\t\t{color15}
active_tab_foreground\t\t\t{color15}
active_tab_background\t\t\t{color8}
inactive_tab_foreground\t\t\t{color15}
inactive_tab_background\t\t\t{color0}
'''
    return kitty_config


if __name__ == '__main__':
    main()
