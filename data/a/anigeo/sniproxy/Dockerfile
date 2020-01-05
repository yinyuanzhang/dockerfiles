FROM alpine:latest

ADD sniproxy.conf /etc/sniproxy.conf

RUN set -ex \
	&& apk upgrade --no-cache \
	&& apk add --no-cache \
		udns \
		libev \
		pcre \
	&& apk add --no-cache --virtual .build-deps \
		git \
		autoconf \
		automake \
		build-base \
		bsd-compat-headers \
		gettext-dev \
		libev-dev \
		libtool \
		pcre-dev \
		udns-dev \
	&& git clone --single-branch https://github.com/dlundquist/sniproxy.git \
	&& cd sniproxy \
	&& aclocal \
	&& autoconf \
	&& ./autogen.sh \
	&& ./configure --prefix=/usr --sysconfdir=/etc \
	&& make all \
	&& /usr/bin/install -c src/sniproxy /usr/sbin \
	&& cd .. \
	&& rm -rf sniproxy \
	&& apk del --no-cache --purge --rdepends .build-deps \
	&& /usr/sbin/sniproxy -V

ENTRYPOINT ["/usr/sbin/sniproxy", "-f"]
