FROM alpine:3.7 as build

LABEL maintainer="Pavel Volkovitskiy <olfway@olfway.net>"

ENV DANTE_VERSION 1.4.2
ENV DANTE_URL https://www.inet.no/dante/files/dante-$DANTE_VERSION.tar.gz
ENV DANTE_SHA baa25750633a7f9f37467ee43afdf7a95c80274394eddd7dcd4e1542aa75caad

ENV PAM_PWDFILE_VERSION 1.0
ENV PAM_PWDFILE_URL https://github.com/tiwe-de/libpam-pwdfile/archive/v$PAM_PWDFILE_VERSION.tar.gz
ENV PAM_PWDFILE_SHA 5b8db1397cff9cadfd1bb96f53c134b787ab0e6a0fbedb71040541d340313ba2

RUN set -x \
  && apk add --no-cache \
    automake \
    curl \
    g++ \
    gcc \
    linux-pam-dev \
    make

RUN set -x \
  && curl -sSL $DANTE_URL -o dante-$DANTE_VERSION.tar.gz \
  && sha256sum "dante-$DANTE_VERSION.tar.gz" \
  && echo "$DANTE_SHA *dante-$DANTE_VERSION.tar.gz" | sha256sum -c \
  && tar xzf dante-$DANTE_VERSION.tar.gz

RUN set -x \
  && cd dante-$DANTE_VERSION \
  && export ac_cv_func_sched_setscheduler=no \
  && cp -v /usr/share/automake-*/config.guess . \
  && ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --localstatedir=/var \
    --disable-client \
  && make -j \
  && make install DESTDIR=/image

RUN set -x \
  && curl -sSL $PAM_PWDFILE_URL -o libpam-pwdfile-$PAM_PWDFILE_VERSION.tar.gz \
  && sha256sum "libpam-pwdfile-$PAM_PWDFILE_VERSION.tar.gz" \
  && echo "$PAM_PWDFILE_SHA *libpam-pwdfile-$PAM_PWDFILE_VERSION.tar.gz" | sha256sum -c \
  && tar xzf libpam-pwdfile-$PAM_PWDFILE_VERSION.tar.gz

RUN set -x \
  && cd libpam-pwdfile-$PAM_PWDFILE_VERSION \
  && make -j \
  && make install DESTDIR=/image

CMD /bin/bash

FROM alpine:3.7 as runtime

RUN set -x \
  && apk add --no-cache \
    apg \
    bash \
    linux-pam

COPY --from=build /image/ /

COPY files/dante.pam /etc/pam.d/sockd
COPY files/dante.conf.tmpl /usr/share/dante/

COPY scripts/ /scripts/

CMD /scripts/dante-start
