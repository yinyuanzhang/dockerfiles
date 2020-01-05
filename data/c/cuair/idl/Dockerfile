FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y sudo gnupg protobuf-compiler \
    && mkdir idl

COPY . idl/

CMD ["/bin/bash", "-c", "while true; do sleep 1000; done"]
