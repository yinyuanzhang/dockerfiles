FROM ubuntu:16.04

ENV PANDOC_VERSION '1.19.2.1'

RUN apt-get update && apt-get install -y texlive && apt-get install -y wget
RUN wget https://github.com/jgm/pandoc/releases/download/${PANDOC_VERSION}/pandoc-${PANDOC_VERSION}-1-amd64.deb
RUN dpkg -i pandoc-${PANDOC_VERSION}-1-amd64.deb

CMD pandoc --help
