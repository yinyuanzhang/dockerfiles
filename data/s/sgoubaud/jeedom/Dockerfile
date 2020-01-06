FROM jeedom/jeedom:lastest

RUN export LANG=en_US.UTF-8 && \
    echo "export LANG=en_US.UTF-8" >> ~/.bashrc

# Update system
RUN apt-get update && \
    apt install -y 	curl \
    				mosquitto-clients \
    				cron \
    				net-tools \
    				unzip \
    				tar \
    				ntp \ 
    				iputils-ping \
    				vim \
    				moreutils \
    				bash-completion

RUN echo "* * * * * www-data /usr/bin/php /var/www/html/core/php/jeeCron.php >> /dev/null" > /etc/cron.d/jeedom
RUN  echo "source /etc/profile.d/bash_completion.sh" >> ~/.bashrc

COPY resources/ /
RUN chmod 755 /usr/bin/docker-entrypoint.sh
RUN chmod 755 /usr/bin/liveness_status.sh

MAINTAINER "Sylvain Goubaud"
LABEL progam-name="Jeedom"
LABEL version="1.24"
ENV DOCKERFILE_VERSION=1.24

ENTRYPOINT ["docker-entrypoint.sh"]

# Ports
EXPOSE 80/tcp 22/tcp 443/tcp

CMD ["supervisord"]