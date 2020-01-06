FROM phenoscape/owlery

MAINTAINER Robbie - Virtual Fly Brain <rcourt@ed.ac.uk>

ENV OWLURL=http://www.virtualflybrain.org/owl/vfb.owl

COPY application.conf /srv/conf/application.conf

USER root

COPY startup.sh /startup.sh

RUN chmod +x /startup.sh

USER $APP_USER

ENTRYPOINT ["/startup.sh"]
