FROM debian:stretch
MAINTAINER Jonathan Süssemilch Poulain <jonathan@sofiero.net>

SHELL [ "/bin/bash", "-c" ]

ENV LANG=C.UTF-8 \
    base_url="http://downloads.slimdevices.com/nightly/"

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y install \
      curl \
      faad \
      flac \
      lame \
      perl \
      sox \
      wget \
      libio-socket-ssl-perl \
      libnet-ssleay-perl \
    && \
    rm -rf /var/lib/apt/lists/* && \
    curl -Lsf -o /tmp/logitechmediaserver.deb "${base_url}"$(curl -Lsf "${base_url}index.php?ver=7.9" | awk -F'"' '/_amd64.deb/ { print $2}') && \
    DEBIAN_FRONTEND=noninteractive dpkg -i /tmp/logitechmediaserver.deb && \
    rm -f /tmp/logitechmediaserver.deb

EXPOSE 3483 3483/udp 9000 9090

COPY entrypoint.sh /

ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "" ]
