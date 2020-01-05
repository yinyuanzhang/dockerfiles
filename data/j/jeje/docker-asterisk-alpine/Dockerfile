FROM andrius/asterisk:latest

MAINTAINER jerome.bernard@gmail.com

RUN apk add --update asterisk-sounds-en asterisk-mobile asterisk-dahdi dahdi-linux \
&&  rm -rf /var/cache/apk/*

RUN mkdir -p /var/lib/asterisk/sounds/fr && cd /var/lib/asterisk/sounds/fr \
&& wget http://downloads.asterisk.org/pub/telephony/sounds/asterisk-core-sounds-fr-gsm-current.tar.gz \
&& tar xvzf asterisk-core-sounds-fr-gsm-current.tar.gz \
&& rm asterisk-core-sounds-fr-gsm-current.tar.gz \
&& chown -R asterisk:117 /var/lib/asterisk/sounds/fr \
&& find /var/lib/asterisk/sounds/fr -type d -exec chmod 0775 {} \;
