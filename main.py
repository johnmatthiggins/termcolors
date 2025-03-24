#!/usr/bin/env python
from enum import Enum
import tomllib as toml

class ThemeFormat(Enum):
    ALACRITTY_TOML = 0
    ALACRITTY_YAML = 1
    KITTY     = 2
    ITERM2    = 3
    XTERM     = 4
    WINDOWS_TERMINAL = 5

def file_ext_to_format(file_ext):
    match file_ext.lower():
        case 'xresources':
            return ThemeFormat.XTERM

        # maybe kitty but who knows...
        # conf is a pretty generic file extension
        case 'conf':
            pass

        # assume this is alacritty
        case 'toml':
            return ThemeFormat.ALACRITTY_TOML
        case 'yaml':
            return ThemeFormat.ALACRITTY_YAML
        case 'yml':
            return ThemeFormat.ALACRITTY_YAML

        case 'itermcolors':
            return ThemeFormat.ITERM2

        case 'json':
            return ThemeFormat.WINDOWS_TERMINAL

        case _:
            raise Exception("File extension is not recognized!")


# intermediate representation of themes
class ThemeIR:
    # colors = array of 16 rgb values... (strings)
    def __init__(self, text: str, input_type: ThemeFormat):
        match input_type:
            case ThemeFormat.ALACRITTY_YAML:
                self._load_alacritty_yaml(text)
            case ThemeFormat.ALACRITTY_TOML:
                self._load_alacritty_toml(text)
            case ThemeFormat.KITTY:
                self._load_kitty(text)
            case ThemeFormat.ITERM2:
                self._load_iterm2(text)
            case ThemeFormat.XTERM:
                self._load_xterm(text)
            case ThemeFormat.WINDOWS_TERMINAL:
                self._load_windows_terminal(text)

    def _load_alacritty_toml(self, text: str):
        theme_data = toml.loads(text)

        background    = theme_data['colors']['primary']['background']
        foreground    = theme_data['colors']['primary']['foreground']

        cursor_text = background
        cursor_cursor = foreground
        if theme_data['colors'].get('cursor'):
            cursor_text   = theme_data['colors']['cursor'].get('text')
            cursor_cursor = theme_data['colors']['cursor'].get('cursor')

        color0 = theme_data['colors']['normal']['black']
        color1 = theme_data['colors']['normal']['red']
        color2 = theme_data['colors']['normal']['green']
        color3 = theme_data['colors']['normal']['yellow']
        color4 = theme_data['colors']['normal']['blue']
        color5 = theme_data['colors']['normal']['magenta']
        color6 = theme_data['colors']['normal']['cyan']
        color7 = theme_data['colors']['normal']['white']

        color8 = theme_data['colors']['bright']['black']
        color9 = theme_data['colors']['bright']['red']
        color10 = theme_data['colors']['bright']['green']
        color11 = theme_data['colors']['bright']['yellow']
        color12 = theme_data['colors']['bright']['blue']
        color13 = theme_data['colors']['bright']['magenta']
        color14 = theme_data['colors']['bright']['cyan']
        color15 = theme_data['colors']['bright']['white']

        self._colors = [
            color0,
            color1,
            color2,
            color3,
            color4,
            color5,
            color6,
            color7,
            color8,
            color9,
            color10,
            color11,
            color12,
            color13,
            color14,
            color15,
        ]
        self._background = background
        self._foreground = foreground
        self._cursor_foreground = cursor_cursor 
        self._cursor_background = cursor_text


    def _load_alacritty_yaml(self, text: str):
        pass

    def _load_kitty(self, text: str):
        pass

    def _load_xterm(self, text: str):
        pass

    def _load_iterm2(self, text: str):
        pass

    def _load_windows_terminal(self, text: str):
        pass

    def text(self, output_type: ThemeFormat) -> str:
        match output_type:
            case ThemeFormat.ALACRITTY_YAML:
                return self._output_alacritty_yaml()
            case ThemeFormat.ALACRITTY_TOML:
                return self._output_alacritty_toml()
            case ThemeFormat.KITTY:
                return self._output_kitty()
            case ThemeFormat.ITERM2:
                return self._output_iterm2()
            case ThemeFormat.XTERM:
                return self._output_xterm()
            case ThemeFormat.WINDOWS_TERMINAL:
                return self._output_windows_terminal()

    def _output_alacritty_toml(self) -> str:
        return ""

    def _output_alacritty_yaml(self) -> str:
        return ""

    def _output_iterm2(self) -> str:
        return ""

    def _output_xterm(self) -> str:
        return ""

    def _output_kitty(self) -> str:
        return ""

    def _output_windows_terminal(self) -> str:
        return ""

class ThemeConverter:
    def __init__(self, text: str, input_type: ThemeFormat):
        self._theme = ThemeIR(text, input_type)

    def text(self, output_type: ThemeFormat):
        return self._theme.text(output_type)

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
