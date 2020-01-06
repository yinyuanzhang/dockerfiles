FROM debian:stretch
MAINTAINER LWB

ENV APPLICATION=APP \
		FILE_BACKUP_USER=ADMIN \
		FILE_BACKUP_PASSWORD=ADMIN \
		FILE_BACKUP_PATH=/ \
		BACKUP_PATH="/var/www/html/"

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y --force-yes --no-install-recommends tar bzip2 cifs-utils && \
    rm -rf /var/lib/apt/lists

USER root

ADD ./backup.sh /

CMD ["/backup.sh"]
