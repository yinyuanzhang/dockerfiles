FROM martinhelmich/typo3:8
LABEL maintainer="Seti <sebastian.koehlmeier@kyberna.com>"

ADD docker-typo3-entrypoint /usr/local/bin/

RUN apt update && apt install -y ghostscript ssh rsync && apt clean && rm -rf /var/lib/apt/lists/* /usr/src/*
RUN sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && \
    sed -i "s/UsePAM.*/UsePAM yes/g" /etc/ssh/sshd_config && \
    sed -i "s/#PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config && \
    chmod 0755 /usr/local/bin/docker-typo3-entrypoint

ENTRYPOINT ["docker-typo3-entrypoint"]
CMD ["apache2-foreground"]