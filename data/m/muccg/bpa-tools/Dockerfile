FROM muccg/python-base:debian8-3.4
MAINTAINER  ccg <ccgdevops@googlegroups.com>
ENV REFRESHED_AT 2015-06-12

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
  apt-transport-https \
  tree \
  vim \
  ssh \
  lftp \
  wget \
  dos2unix \
  perl \
  rsync \
  python-pip
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install -U pip
RUN pip install sedge

COPY ./tools /tools/
COPY ./docker-entrypoint.sh  /

VOLUME /bpadownloads
VOLUME /config

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/bin/bash"]
