# Start with miniconda image
FROM continuumio/miniconda3
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update
RUN apt-get install graphviz libgraphviz-dev pkg-config -y
RUN apt-get install libreoffice -y