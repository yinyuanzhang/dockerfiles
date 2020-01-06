#
# *** IMPORTANT: Change default password on first use ***
#
# Username: admin
# Password: foswiki
#

FROM debian:stretch

LABEL maintainer="robinwunderbaldinger@gmail.com"

WORKDIR /var/www/foswiki

RUN apt-get update && apt-get -y install nano curl unzip nginx build-essential \
    libalgorithm-diff-perl libarchive-tar-perl libauthen-sasl-perl libcgi-pm-perl libcgi-session-perl \
    libcrypt-passwdmd5-perl libdigest-sha-perl libemail-address-perl libemail-mime-perl \
    libencode-perl liberror-perl libfile-copy-recursive-perl libhtml-parser-perl libhtml-tree-perl \
    libio-socket-ip-perl libio-socket-ssl-perl libjson-perl liblocale-maketext-perl \
    liblocale-maketext-lexicon-perl liblocale-msgfmt-perl libwww-perl liblwp-protocol-https-perl \
    liburi-perl libversion-perl cpanminus libfcgi-perl libfcgi-procmanager-perl && \
    cpan -i Crypt::Eksblowfish::Bcrypt && \
    curl -LfsS https://sourceforge.net/projects/foswiki/files/latest/download -o ../foswiki.zip  && \
    unzip ../foswiki.zip -d .. && mv ../Foswiki*/* . && rmdir ../Foswiki* && rm ../foswiki.zip && \
    chown -R www-data:www-data . && mkdir external-config && mkdir external-config/foswiki-etc && \
    cp tools/foswiki.defaults external-config/foswiki-etc/foswiki-default && \
    cp tools/foswiki.init-script external-config/foswiki-init-script && \
    ln -s /var/www/foswiki/external-config/foswiki-etc/foswiki-default /etc/default/foswiki && \
    ln -s /etc/nginx/sites-available/foswiki /etc/nginx/sites-enabled/foswiki && \
    chown -R root:root external-config/foswiki-etc && \
    rm /etc/nginx/sites-enabled/default && \
    sed -i "/@INC/ a \ \ \ \ push @INC, '/var/www/foswiki/bin';" bin/foswiki.fcgi

COPY foswiki.conf /etc/nginx/sites-available/foswiki
COPY LocalSite.cfg /var/www/foswiki/lib/LocalSite.cfg

ENV FOSWIKI_ROOT=/var/www/foswiki \
    FOSWIKI_FCGI=foswiki.fcgi \
    FOSWIKI_BIND=127.0.0.1:9000 \
    FOSWIKI_CHILDREN=3 \
    FOSWIKI_MAX_REQUESTS=-1 \
    FOSWIKI_MAX_SIZE=200000 \
    FOSWIKI_CHECK_SIZE=10 \
    FOSWIKI_PNAME=foswiki \
    FOSWIKI_QUIET=true \
    FOSWIKI_PIDFILE=/var/run/foswiki.pid

EXPOSE 80
EXPOSE 9000

CMD perl $FOSWIKI_ROOT/bin/$FOSWIKI_FCGI \
         -n $FOSWIKI_CHILDREN \
         -l $FOSWIKI_BIND \
         -c $FOSWIKI_CHECK_SIZE \
         -x $FOSWIKI_MAX_REQUESTS \
         -s $FOSWIKI_MAX_SIZE \
         -p $FOSWIKI_ROOT/working/foswiki.pid \
         -a $FOSWIKI_PNAME \
         -d && \
    nginx -g "daemon off;"

