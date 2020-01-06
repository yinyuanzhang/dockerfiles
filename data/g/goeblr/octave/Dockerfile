FROM ubuntu:18.10
MAINTAINER r.goebl@tum.de

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get install less
ADD install.sh install.sh
RUN sh ./install.sh && rm install.sh

#VOLUME ["/source"]
#ENTRYPOINT ["octave"]
