FROM alpine:3.4
MAINTAINER ryoutahirano <ryoutahirano@kozo.co.jp>

# Install packages needed to build
RUN apk add --update bash ca-certificates curl python py-pip wget \
  && pip install -U awscli \
  && rm /var/cache/apk/*