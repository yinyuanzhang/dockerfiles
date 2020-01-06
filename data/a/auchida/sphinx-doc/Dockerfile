FROM debian:jessie
MAINTAINER Akihiro Uchida <uchida@turbare.net>
RUN apt-get update\
 && apt-get install -y --no-install-recommends python-pip make\
 && rm -rf /var/lib/apt/lists/*
RUN pip install Sphinx recommonmark\
 && mkdir -p /opt/docs
RUN apt-get update\
 && apt-get install -y --no-install-recommends texlive-latex-recommended\
 && apt-get install -y --no-install-recommends texlive-fonts-recommended\
 && apt-get install -y --no-install-recommends texlive-latex-extra\
 && apt-get install -y --no-install-recommends texlive-lang-japanese\
 && apt-get install -y --no-install-recommends dvipng\
 && rm -rf /var/lib/apt/lists/*
RUN apt-get update\
 && apt-get install -y --no-install-recommends graphviz\
 && rm -rf /var/lib/apt/lists/*
WORKDIR /opt/docs
CMD ["/bin/bash"]
