FROM quay.io/swatrider/alpine-java8:latest

ADD . /graphhopper

WORKDIR /graphhopper

ENTRYPOINT /graphhopper/run.sh full

EXPOSE 8899
