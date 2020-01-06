FROM quay.io/swatrider/alpine-java8:latest

ADD . /graphhopper

WORKDIR /graphhopper

ENTRYPOINT /graphhopper/run.sh surface

EXPOSE 8989
