FROM jenkinsci/slave
LABEL maintainer="richie.mackay@gmail.com"
USER root
RUN apt-get update && \
  apt-get install sudo -y && \
  apt-get install -y curl && \
  curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - && \
  apt-get install -y nodejs
RUN apt-get install -y npm
USER jenkins