#!/usr/bin/env sh
DIR=$(dirname $0)
cd $DIR

if echo "$@" | grep -q production; then
        echo "RUNNING IN PRODUCTION MODE...";
	export DEBUG=0;
        export POETRY="poetry"
        if ! which poetry | grep -q poetry; then
            export POETRY="/home/ubuntu/.local/bin/poetry"
        fi

        $POETRY run uvicorn \
            --port 8010 \
            --host 127.0.0.1 \
            --workers 4 termcolors.asgi:application
else
	export DEBUG=1;
	/home/ubuntu/.local/bin/poetry run python manage.py runserver
fi
