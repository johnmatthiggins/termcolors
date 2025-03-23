#!/usr/bin/env python
import tomllib as toml

def main():
    with open("cobalt.toml", "rb") as f:
        data = toml.load(f)
        print(data)


if __name__ == '__main__':
    main()
