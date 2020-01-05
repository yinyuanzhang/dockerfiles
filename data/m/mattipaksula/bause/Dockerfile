FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
  curl

WORKDIR /
COPY bause.sh .

ENTRYPOINT [ "/bause.sh" ]
