FROM debian:9.8-slim

ENV HORIZON_VERSION 0.17.3

EXPOSE 8000

ADD install /
RUN /install

ADD start /

CMD ["/start"]
