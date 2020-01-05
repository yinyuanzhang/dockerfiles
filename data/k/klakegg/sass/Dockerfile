FROM ubuntu:17.10

RUN apt update \
 && apt install -y ruby-sass \
 && rm -r /var/lib/apt /var/lib/dpkg

VOLUME /src
VOLUME /target

WORKDIR /src
ENTRYPOINT ["sass"]

