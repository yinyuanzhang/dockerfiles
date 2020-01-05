FROM ubuntu:12.04

# install necessary dependencies
RUN apt-get update && \
    apt-get install -y wget python-dev

WORKDIR /opt
RUN mkdir modeller
WORKDIR /opt/modeller
RUN wget --no-check-certificate https://salilab.org/modeller/9.20/modeller_9.20-1_amd64.deb
RUN env KEY_MODELLER=MODELIRANJE dpkg -i /opt/modeller/modeller_9.20-1_amd64.deb

COPY wrapper.sh /opt/modeller

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/modeller/wrapper.sh"]
