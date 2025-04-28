# termcolors.dev

A website that contains more than 300 cross platform terminal color themes.

## Setup

To run this project you'll need these four programs:

- python
- poetry
- node
- npm

First clone the repository, then run `poetry install --no-root`.
After poetry is done installing packages you can run these commands:

- `./mg migrate` - sets up the database schema
- `./mg tailwind install` - installs tailwind using django-tailwind.
- `./mg downloadthemes` - installs a list of themes from the internet.
- `./mg importthemes` - parses and imports those themes into the sqlite database.

Then once you are ready to develop you can run these to commands:
`./mg runserver` and `./mg tailwind start`

You have to run both commands at the same time.
I normally use tmux so I can run them with a split screen.

## Thanks

- [Joshua Hicks](https://github.com/Hicks-Josh) - for helping with colors and testing.
