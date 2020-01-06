FROM python:3.7-slim
RUN apt-get update && apt-get -y install libglib2.0 libsm6 libxext6 libxrender-dev; apt-get clean
RUN apt-get update && apt-get -y install \
    bash \
    git \
    wget \
    curl \
    postgresql-client \
    python3.7-dev \
    gettext \
    libffi-dev \
    libxslt-dev
RUN pip install opencv-contrib-python-headless psycopg2-binary

ENV EXIFTOOL_VERSION=11.65

RUN apt-get -y install perl make
RUN cd /tmp \
	&& wget http://www.sno.phy.queensu.ca/~phil/exiftool/Image-ExifTool-${EXIFTOOL_VERSION}.tar.gz \
	&& tar -zxvf Image-ExifTool-${EXIFTOOL_VERSION}.tar.gz \
	&& cd Image-ExifTool-${EXIFTOOL_VERSION} \
	&& perl Makefile.PL \
	&& make test \
	&& make install \
	&& cd .. \
	&& rm -rf Image-ExifTool-${EXIFTOOL_VERSION}

RUN pip3 install --upgrade pip
RUN pip3 install -U pip setuptools

WORKDIR /base
COPY requirements.txt /base

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
