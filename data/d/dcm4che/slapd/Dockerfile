FROM alpine:3.10

RUN apk --no-cache --update add openldap openldap-back-mdb openldap-overlay-syncprov openldap-clients

ENV LDAP_USER_ID=1021 \
    LDAP_GROUP_ID=1021 \
    LDAP_ORGANISATION=dcm4che.org \
    LDAP_BASE_DN=dc=dcm4che,dc=org \
    LDAP_URLS="ldap:///" \
    LDAP_TLS_CACERT=/etc/certs/cacert.pem \
    LDAP_TLS_CERT=/etc/certs/cert.pem \
    LDAP_TLS_KEY=/etc/certs/key.pem \
    LDAP_TLS_VERIFY=never \
    LDAP_TLS_REQCERT=never

VOLUME [ "/var/lib/openldap/openldap-data", "/etc/openldap/slapd.d" ]

COPY docker-entrypoint.sh setenv.sh slapadd.sh /
COPY ldap /etc/openldap
COPY certs /etc/certs
COPY bin /usr/bin

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 389
CMD ["slapd", "-d", "32768", "-u", "ldap", "-g", "ldap"]
