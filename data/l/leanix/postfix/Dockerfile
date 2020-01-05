FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y \
    python python-dev python-pip python-httplib2 \
    postfix=3.3.0-1 libsasl2-modules rsyslog && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install ansible==2.7.2

RUN mkdir /etc/ansible/ && \
    echo '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts

COPY postfix-start.sh /usr/local/bin/
COPY ansible /ansible

ENV POSTFIX_RELAYHOST in-v3.mailjet.com
ENV POSTFIX_RELAYHOST_PORT 587
ENV POSTFIX_SMTP_SASL_AUTH_ENABLE yes
ENV POSTFIX_SASL_DOMAIN leanix.net
ENV POSTFIX_TESTING True
ENV POSTFIX_TESTING_EMAIL development@leanix.net
ENV POSTFIX_BCC_EMAIL outgoing@leanix.net

ENV TERM=xterm

EXPOSE 25

CMD ["/usr/local/bin/postfix-start.sh"]