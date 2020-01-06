FROM python:3.5
MAINTAINER Hudson Brendon <contato.hudsonbrendon@gmail.com>
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/

COPY .bowerrc /root/.bowerrc

RUN apt-get update

RUN apt-get install -y build-essential \
    git-core \
    python-dev \
    ruby-full \
    nodejs-legacy \
    npm

RUN npm install -g bower \
    grunt \
    grunt-cli \
    less

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ADD . /code/

EXPOSE 8000
