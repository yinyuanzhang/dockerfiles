FROM tensorflow/tensorflow:latest-gpu-py3

RUN apt-get -y update -qq && apt-get install -y \
    build-essential \
    python3-dev \
    python3-pip \
    python-opencv \
    libpcre3 \
    libpcre3-dev \
    postgresql-client \
    git \
    uwsgi

ENV PYTHONBUFFERED 1
RUN pip install --no-cache-dir poetry && \
    poetry config settings.virtualenvs.create false

COPY *.toml /
RUN poetry update --no-interaction --no-ansi

WORKDIR /uwsgi-plugins
RUN uwsgi --build-plugin https://github.com/Datadog/uwsgi-dogstatsd

WORKDIR /app
ENV PYTHONPATH /app
ENV PYTHONWARNINGS ignore
CMD uwsgi --plugin-dir /uwsgi-plugins --ini uwsgi.ini --uid www-data --gid www-data
