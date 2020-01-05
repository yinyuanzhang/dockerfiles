FROM debian:stable-slim 

RUN groupadd -r -g 2000 vmail   && useradd --no-log-init -r -g vmail -u 2000 vmail

RUN apt-get clean && apt-get update && apt-get --no-install-recommends -y install dovecot-imapd python-setuptools python-pip rsyslog && apt-get clean && rm -rf /var/lib/apt/lists/* && pip install wheel && pip install supervisor supervisor-stdout

ADD supervisord.conf /etc/supervisord.conf
ADD rsyslog.conf /etc/rsyslog.conf

RUN mkdir /var/log/supervisor/

EXPOSE  993 
CMD ["supervisord","-n","-c","/etc/supervisord.conf"]
