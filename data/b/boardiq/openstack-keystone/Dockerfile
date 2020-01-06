FROM ubuntu:16.04
MAINTAINER Patrik Sundberg <patrik.sundberg@gmail.com>

EXPOSE 5000 35357

RUN apt-get update && apt-get install -y software-properties-common && \
    add-apt-repository cloud-archive:newton && apt-get update && \
    apt-get install -y keystone python-psycopg2 python-openstackclient sudo && \
    apt-get autoremove -y && \
    mkdir -p /files

COPY files/ /files
COPY entrypoint.sh bootstrap-db.sh initialize-keystone.sh /
COPY apache-keystone.conf /etc/apache2/sites-available/keystone.conf
COPY keystone-paste.ini /etc/keystone/

ENTRYPOINT ["/entrypoint.sh"]
