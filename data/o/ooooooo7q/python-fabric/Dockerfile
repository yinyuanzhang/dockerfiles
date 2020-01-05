FROM ubuntu:16.04
RUN apt-get update \
    && apt-get install -y python python-pip git unzip zip curl language-pack-ja \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip==9.0.3 \
    && pip install backports.tempfile 'fabric==1.14.0' jinja2 requests

ENV PYTHONIOENCODING=UTF-8
ENV LANG=ja_JP.UTF-8

CMD ["fab", "-l"]