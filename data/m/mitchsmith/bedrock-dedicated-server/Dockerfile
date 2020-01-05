FROM ubuntu:latest

ARG BEDROCK_URL=https://minecraft.azureedge.net/bin-linux/bedrock-server-1.14.1.4.zip

RUN apt-get -y update
RUN apt-get -y install wget &&\
    apt-get -y install libssl1.0.0 &&\
    apt-get -y install unzip &&\
    apt-get -y install libcurl4

# get the files in put them under .. was going to say /opt but probably can't. Needs to go in working directory.

# could try: https://github.com/Switchbladed/TeamSpeak3-GAME/blob/master/Dockerfile
RUN mkdir /data &&\
    wget ${BEDROCK_URL} -O /opt/bedrock.zip &&\
    unzip /opt/bedrock.zip -d /data &&\
    chmod +x /data/bedrock_server

ENV LD_LIBRARY_PATH=/data

# Entry
COPY ./start_bedrock.sh /opt
RUN ["chmod", "+x", "/opt/start_bedrock.sh"]

RUN useradd -r docker
RUN chown -R docker:docker /data
USER docker:docker
