FROM debian:stretch
MAINTAINER SFoxDev <admin@sfoxdev.com>

ENV DEBIAN_FRONTEND=noninteractive \
    LC_ALL=C.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 

RUN apt-get update \
    && apt-get install -y pdftk mc\
    && apt-get clean autoclean \
    && apt-get autoremove --yes \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && mkdir /input \
    && mkdir /output 

VOLUME ["/input","/output"]

ENTRYPOINT ["/usr/bin/pdftk"]

#CMD ["/bin/bash"]
