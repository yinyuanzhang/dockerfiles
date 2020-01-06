FROM alpine
MAINTAINER Jimmy Koo<kukkiz@gmail.com>

RUN apk update
RUN apk add python python-dev py-pip build-base
RUN apk add aria2
RUN pip install requests
RUN pip install bypy
RUN mkdir /bypy

VOLUME ["/bypy"]

COPY bypy-daemon.sh /

CMD /bypy-daemon.sh
