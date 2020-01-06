FROM python:2-alpine
MAINTAINER Rija Menage <rija+dockerfiles@cinecinetique.com>

RUN apk update && \
    apk upgrade && \
    apk add --update --no-cache gcc libxml2 libxml2-dev libxslt libxslt-dev python2-dev musl-dev git wget && \

pip install future && \
pip install python-dateutil --upgrade && \
pip install pytz --upgrade && \
pip install docopt && \
pip install gitpython && \
pip install pyquery && \
pip install git+https://github.com/rija/buster && \
apk del gcc libxml2-dev libxslt-dev python2-dev musl-dev

ENTRYPOINT ["/usr/local/bin/buster"]
CMD ["generate"]

# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
	 org.label-schema.name="(Ghost) Buster Docker Container" \
	 org.label-schema.description="Generates static web pages from a locally running Ghost instance" \
	 org.label-schema.url="https://github.com/rija/buster" \
	 org.label-schema.vcs-ref=$VCS_REF \
	 org.label-schema.vcs-url="https://github.com/rija/buster" \
	 org.label-schema.vendor="Rija Menage" \
	 org.label-schema.version=$VERSION \
org.label-schema.schema-version="1.0"


