FROM alpine:3.10

LABEL de.kdac.openldap.maintainer = "Claus Böhmer" \
      de.kdac.openldap.authors = "eso@bistum-eichstaett.de" \
      de.kdac.openldap.url = "https://hub.docker.com/r/kidac/openldap" \
      de.kdac.openldap.documentation = "https://hub.docker.com/r/kidac/openldap" \
      de.kdac.openldap.source = "https://github.com/kidac/openldap" \
      de.kdac.openldap.version = "2.4" \
      de.kdac.openldap.vendor = "KDAC - https://ews.kdac.de" \
      de.kdac.openldap.licenses = "https://www.openldap.org/software/release/license.html" \
      de.kdac.openldap.title = "Openldap (KDAC Version)" \
      de.kdac.openldap.description = "Adapted Openldap Dockerfile used by https://ews.kdac.de"

ENV LDAPDATA_DIR=/var/lib/openldap/openldap-data \
    LDAP_DIR=/etc/openldap

VOLUME ["${LDAPDATA_DIR}"]

RUN apk --no-cache upgrade \
 && apk add --no-cache bash openldap openldap-clients openldap-overlay-memberof openldap-overlay-refint openldap-overlay-deref openldap-back-mdb openldap-overlay-ppolicy tini

RUN mkdir -p /run/openldap

EXPOSE 389

COPY slapd.conf ${LDAP_DIR}
COPY initial.ldif ${LDAP_DIR}
COPY change_pw.ldif ${LDAP_DIR}

COPY entrypoint.sh /

CMD ["/entrypoint.sh"]
ENTRYPOINT ["/sbin/tini", "--"]
