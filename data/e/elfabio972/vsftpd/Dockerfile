FROM fauria/vsftpd:latest
ARG BUILD_DATE
ARG VCS_REF

RUN echo -e "\n# SSL \n\ 
ssl_enable=Yes \n\
rsa_cert_file=/etc/ssl/certs/vsftpd.crt \n\
rsa_private_key_file=/etc/ssl/private/vsftpd.key \n\
require_ssl_reuse=NO \n\
force_local_data_ssl=YES \n\
force_local_logins_ssl=YES \n\
ssl_ciphers=HIGH" >>  /etc/vsftpd/vsftpd.conf

# Build-time metadata as defined at http://label-schema.org
LABEL org.label-schema.build-date=$BUILD_DATE \
        org.label-schema.name="vsftpd SSL" \
        org.label-schema.description="A ssl only vsftpd docker image" \
        org.label-schema.vcs-ref=$VCS_REF \
        org.label-schema.vcs-url="https://github.com/fsimplice/docker-vsftpd" \
        org.label-schema.vendor="fsimplice" \
        org.label-schema.docker.debug="docker exec -it $CONTAINER /bin/bash"
