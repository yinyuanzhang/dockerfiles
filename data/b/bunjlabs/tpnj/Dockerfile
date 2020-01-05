FROM bunjlabs/texlive2016:lite
MAINTAINER Artem Shurygin <show.vars@gmail.com>

ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

ADD https://deb.nodesource.com/setup_7.x setup_7.x
RUN bash setup_7.x && apt-get update && apt-get install -y nodejs

ADD https://github.com/jgm/pandoc/releases/download/1.18/pandoc-1.18-1-amd64.deb pandoc.deb
RUN dpkg -i pandoc.deb
