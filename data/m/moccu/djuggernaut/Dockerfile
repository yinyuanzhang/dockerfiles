FROM python:3.6-slim

LABEL com.moccu.type="djuggernaut" \
    com.moccu.version.python="${PYTHON_VERSION}"

# Some basic stuff
RUN apt-get -qq update && apt-get -qq install -y --no-install-recommends \
        git \
        curl \
        bzip2 \
        locales \
        gettext \
        gcc \
        libpq-dev \
        libjpeg62-turbo-dev \
        graphicsmagick \
    && rm -rf /var/lib/apt/lists/*


RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
    && locale-gen \
    && update-locale LANG=en_US.UTF-8

ADD mime.types /etc/mime.types

CMD ["bash"]
