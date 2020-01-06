FROM ubuntu:bionic
LABEL maintainer="azyqxt6gzrtd@streaky.me"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y dist-upgrade && apt-get -y --purge autoremove
RUN apt-get -y install python3-pip python3-dev python3-venv gcc libyaml-dev libev-dev git nginx cron
RUN git clone --single-branch -b master https://github.com/amonapp/amon.git /opt/amon 

ADD ./build /build

RUN /build/amon.sh
RUN /build/clean.sh

EXPOSE 80
VOLUME ["/var/log/amon", "/etc/opt/amon"]

WORKDIR /opt/amon
ENTRYPOINT ["/entrypoint"]
CMD ["server"]
