#!/usr/bin/env python
from enum import Enum
import io
import json
import toml
import yaml

class ThemeFormat(Enum):
    ALACRITTY_TOML = 0
    ALACRITTY_YAML = 1
    KITTY     = 2
    ITERM2    = 3
    XTERM     = 4
    WINDOWS_TERMINAL = 5

def file_ext_to_format(file_ext: str) -> ThemeFormat:
    match file_ext.lower():
        case 'xresources':
            return ThemeFormat.XTERM
        # maybe kitty but who knows...
        # conf is a pretty generic file extension
        case 'conf':
            return ThemeFormat.KITTY
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
        from yaml import CLoader as Loader
        theme_data = yaml.load(text, Loader)

        background    = theme_data['colors']['primary']['background'].replace('0x', '#')
        foreground    = theme_data['colors']['primary']['foreground'].replace('0x', '#')

        cursor_text = background
        cursor_cursor = foreground
        if theme_data['colors'].get('cursor'):
            cursor_text   = theme_data['colors']['cursor'].get('text').replace('0x', '#')
            cursor_cursor = theme_data['colors']['cursor'].get('cursor').replace('0x', '#')

        color0 = theme_data['colors']['normal']['black'].replace('0x', '#')
        color1 = theme_data['colors']['normal']['red'].replace('0x', '#')
        color2 = theme_data['colors']['normal']['green'].replace('0x', '#')
        color3 = theme_data['colors']['normal']['yellow'].replace('0x', '#')
        color4 = theme_data['colors']['normal']['blue'].replace('0x', '#')
        color5 = theme_data['colors']['normal']['magenta'].replace('0x', '#')
        color6 = theme_data['colors']['normal']['cyan'].replace('0x', '#')
        color7 = theme_data['colors']['normal']['white'].replace('0x', '#')

        color8 = theme_data['colors']['bright']['black'].replace('0x', '#')
        color9 = theme_data['colors']['bright']['red'].replace('0x', '#')
        color10 = theme_data['colors']['bright']['green'].replace('0x', '#')
        color11 = theme_data['colors']['bright']['yellow'].replace('0x', '#')
        color12 = theme_data['colors']['bright']['blue'].replace('0x', '#')
        color13 = theme_data['colors']['bright']['magenta'].replace('0x', '#')
        color14 = theme_data['colors']['bright']['cyan'].replace('0x', '#')
        color15 = theme_data['colors']['bright']['white'].replace('0x', '#')

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

    def _load_kitty(self, text: str):
        theme = {}
        for line in text.splitlines():
            segments = line.split()
            if len(segments) == 2:
                key = segments[0]
                value = segments[1]

                theme[key] = value

        self._background = theme["background"]
        self._foreground = theme["foreground"]
        self._cursor_background = theme["cursor"]
        self._cursor_foreground = theme["background"]
        self._ = theme["selection_background"]
        self._ = theme["selection_foreground"]

        self._colors = []
        self._colors.append(theme["color0"])
        self._colors.append(theme["color1"])
        self._colors.append(theme["color2"])
        self._colors.append(theme["color3"])
        self._colors.append(theme["color4"])
        self._colors.append(theme["color5"])
        self._colors.append(theme["color6"])
        self._colors.append(theme["color7"])
        self._colors.append(theme["color8"])
        self._colors.append(theme["color9"])
        self._colors.append(theme["color10"])
        self._colors.append(theme["color11"])
        self._colors.append(theme["color12"])
        self._colors.append(theme["color13"])
        self._colors.append(theme["color14"])
        self._colors.append(theme["color15"])

    def _load_xterm(self, text: str):
        pass

    def _load_iterm2(self, text: str):
        pass

    def _load_windows_terminal(self, text: str):
        theme_data = json.loads(text)

        self._cursor_foreground = theme_data["cursorColor"]
        self._cursor_background = theme_data["selectionBackground"]

        self._background = theme_data["background"]
        self._foreground = theme_data["foreground"]

        self._colors = [
            theme_data["black"],
            theme_data["red"],
            theme_data["green"],
            theme_data["yellow"],
            theme_data["blue"],
            theme_data["purple"],
            theme_data["cyan"],
            theme_data["white"],

            theme_data["brightBlack"],
            theme_data["brightRed"],
            theme_data["brightGreen"],
            theme_data["brightYellow"],
            theme_data["brightBlue"],
            theme_data["brightPurple"],
            theme_data["brightCyan"],
            theme_data["brightWhite"],
        ]

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
        theme_data = {
            "colors": {
                "primary": {
                    "background": self._background,
                    "foreground": self._foreground,
                },
                "normal": {
                    "black": self._colors[0],
                    "red": self._colors[1],
                    "green": self._colors[2],
                    "yellow": self._colors[3],
                    "blue": self._colors[4],
                    "magenta": self._colors[5],
                    "cyan": self._colors[6],
                    "white": self._colors[7],
                },
                "bright": {
                    "black": self._colors[8],
                    "red": self._colors[9],
                    "green": self._colors[10],
                    "yellow": self._colors[11],
                    "blue": self._colors[12],
                    "magenta": self._colors[13],
                    "cyan": self._colors[14],
                    "white": self._colors[15],
                },
                "cursor": {
                    "cursor": self._cursor_background,
                    "text": self._cursor_foreground,
                },
            }
        }
        text = toml.dumps(theme_data)
        return text

    def _output_alacritty_yaml(self) -> str:
        theme_data = {
            "colors": {
                "primary": {
                    "background": self._background,
                    "foreground": self._foreground,
                },
                "normal": {
                    "black": self._colors[0],
                    "red": self._colors[1],
                    "green": self._colors[2],
                    "yellow": self._colors[3],
                    "blue": self._colors[4],
                    "magenta": self._colors[5],
                    "cyan": self._colors[6],
                    "white": self._colors[7],
                },
                "bright": {
                    "black": self._colors[8],
                    "red": self._colors[9],
                    "green": self._colors[10],
                    "yellow": self._colors[11],
                    "blue": self._colors[12],
                    "magenta": self._colors[13],
                    "cyan": self._colors[14],
                    "white": self._colors[15],
                },
                "cursor": {
                    "cursor": self._cursor_background,
                    "text": self._cursor_foreground,
                },
            }
        }
        text = yaml.dump(theme_data)
        return text

    def _output_iterm2(self) -> str:
        return ""

    def _output_xterm(self) -> str:
        return ""

    def _output_kitty(self) -> str:
        background = self._background
        foreground = self._foreground

        cursor_text = self._cursor_foreground
        cursor_cursor = self._cursor_background

        colors = self._colors

        kitty_config = f'''
background {background}
foreground {foreground}
selection_background {foreground}
selection_foreground {background}
cursor {cursor_cursor}
color0 {colors[0]}
color1 {colors[1]}
color2 {colors[2]}
color3 {colors[3]}
color4 {colors[4]}
color5 {colors[5]}
color6 {colors[6]}
color7 {colors[7]}
color8 {colors[8]}
color9 {colors[9]}
color10 {colors[10]}
color11 {colors[11]}
color12 {colors[12]}
color13 {colors[13]}
color14 {colors[14]}
color15 {colors[15]}
active_tab_foreground {colors[15]}
active_tab_background {colors[8]}
inactive_tab_foreground {colors[15]}
inactive_tab_background {colors[0]}
    '''
        return kitty_config

    def _output_windows_terminal(self) -> str:
        data = {
            "name": "Generated Theme",

            "cursorColor": self._cursor_foreground,
            "selectionBackground": self._cursor_background,

            "background": self._background,
            "foreground": self._foreground,

            "black": self._colors[0],
            "red": self._colors[1],
            "green": self._colors[2],
            "yellow": self._colors[3],
            "blue": self._colors[4],
            "purple": self._colors[5],
            "cyan": self._colors[6],
            "white": self._colors[7],

            "brightBlack": self._colors[8],
            "brightRed": self._colors[9],
            "brightGreen": self._colors[10],
            "brightYellow": self._colors[11],
            "brightBlue": self._colors[12],
            "brightPurple": self._colors[13],
            "brightCyan": self._colors[14],
            "brightWhite": self._colors[15],
        }

        text = json.dumps(data, indent=4)
        return text

class ThemeConverter:
    def __init__(self, text: str, input_type: ThemeFormat):
        self._theme = ThemeIR(text, input_type)

    def text(self, output_type: ThemeFormat):
        return self._theme.text(output_type)

def main():
    with open("example_themes/alacritty.yaml", "rb") as f:
        contents = f.read().decode(encoding='utf8')
        theme = ThemeIR(contents, ThemeFormat.ALACRITTY_YAML)
        print(theme.text(ThemeFormat.ALACRITTY_YAML))

if __name__ == '__main__':
    main()
