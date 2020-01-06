FROM alpine:3.9

ENV EV_EXTRA_DEFS -DEV_NO_ATFORK
COPY cpanfile /
RUN apk update && \
  apk add perl perl-io-socket-ssl perl-dbd-mysql perl-dbi perl-dev g++ make curl wget && \
  curl -L https://cpanmin.us | perl - App::cpanminus && \
  cpanm --installdeps . -M https://cpan.metacpan.org && \
  apk del perl-dev g++ make wget curl && \
  rm -rf /root/.cpanm/* /usr/local/share/man/*
