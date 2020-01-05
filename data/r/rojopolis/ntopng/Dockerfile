FROM debian:9
LABEL maintainer="Robert Jordan <rojopolis@deba.cl>"

ADD http://apt-stable.ntop.org/stretch/all/apt-ntop-stable.deb apt-ntop-stable.deb
RUN apt-get update && \
    apt-get install -y ./apt-ntop-stable.deb && \
    apt-get update && \
    apt-get install -y ntopng && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* apt-ntop-stable.deb

EXPOSE 3000
ENTRYPOINT [ "/usr/local/bin/ntopng" ]