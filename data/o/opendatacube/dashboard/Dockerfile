FROM opendatacube/datacube-core:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3-fiona \
    python3-shapely \
    libpng-dev \
    wget \
    vim \
    unzip \
    postgresql-client \
    jq \
    awscli \
    curl \
    libev-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip first: pip3 install --upgrade pip.
RUN pip3 install --upgrade pip \
    && rm -rf $HOME/.cache/pip

RUN pip3 install gunicorn flask pyorbital colorama sentry-sdk[flask] raven \
    && rm -rf $HOME/.cache/pip

WORKDIR /code
RUN mkdir /code/product-summaries

ADD . .

RUN pip3 install .[deployment]

CMD gunicorn -b '0.0.0.0:8080' -w 1 '--worker-class=egg:meinheld#gunicorn_worker'  --timeout 60 cubedash:app
