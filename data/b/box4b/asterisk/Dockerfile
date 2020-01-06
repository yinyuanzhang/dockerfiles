FROM alpine:edge as builder

RUN apk add --update --no-cache alpine-sdk
RUN mkdir /build
WORKDIR /build
RUN git init
COPY asterisk/ .
RUN adduser -D -g "" dev
RUN adduser dev abuild
RUN chmod 777 /var/cache/distfiles/
RUN chown dev:dev /build
RUN su dev -c 'abuild-keygen -a -n'
RUN su dev -c 'abuild checksum'
RUN apk update
RUN su dev -c 'abuild -r'

FROM alpine:edge

WORKDIR /

COPY --from=builder /home/dev/packages/x86_64/asterisk-16.3.0-r0.apk .
RUN apk add --allow-untrusted asterisk-16.3.0-r0.apk
RUN apk update \
&& apk upgrade \
&& apk add asterisk-sounds-moh \
&& apk add asterisk-srtp \
&& apk add asterisk-cdr-mysql

# RUN mkdir -p /var/lib/asterisk/sounds/fr
# WORKDIR /var/lib/asterisk/sounds/fr
# RUN wget -O core.zip https://www.asterisksounds.org/fr-fr/download/asterisk-sounds-core-fr-FR-sln16.zip \
# 	&& wget -O extra.zip https://www.asterisksounds.org/fr-fr/download/asterisk-sounds-extra-fr-FR-sln16.zip \
# 	&& unzip -oq core.zip \
# 	&& unzip -oq extra.zip \
# 	&& chown -R asterisk /var/lib/asterisk/sounds/fr \
# 	&& find /var/lib/asterisk/sounds/fr -type d -exec chmod 0775 {} \;

EXPOSE 5038 5065/udp 10000-20000/udp

WORKDIR /etc/asterisk

VOLUME /etc/asterisk /var/lib/asterisk/sounds /var/log/asterisk

CMD [ "/usr/sbin/asterisk", "-vvvvvvvdf" ]
