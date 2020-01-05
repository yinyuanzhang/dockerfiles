FROM debian:stretch-slim
MAINTAINER Alessandro Lattao <alessandro.lattao@brumbrum.it>

ENV DEBIAN_FRONTEND noninteractive
ENV TZ=Europe/Rome

# Aggiungo il demone xray
# https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html
ADD https://s3.dualstack.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-2.x.deb /tmp

RUN \
  apt-get update && \
  apt-get -y --no-install-recommends install locales apt-utils curl && \
  echo "it_IT.UTF-8 UTF-8" >> /etc/locale.gen && \
  ln -sf /etc/locale.alias /usr/share/locale/locale.alias && \
  locale-gen it_IT.UTF-8 && \
  /usr/sbin/update-locale LANG=it_IT.UTF-8 && \
  apt-get -y upgrade && \
  apt-get -y --no-install-recommends install ca-certificates zip unzip git python3 python3-setuptools python3-pip jq && \
  dpkg -i /tmp/aws-xray-daemon-2.x.deb && \
  rm /tmp/aws-xray-daemon-2.x.deb && \
  pip3 install awscli && \
  apt-get -y purge python3-setuptools python3-pip && \
  apt-get -y autoclean && \
  apt-get -y clean && \
  apt-get -y autoremove

ENV LC_ALL it_IT.UTF-8
ENV LANGUAGE it_IT

# Aggiungo gli script pre e post entrypoint
COPY entrypoint.pre-run.d/* /entrypoint.pre-run.d/
COPY entrypoint.post-run.d/* /entrypoint.post-run.d/
COPY bin/read_aws_ssm_parameters.sh /bin/read_aws_ssm_parameters.sh

# Do il permesso di esecuzione sui file altrimenti run-parts non li avvia
RUN \
  chmod +x /entrypoint.pre-run.d/* && \
  chmod +x /entrypoint.post-run.d/*

# Define working directory.
WORKDIR /data
