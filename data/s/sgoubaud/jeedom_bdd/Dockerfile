FROM mysql:5.7

RUN export LANG=en_US.UTF-8 && \
    echo "export LANG=en_US.UTF-8" >> ~/.bashrc

# Update system
RUN apt-get update && \
    apt install -y 	curl \
    				procps \
    				mosquitto-clients \
    				cron \
    				net-tools \
    				unzip \
    				tar \
    				ntp \
    				iputils-ping \
    				vim \
    				bash-completion \
    				moreutils
    				
RUN echo "source /etc/profile.d/bash_completion.sh" >> ~/.bashrc

MAINTAINER "Sylvain Goubaud"
LABEL progam-name="Jeedom DB"
LABEL version="1.13"
ENV DOCKERFILE_VERSION=1.13

COPY resources/ /
RUN chmod 744 /usr/bin/overrided-entrypoint.sh
