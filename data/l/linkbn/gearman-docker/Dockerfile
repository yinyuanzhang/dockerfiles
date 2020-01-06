ARG CENTOS_VERSION=7
FROM centos:${CENTOS_VERSION}

ARG USER_ID=2000

RUN yum -y install epel-release && yum -y install gearmand
COPY bin/*.sh /
RUN chmod +x /*.sh
RUN chgrp -R 0 /var/log/ \
    && chmod -R g=u /var/log/ /etc/passwd
EXPOSE 4730

ENTRYPOINT ["/entrypoint.sh"]

USER ${USER_ID}