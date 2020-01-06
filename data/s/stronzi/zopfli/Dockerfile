FROM alpine
LABEL maintainer="Yanis Benson <yanis.benson@gmail.com>"
ENV ZOPFLI_VERSION=1.0.2
RUN apk update && apk upgrade && apk add --no-cache build-base libstdc++
RUN cd /tmp &&\
	wget -q https://github.com/google/zopfli/archive/zopfli-${ZOPFLI_VERSION}.tar.gz -O - | tar -xvzp && cd zopfli-* &&\
	make zopfli zopflipng && mv zopfli zopflipng /usr/local/bin/ &&\
	rm -rf /tmp/zopfli-zopfli-${ZOPFLI_VERSION} &&\
	apk del build-base
