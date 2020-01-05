FROM perl:5.22.0-threaded

MAINTAINER Leon Kyneur <leon@dexterous.org>

RUN apt-get update -y && apt-get install -y monitoring-plugins-common lmdb-utils
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN curl -L http://cpanmin.us | perl - App::cpm
RUN cpm install -g Date::Manip Net::LDAP
RUN rm -rf /root/.cpanm && rm -rf /root/.perl-cpm

ADD http://tools.ltb-project.org/attachments/download/813/ltb-project-nagios-plugins-0.6.tar.gz /
RUN tar xvf /ltb-project-nagios-plugins-0.6.tar.gz -C /
#RUN cd /ltb-project-nagios-plugins-0.6 && perl -p -i -e 's/\/usr\/local\/nagios\/libexec/\/usr\/lib\/nagios\/plugins/' *.pl
RUN cd /
WORKDIR /ltb-project-nagios-plugins-0.6
RUN perl -p -i -e 's/\/usr\/local\/nagios\/libexec/\/usr\/lib\/nagios\/plugins/' *.pl
RUN perl -p -i -e 's/\/usr\/local\/openldap\/sbin\/mdb_stat/\/usr\/bin\/mdb_stat/' *.pl
