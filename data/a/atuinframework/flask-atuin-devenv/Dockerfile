# vim:set ft=dockerfile:

# LOCAL DEVELOPMENT

FROM python:3

LABEL maintainer="Paolo Casciello <paolo.casciello@scalebox.it>"

RUN apt-get update && apt-get install -y \
    libxml2-dev \
    libxslt1-dev

RUN mkdir -vp /var/wsgi

COPY ./requirements.txt /var/wsgi/

RUN mkdir -vp /var/wsgi-commands

COPY ./start.sh /var/wsgi-commands

WORKDIR /var/wsgi

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["/var/wsgi-commands/start.sh"]
