FROM google/dart:1.15.0

RUN set -ex


RUN pub global activate tuneup
RUN apt-get update && apt-get install -y openssh-client

env PATH ~/.pub-cache/bin:$PATH
