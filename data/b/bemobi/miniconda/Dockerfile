FROM ubuntu:14.04
MAINTAINER Rafael Martins "rafael.martins@bemobi.com.br"

ENV JAVA_VERSION 7u71

# utility tools
RUN apt-get update -qq \
    && apt-get install -q -y aria2 build-essential python-dev freetds-dev \
                             openjdk-7-jre-headless="$JAVA_VERSION"* \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# miniconda
RUN aria2c http://repo.continuum.io/miniconda/Miniconda-3.7.0-Linux-x86_64.sh \
    && bash Miniconda-3.7.0-Linux-x86_64.sh -b -f \
    && rm -f Miniconda-3.7.0-Linux-x86_64.sh
ENV PATH /root/miniconda/bin:$PATH

# python packages
RUN conda install --yes pip numpy matplotlib pandas \
    && pip install ipython ipdb gevent geventhttpclient flask docopt sqlalchemy pymssql
