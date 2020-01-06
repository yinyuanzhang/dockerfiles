# Download from docker cloud of teatime(public)
FROM teatime/docker-img-django:latest

RUN groupadd -r django && useradd -r -g django django

ADD . /code
RUN chown -R django /code

WORKDIR /code
