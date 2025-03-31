#!/usr/bin/env sh
poetry install --no-root
echo yes | poetry run python manage.py collectstatic
sudo systemctl restart termcolors.dev.service
