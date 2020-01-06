FROM ubuntu:latest
MAINTAINER Thomas Berger <th.berger@it.piratenpartei.de>

RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get -y dist-upgrade && apt-get -y install apache2 rcs diffutils zip cron make gcc g++ pkg-config libssl-dev curl

ADD https://fossies.org/linux/www/TWiki-6.1.0.tgz ./TWiki-6.1.0.tgz
RUN mkdir -p /var/www && tar xf TWiki-6.1.0.tgz -C /var/www && rm TWiki-6.1.0.tgz

ADD perl/cpanfile /tmp/cpanfile
RUN curl -L https://cpanmin.us | perl - App::cpanminus && cpanm -l /var/www/twiki/lib/CPAN --installdeps /tmp/

ADD configs/vhost.conf /etc/apache2/sites-available/twiki.conf
ADD configs/LocalLib.cfg  /var/www/twiki/bin/LocalLib.cfg
ADD configs/LocalSite.cfg /var/www/twiki/lib/LocalSite.cfg
ADD configs/setlib.cfg /var/www/twiki/bin/setlib.cfg
ADD bin/prepare-env.sh /prepare-env.sh
ADD bin/run.sh /run.sh
RUN a2enmod cgi expires && a2dissite '*' && a2ensite twiki.conf && chown -cR www-data: /var/www/twiki && chmod +x /prepare-env.sh

VOLUME ["/data"]
ENTRYPOINT "/run.sh"

EXPOSE 80
