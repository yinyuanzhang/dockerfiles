FROM python:3.7.2-alpine3.9

RUN set -x \
 && apk --update upgrade \
 && apk --no-cache add freetype-dev libpng-dev \
 && apk --no-cache add alpine-sdk \
 && ln -s /usr/include/locale.h /usr/include/xlocale.h \
 && pip --no-cache-dir install matplotlib==3.0.3 \
 && apk del --purge alpine-sdk \
 && apk --no-cache add libstdc++ \
 && rm -fr /root/.cache/
