# docker build --pull --force-rm --rm -t dev0004:5000/library/webtester .
# docker push dev0004:5000/libray/webtester
FROM ubuntu:latest
MAINTAINER "Marc Wäckerlin"

RUN apt-get install -y wget software-properties-common apt-transport-https
RUN apt-add-repository https://dev.marc.waeckerlin.org/repository
RUN wget -O- https://dev.marc.waeckerlin.org/repository/PublicKey | apt-key add -
RUN apt-get update -y
RUN apt-get install -y xvfb webtester

ADD runtests.sh runtests.sh

VOLUME /tests

WORKDIR /tests
CMD /runtests.sh
