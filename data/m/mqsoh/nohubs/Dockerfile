FROM debian:stretch

RUN apt update && \
    apt install --assume-yes \
        openssh-server \
        gitweb \
        highlight \
    && rm -rf /var/lib/apt/lists/*


# SSH
RUN adduser --home /git --disabled-password git
COPY ./files/sshd_config /etc/ssh/
COPY ./files/regenerate-host-keys /bin/
RUN chmod +x /bin/regenerate-host-keys

# GitWeb
RUN a2enmod cgid
COPY ./files/apache.conf /etc/apache2/sites-enabled/000-default.conf
COPY ./files/gitweb_config.perl /usr/share/gitweb/gitweb_config.perl

# Repository management scripts.
COPY ./files/mkrepo /bin/
RUN chmod +x /bin/mkrepo
COPY ./files/fork /bin/
RUN chmod +x /bin/fork

COPY ./files/motd /etc/
COPY ./files/entrypoint.sh /bin/
RUN chmod +x /bin/entrypoint.sh
ENTRYPOINT [ "entrypoint.sh" ]
