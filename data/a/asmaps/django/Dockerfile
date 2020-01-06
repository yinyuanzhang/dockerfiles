FROM asmaps/ubuntu
MAINTAINER asmaps

RUN apt-get update && apt-get install -y \
    lib32z1-dev \
    libfreetype6-dev \
    libjpeg8-dev \
    libxml2-dev \
    libxslt1-dev \
    postgresql-client \
    postgresql-server-dev-all \
    python-virtualenv \
    python3-pip \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

RUN easy_install3 -U "pip<8.0"
RUN pip3 install psycopg2 Pillow

ONBUILD ADD requirements.txt /opt/code/requirements.txt
ONBUILD WORKDIR /opt/code
ONBUILD RUN pip3 install -Ur requirements.txt

ONBUILD ADD . /opt/code
ONBUILD WORKDIR /opt/code
ONBUILD USER uid1000
