# Dockerfile for icinga2 with icingaweb2
# https://github.com/jjethwa/icinga2

FROM debian:jessie

MAINTAINER Jordan Jethwa

LABEL version="2.4.10"

ENV DEBIAN_FRONTEND noninteractive
ENV ICINGA2_FEATURE_GRAPHITE false
ENV ICINGA2_FEATURE_GRAPHITE_HOST graphite
ENV ICINGA2_FEATURE_GRAPHITE_PORT 2003

RUN apt-get -qq update \
    && apt-get -qqy upgrade \
    && apt-get -qqy install --no-install-recommends bash sudo procps ca-certificates wget supervisor mysql-server mysql-client apache2 pwgen unzip php5-ldap ssmtp mailutils vim php5-curl

RUN wget --quiet -O - http://debmon.org/debmon/repo.key 2>/dev/null | apt-key add -
RUN echo "deb http://debmon.org/debmon debmon-jessie main" > /etc/apt/sources.list.d/debmon.list

RUN apt-get -qq update \
    && apt-get -qqy install --no-install-recommends -t debmon-jessie icinga2 icinga2-ido-mysql icinga-web nagios-plugins icingaweb2 \
    && apt-get clean

# Temporary hack to get icingaweb2 modules via git
RUN mkdir -p /etc/icingaweb2/enabledModules
RUN wget --no-cookies "https://github.com/Icinga/icingaweb2/archive/v2.3.2.zip" -O /tmp/icingaweb2.zip
RUN unzip /tmp/icingaweb2.zip "icingaweb2-2.3.2/modules/doc/*" "icingaweb2-2.3.2/modules/monitoring/*" -d "/tmp/icingaweb2"
RUN cp -R /tmp/icingaweb2/icingaweb2-2.3.2/modules/monitoring /etc/icingaweb2/modules/
RUN cp -R  /tmp/icingaweb2/icingaweb2-2.3.2/modules/doc /etc/icingaweb2/modules/
RUN rm -rf /tmp/icingaweb2.zip /tmp/icingaweb2

# Icinga Director
RUN wget --no-cookies "https://github.com/Icinga/icingaweb2-module-director/archive/master.zip" -O /tmp/director.zip
RUN unzip /tmp/director.zip -d "/tmp/director"
RUN mkdir /etc/icingaweb2/modules/director
RUN cp -R /tmp/director/icingaweb2-module-director-master/* /etc/icingaweb2/modules/director/
RUN rm -rf /tmp/director

EXPOSE 80 443 5665

ADD content/ /

RUN chmod u+x /opt/supervisor/mysql_supervisor /opt/supervisor/icinga2_supervisor /opt/supervisor/apache2_supervisor
RUN chmod u+x /opt/run

RUN chmod u+s /bin/ping && chmod u+s /bin/ping6

# Initialize and run Supervisor
ENTRYPOINT ["/opt/run"]
