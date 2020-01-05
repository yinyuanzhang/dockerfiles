FROM ubuntu:14.04
MAINTAINER Shisei Hanai<ruimo.uno@gmail.com>

RUN apt-get update
RUN apt-get -y install python3-pip libpq-dev
RUN pip3 install psycopg2
RUN pip3 install Django==1.7.4

RUN django-admin startproject hello

EXPOSE 6502

ADD profile /profile

ENTRYPOINT ["python3"]
CMD ["hello/manage.py", "runserver", "0.0.0.0:6502"]
