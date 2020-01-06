FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get upgrade -y && apt-get -y install gettext
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
