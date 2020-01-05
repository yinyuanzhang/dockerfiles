FROM myforexidea/mt4-compiler
LABEL maintainer="araran <araitomonori@gmail.com>"

USER root

COPY install-gosu.sh /usr/local/bin/install-gosu.sh
RUN chmod +x /usr/local/bin/install-gosu.sh
RUN /usr/local/bin/install-gosu.sh

RUN apt-get update && apt-get upgrade -y \
 && apt-get install -y python3
