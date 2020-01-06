FROM ubuntu:18.04
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG='C.UTF-8' LANGUAGE='C.UTF-8' LC_ALL='C.UTF-8'

# Add s6 script

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.22.1.0/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /

# Copy S6 init scripts

COPY s6/ /etc

# Add necessary packages

RUN apt-get update && apt install -y tzdata

EXPOSE 22
ENTRYPOINT ["/init"]
