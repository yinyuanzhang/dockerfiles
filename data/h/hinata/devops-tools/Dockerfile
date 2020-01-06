#@# vim: set filetype=dockerfile:
FROM docker:19.03.5-git
MAINTAINER Takahiro INOUE <takahiro.inoue@mail.3dcg-arts.net>

WORKDIR /tmp

ADD requirements.txt .

RUN apk add --no-cache --update \
  alpine-sdk                    \
  gettext                       \
  libffi                        \
  libffi-dev                    \
  openssl                       \
  openssl-dev                   \
  python3                       \
  python3-dev

RUN pip3 install -r requirements.txt

WORKDIR /

RUN find /root | grep -v /root$ | xargs rm -fr && \
    find /tmp  | grep -v /tmp$  | xargs rm -fr
