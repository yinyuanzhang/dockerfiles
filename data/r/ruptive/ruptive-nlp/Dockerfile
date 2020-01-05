FROM tiangolo/uwsgi-nginx-flask:python3.7

MAINTAINER ""

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

RUN apt-get update --fix-missing && \
    apt-get install -y wget bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 git mercurial subversion libgconf-2-4 xvfb && \
    apt-get clean

# Plotly depedencies
RUN apt-get install -y --no-install-recommends \
        wget \
        xvfb \
        libgtk2.0-0 \
        libxtst6 \
        libxss1 \
        libgconf-2-4 \
        libnss3 \
        libasound2 && \
     mkdir -p /home/orca && \
     cd /home/orca && \
     wget https://github.com/plotly/orca/releases/download/v1.2.1/orca-1.2.1-x86_64.AppImage && \
     chmod +x orca-1.2.1-x86_64.AppImage && \
     ./orca-1.2.1-x86_64.AppImage --appimage-extract && \
     printf '#!/bin/bash \nxvfb-run --auto-servernum --server-args "-screen 0 640x480x24" /home/orca/squashfs-root/app/orca "$@"' > /usr/bin/orca && \
     chmod +x /usr/bin/orca

RUN pip install --upgrade pip

RUN pip install --no-cache-dir Cython \
    && pip install pybind11

RUN pip install -U azure-storage-blob

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

RUN python -m spacy download en_trf_bertbaseuncased_lg

ENV LISTEN_PORT 5050
ENV LISTEN_PORT 8080

EXPOSE 5050
EXPOSE 8080

COPY ./app /app

ENV STATIC_PATH /app/app/api/resources/static

# Increase Timeout 600 seconds = 10 minutes
# Timeout 1200 seconds = 20 minutes
RUN echo "uwsgi_read_timeout 600s;" > /etc/nginx/conf.d/custom_timeout.conf

# ENTRYPOINT [ "python" ]

# CMD [ "main.py" ]
