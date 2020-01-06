FROM debian:buster-slim
# hadolint ignore=DL3008
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        fakeroot \
        gettext-base \
        gnutls-bin \
        ldap-utils \
        libcap2-bin \
        slapd \
        ssl-cert \
        time \
    && \
    usermod -aG ssl-cert openldap && \
    setcap CAP_NET_BIND_SERVICE=+ep /usr/sbin/slapd && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apt/archives/* /var/lib/apt/lists/* && \
    rm -rf /var/lib/ldap/* /var/backups/ldap/* /run/slapd/* /etc/ldap/slapd.d && \
    install -d -o openldap -g ssl-cert -m 710 /etc/ssl/private && \
    install -d -o openldap -g root -m 755 /etc/ssl/certs && \
    install -o root -g ssl-cert -m 664 /dev/null /etc/ssl/certs/ssl-cert-snakeoil.pem && \
    install -o root -g ssl-cert -m 664 /dev/null /etc/ssl/private/ssl-cert-snakeoil.key && \
    install -o root -g ssl-cert -m 664 /dev/null /usr/share/slapd/dh.pem && \
    chown openldap /etc/ldap/ldap.conf && \
    install -d -o openldap -g openldap /run/slapd && \
    install -d -o openldap -g openldap /var/backups/ldap && \
    install -d -o openldap -g openldap /var/lib/ldap && \
    install -d -o openldap -g openldap /var/lib/ldap/config && \
    install -d -o openldap -g openldap /var/lib/ldap/data
COPY --chown=root:root config.ldif /usr/share/slapd/
COPY --chown=root:root skel.ldif /usr/share/slapd/
COPY --chown=root:root entrypoint /usr/local/sbin/
COPY --chown=root:root backup /usr/local/sbin/
EXPOSE 389 636
VOLUME [ "/var/lib/ldap" ]
VOLUME [ "/run/slapd" ]
VOLUME [ "/var/backups/ldap" ]
ENV LDAP_URLS="ldap:/// ldapi:/// ldaps:///" \
    SLAPD_DEBUG_LEVEL="stats,stats2,none" \
    SSL_CERT_FILE="/etc/ssl/certs/ssl-cert-snakeoil.pem" \
    SSL_KEY_FILE="/etc/ssl/private/ssl-cert-snakeoil.key" \
    SSL_CA_FILE="/etc/ssl/certs/ssl-cert-snakeoil.pem"
WORKDIR /var/lib/ldap
USER openldap
ENTRYPOINT [ "entrypoint" ]
CMD [ "slapd", "-F", "/var/lib/ldap/config", "-u", "openldap", "-g", "openldap", "-h", "\"$LDAP_URLS\"", "-d", "$SLAPD_DEBUG_LEVEL" ]
HEALTHCHECK CMD ldapsearch -b cn=config > /dev/null || exit 1
STOPSIGNAL INT
