FROM cibuilds/hugo
LABEL maintainer="Okky Hendriansyah <okky.htf@gmail.com>"
ENV ZOPFLI_RELEASE=1.0.2
RUN true \
 && set -xe \
 && apk update --no-cache \
 && apk add --no-cache build-base curl yarn \
 && cd /tmp \
 && curl -LO https://github.com/google/zopfli/archive/zopfli-${ZOPFLI_RELEASE}.tar.gz \
 && tar xvvzpf zopfli-${ZOPFLI_RELEASE}.tar.gz \
 && cd zopfli-zopfli-${ZOPFLI_RELEASE} \
 && make zopfli \
 && make zopflipng \
 && mv zopfli /usr/local/bin/ \
 && mv zopflipng /usr/local/bin/ \
 && cd /tmp \
 && rm zopfli-${ZOPFLI_RELEASE}.tar.gz \
 && rm -Rf zopfli-zopfli-${ZOPFLI_RELEASE} 
