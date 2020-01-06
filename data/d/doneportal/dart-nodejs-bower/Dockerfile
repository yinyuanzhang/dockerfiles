FROM node:slim

RUN npm install -g bower

ENV DART_VERSION 1.22.1

RUN apt-get -q update && apt-get install --no-install-recommends -y -q curl git ca-certificates apt-transport-https vim
RUN curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  curl https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list > /etc/apt/sources.list.d/dart_stable.list && \
  curl https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_unstable.list > /etc/apt/sources.list.d/dart_unstable.list && \
  apt-get update && \
  apt-get install dart=$DART_VERSION-1 && \
  rm -rf /var/lib/apt/lists/*

ENV DART_SDK /usr/lib/dart
ENV PATH $DART_SDK/bin:$PATH

WORKDIR /data

# Define default command.
CMD ["bash"]
