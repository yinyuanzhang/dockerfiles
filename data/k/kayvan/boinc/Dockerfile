# Alpine based docker container
# for https://boinc.berkeley.edu
#
# Based on https://boinc.berkeley.edu/trac/wiki/SoftwareBuilding

FROM alpine:3.6

LABEL maintainer "Kayvan Sylvan <kayvansylvan@gmail.com>"

ENV CLIENT_VERSION client_release/7.8/7.8.3
ENV CLIENT_DIR boinc-client_release-7.8-7.8.3

ADD https://github.com/BOINC/boinc/archive/${CLIENT_VERSION}.tar.gz /root
WORKDIR /root

RUN if [ ! -d ${CLIENT_DIR} ]; then tar xvzf *.tar.gz; fi \
  && cd /root/${CLIENT_DIR} \
  && apk --no-cache add \
    libtool g++ openssl-dev make m4 libtool autoconf \
    automake curl-dev libnotify-dev file \
  && ./_autosetup \
  && ./configure CXXFLAGS="-O3 " --disable-server \
  && make install && cd .. && rm -rf ${CLIENT_DIR} *.tar.gz

ENTRYPOINT [ "/usr/local/bin/boinc_client" ]
