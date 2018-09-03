#!/bin/bash
# $0 is a script name, $1, $2, $3 etc are passed arguments
# $1 is our command
# Credits: https://rock-it.pl/how-to-write-excellent-dockerfiles/
CMD=$1

wait_for_db () {
    # Wait until postgres is ready
    until nc -z db 5432; do
        echo "$(date) - waiting for postgres... (db:5432)"
        sleep 3
    done
}

case "$CMD" in
    "runserver" )
        wait_for_db

        pipenv run ./src/manage.py migrate --noinput
        pipenv run ./src/manage.py runserver 0.0.0.0:8000
        ;;

    "celery_worker" )
        wait_for_db

        cd src && pipenv run celery -A screenshotr worker -l info
        ;;

    * )
        exec $CMD ${@:2}
        ;;
esac