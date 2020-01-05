FROM ubuntu:xenial
MAINTAINER Josh Lukens <jlukens@botch.com>

ENV SQUEEZE_VOL /srv/squeezebox
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND noninteractive
ENV BASESERVER_URL=http://downloads.slimdevices.com/nightly/7.9/sc/
ENV PERL_MM_USE_DEFAULT 1

RUN buildDeps='build-essential libssl-dev libffi-dev python-pip python-dev' && \
        apt-get update && \
	apt-get -y install curl faad flac lame libcrypt-openssl-bignum-perl libcrypt-openssl-random-perl libcrypt-openssl-rsa-perl libcrypt-ssleay-perl libfont-freetype-perl libfreetype6 libio-socket-ssl-perl libpython2.7 openssl perl pv sox sudo tzdata wget $buildDeps && \
	RELEASE=`curl -Lsf -o - "${BASESERVER_URL}?C=M;O=A" | grep DIR | sed -e '$!d' -e 's/.*href="//' -e 's/".*//'` && \
	MEDIAFILE=`curl -Lsf -o - "${BASESERVER_URL}${RELEASE}" | grep _amd64.deb | sed -e '$!d' -e 's/.*href="//' -e 's/".*//'` && \
	MEDIASERVER_URL="${BASESERVER_URL}${RELEASE}${MEDIAFILE}" && \
	curl -Lsf -o /tmp/logitechmediaserver.deb $MEDIASERVER_URL && \
	dpkg -i /tmp/logitechmediaserver.deb && \
	rm -rf /usr/share/squeezeboxserver/CPAN/Font && \
	rm -f /tmp/logitechmediaserver.deb && \
	pip install --upgrade pip && \
        hash -r pip && \
	pip install gmusicapi==12.0.0 && \
	cpan App::cpanminus && \
	cpanm --notest Inline && \
	cpanm --notest Inline::Python && \
	apt-get purge -y --auto-remove $buildDeps && \
	apt-get clean && \
        rm -rf /var/lib/apt/lists/* && \
        awk '/sub serverAddr {/{print $0 " \nif(defined $ENV{'\''PUBLIC_IP'\''}) { return $ENV{'\''PUBLIC_IP'\''} }"; next}1' /usr/share/perl5/Slim/Utils/Network.pm > /tmp/Network.pm && \
	mv /tmp/Network.pm /usr/share/perl5/Slim/Utils/Network.pm

VOLUME $SQUEEZE_VOL
EXPOSE 3483 3483/udp 9000 9090

COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

