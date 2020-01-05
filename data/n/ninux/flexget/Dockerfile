FROM python:2.7
MAINTAINER nicolas.bonaldi@gmail.com

#requirements
RUN pip install -I flexget

RUN mkdir /app \
  && mkdir -p /root/.flexget \
  && mkdir /download

ADD config.ori.yml /app/config.ori.yml
ADD init /app/init
RUN chmod 755 /app/init

VOLUME ["/download"]
VOLUME ["/root/.flexget"]

ENTRYPOINT ["/app/init"]
CMD ["app:start"]
