FROM debian:buster-slim
LABEL maintainer="ryan@devenvy.com"

ENV FAH_VERSION_MINOR=7.5.1
ENV FAH_VERSION_MAJOR=7.5
ENV DEBIAN_FRONTEND=noninteractive

ENV FAH_TEAM=223518
ENV FAH_USER=Anonymous
ENV FAH_SMP=true
ENV FAH_POWER=full
ENV FAH_GPU=false
ENV FAH_PASSKEY=

# limit calls to apt + fah by combining into initial RUN
RUN apt-get update && \
    apt-get install --no-install-recommends -y curl bzip2 &&\
    curl --insecure https://download.foldingathome.org/releases/public/release/fahclient/debian-stable-64bit/v${FAH_VERSION_MAJOR}/fahclient_${FAH_VERSION_MINOR}_amd64.deb -o /tmp/fah.deb
    
# set config placeholder, install and cleanup
RUN mkdir -p /etc/fahclient/ &&\
    touch /etc/fahclient/config.xml &&\
    dpkg -i /tmp/fah.deb &&\
    apt remove -y curl &&\
    apt autoremove -y &&\
    rm --recursive --verbose --force /tmp/* /var/log/* /var/lib/apt/

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 7396
EXPOSE 36330
ENTRYPOINT ["/entrypoint.sh"]
