FROM docker.io/ubuntu

RUN apt-get update && \
    apt-get install -y libcurl4-openssl-dev

RUN mkdir /minecraft
VOLUME /minecraft
WORKDIR /minecraft

RUN addgroup --gid 543 minecraft
RUN adduser --uid 543 --gid 543 --gecos "" --disabled-password minecraft
USER minecraft:minecraft

EXPOSE 19132/tcp
ENV LD_LIBRARY_PATH /minecraft

ENTRYPOINT /minecraft/bedrock_server
