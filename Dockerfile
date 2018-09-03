FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

ADD Pipfile /app/
ADD Pipfile.lock /app/
ADD "docker-entrypoint.sh" /app/

RUN apt-get update && apt-get install -y netcat wkhtmltopdf xvfb

RUN pip install pipenv
RUN pipenv install

EXPOSE 8000

CMD ["runserver"]
ENTRYPOINT ["./docker-entrypoint.sh"]
