FROM kemixkoo/debian-maven
MAINTAINER Kemix Koo <kemix_koo@163.com>

ENV DEBIAN_FRONTEND noninteractive

USER root

# workspace home
ENV WORKSPACE_HOME /workspace
# setup workdir
WORKDIR $WORKSPACE_HOME

# add sh in workspace
ADD gitx.sh ./
RUN chmod +x ./gitx.sh

# sources home
ENV SOURCES_HOME $WORKSPACE_HOME/sources
RUN mkdir -p $SOURCES_HOME

# show current status
CMD [ -f ./gitx.sh ] && ./gitx.sh st
