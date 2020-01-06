FROM larrycai/openldap:latest

COPY ./config.ldif config.ldif

RUN service slapd start && ldapadd -x -D cn=admin,dc=openstack,dc=org -w password -c -f config.ldif
