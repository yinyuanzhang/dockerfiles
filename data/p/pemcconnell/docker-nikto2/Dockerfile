FROM alpine:3.5
MAINTAINER Peter McConnell <me@petermcconnell.com>

RUN apk upgrade && \
	apk add --update \
	  git \
	  perl \
      perl-net-ssleay \
	  ca-certificates

RUN git clone https://github.com/sullo/nikto.git /nikto

ENTRYPOINT ["/nikto/program/nikto.pl"]
