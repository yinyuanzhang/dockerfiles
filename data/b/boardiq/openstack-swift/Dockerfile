FROM ubuntu:16.04
MAINTAINER Patrik Sundberg <patrik.sundberg@gmail.com>

VOLUME "/dev/log", "/etc/swift" "/srv", "/ring"
EXPOSE 837 8080 6000 6001 6002

RUN apt-get update && apt-get install -y software-properties-common && \
    add-apt-repository cloud-archive:newton && apt-get update && \
    apt-get install -y supervisor rsync swift python-swiftclient \
                       swift-proxy swift-object python-keystoneclient \
                       python-openstackclient \
                       python-swiftclient swift-plugin-s3 python-netifaces \
                       python-xattr python-memcache cron \
                       swift-account swift-container swift-object pwgen sudo && \
    apt-get autoremove -y && \
    mkdir -p /srv /files /ring && \
    groupmod -g 1111 swift && \
    usermod -u 1111 swift && \
    usermod -g 1111 swift

# TODO: move into same run as above once confirmed working
RUN apt-get install -y python-keystonemiddleware && \
    chgrp swift /var/cache/swift

COPY entrypoint_storage.sh entrypoint_proxy.sh entrypoint_cmd.sh initialize-swift.sh create-*.sh grant-role.sh /
COPY files/* /files/
