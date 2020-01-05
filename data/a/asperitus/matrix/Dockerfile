FROM ubuntu:bionic
LABEL maintainer="liqiang+docker@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

####
USER root
#
RUN apt-get update \
    && apt-get -y install \
        curl \
        dnsutils \
        git \
        jq \
        lsof \
        procps \
        wget

#
EXPOSE 8080

#
ENV LOGIN=vcap
ENV HOME /home/$LOGIN
ENV PATH $PATH:/opt/bin

RUN useradd -m -b /home -s /bin/bash $LOGIN

COPY ./entrypoint.sh /
COPY ./bin/ /opt/bin/

#
USER $LOGIN
ENV PORT 8080
WORKDIR /home/$LOGIN

#
ENTRYPOINT ["/entrypoint.sh"]
CMD ["matrix", "server"]

##