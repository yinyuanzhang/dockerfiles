FROM quantumobject/docker-nagios

RUN apt-get update
RUN apt-get -y install gettext
COPY utils/replace-vars /replace-vars
COPY cmd.sh /cmd.sh

RUN mkdir /usr/local/nagios/etc/servers
COPY conf/servers/ /usr/local/nagios/etc/servers/
COPY conf/nagios.cfg /usr/local/nagios/etc/nagios.cfg
COPY conf/commands.cfg /usr/local/nagios/etc/objects/commands.cfg
COPY conf/contacts.cfg /usr/local/nagios/etc/objects/contacts.cfg
COPY conf/mailname /etc/mailname

CMD ["/cmd.sh"]
