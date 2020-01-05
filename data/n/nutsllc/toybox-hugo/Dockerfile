FROM alpine:3.10

#ARG VERSION=0.53
ARG VERSION=0.59.0
ENV PACKAGE hugo_${VERSION}_Linux-64bit.tar.gz

RUN apk update && apk add \
	git\
	openssh\
	&& rm -rf /var/cache/apk/*

ADD https://github.com/gohugoio/hugo/releases/download/v${VERSION}/${PACKAGE} /tmp
RUN tar xzvf "/tmp/${PACKAGE}" hugo -C /usr/local/bin \
	&& rm -fr "/tmp/${PACKAGE}"

WORKDIR /site
#VOLUME /site

EXPOSE 1313
ENV HUGO_BASE_URL http://localhost:1313
CMD hugo server -b ${HUGO_BASE_URL} --bind=0.0.0.0
