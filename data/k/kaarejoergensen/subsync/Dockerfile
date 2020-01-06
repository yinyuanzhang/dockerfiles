FROM lsiobase/ubuntu:bionic

# environment settings
ARG DEBIAN_FRONTEND="noninteractive"

# add local files
COPY root/ /
COPY bin/* /bin/

RUN \ 
 apt-get update && \
 echo "***** install prerequisites ****" && \
 apt-get install -y \
	python3 python3-pip python3-psutil ffmpeg git && \
 python3 -m pip install --upgrade pip setuptools wheel && \
 echo "***** install subsync ****" && \
 pip install git+https://github.com/smacke/subsync && \
 echo "***** make script executable ****" && \
 chmod +x /bin/syncsubs && \
 echo "***** install cron and logrotate ****" && \
 apt-get install -y cron logrotate --option=Dpkg::Options::=--force-confdef && \
 chmod 0644 /etc/cron.d/cron_sync && \
 crontab /etc/cron.d/cron_sync && \
 touch /var/log/cron.log && \
 echo "**** cleanup ****" && \
 apt-get purge --auto-remove -y && \
 apt-get clean

# ports and volumes
VOLUME /config /data
CMD ["cron", "-f"]
