FROM python:2.7

RUN mkdir /src
WORKDIR /src

ADD . /src/labman_ud

WORKDIR /src/labman_ud

RUN apt-get update
RUN apt-get -y install graphviz python-dev libgraphviz-dev

RUN pip2 install -U pip
RUN pip2 install -r requirements.txt

EXPOSE 8000

RUN mkdir /src/labman_ud/labman_ud/media
VOLUME /src/labman_ud/labman_ud/media

WORKDIR /
RUN git clone https://github.com/vishnubob/wait-for-it

ENTRYPOINT ["/src/labman_ud/entrypoint.sh"]
