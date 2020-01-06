FROM ubuntu:16.04

LABEL Maintainer="esousa@whitestack.com" \
      Description="Openstack Keystone Instance (Modified)" \
      Version="1.0" \
      Author="Eduardo Sousa"

EXPOSE 5000

WORKDIR /keystone

COPY scripts/start.sh /keystone/start.sh

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get autoremove -y && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y cloud-archive:queens && \
    apt-get update && apt dist-upgrade -y && \
    apt-get install -y python-openstackclient keystone apache2 libapache2-mod-wsgi net-tools mysql-client && \
    rm -rf /var/lib/apt/lists/* && \
    chmod +x start.sh

# database
ENV DB_HOST                 keystone-db
ENV DB_PORT                 3306
ENV ROOT_DB_USER            root
ENV ROOT_DB_PASSWORD        admin
ENV KEYSTONE_DB_PASSWORD    admin
# keystone
ENV REGION_ID               RegionOne
ENV KEYSTONE_HOST           keystone
# - admin
ENV ADMIN_USERNAME          admin
ENV ADMIN_PASSWORD          admin
ENV ADMIN_PROJECT_NAME      admin
# - user
ENV USERNAME                nbi
ENV PASSWORD                nbi
ENV SERVICE                 service

ENTRYPOINT ./start.sh
