FROM lakshtinagar/xmpp-server:v1.0

MAINTAINER Lakshit Nagar <lakshitnagar@gmail.com>

USER root

COPY /assets/entrypoint.sh /usr/bin/
RUN chmod 777 /usr/bin/entrypoint.sh \
    && ln -s /usr/bin/entrypoint.sh /

COPY /assets/ejabberd/ejabberd.yml /etc/ejabberd/

ENTRYPOINT ["entrypoint.sh"]
#CMD ["/usr/bin/ejabberdctl", "start"]
#CMD tail -f /dev/null
