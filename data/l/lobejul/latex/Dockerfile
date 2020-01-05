FROM ubuntu:18.10

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Berlin

RUN mkdir /code
WORKDIR /code

RUN apt-get update && \
    apt-get install -y texlive texlive-binaries texinfo lmodern wget texlive-xetex texlive-fonts-extra ttf-ubuntu-font-family fonts-liberation

RUN wget http://mirrors.ctan.org/macros/latex/contrib/moderncv.zip && \
    unzip moderncv.zip && \
    mkdir -p ~/texmf/tex/latex && \
    mv moderncv/ ~/texmf/tex/latex/

RUN texhash ~/texmf/
