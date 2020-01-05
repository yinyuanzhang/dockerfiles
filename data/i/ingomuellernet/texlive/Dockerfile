FROM ubuntu:bionic
MAINTAINER Ingo Müller <ingo.mueller@inf.ethz.ch>

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        software-properties-common && \
    add-apt-repository -y ppa:jonathonf/texlive

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        make \
        texlive-full=2019* \
        python3-matplotlib \
        python3-nose \
        python3-numpy \
        python3-pandas \
        python3-pygments \
        python3-scipy \
        python3-sympy \
        python3-seaborn \
        latexmk \
        biber \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
