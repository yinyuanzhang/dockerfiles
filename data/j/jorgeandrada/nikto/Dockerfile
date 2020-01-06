FROM alpine:3.8 AS build

RUN apk add --no-cache git
RUN git clone https://github.com/sullo/nikto

FROM alpine:3.8

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
			org.label-schema.name="nikto" \
			org.label-schema.description="Nikto with curl" \
			org.label-schema.url="http://andradaprieto.es" \
			org.label-schema.vcs-ref=$VCS_REF \
			org.label-schema.vcs-url="https://github.com/jandradap/nikto" \
			org.label-schema.vendor="Jorge Andrada Prieto" \
			org.label-schema.version=$VERSION \
			org.label-schema.schema-version="1.0" \
			maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \
			org.label-schema.docker.cmd="docker run --rm -it -v $PWD/output:/tmp/nikto jorgeandrada/nikto -host www.example.org -p 443 -ssl -Format htm -output /tmp/nikto/example.html"


COPY --from=build /nikto /nikto

RUN apk --update --clean-protected --no-cache add \
  openssl \
  perl \
  perl-net-ssleay \
  curl

ENV PATH /nikto/program:$PATH

WORKDIR /nikto/program

# ENTRYPOINT ["nikto.pl"]
