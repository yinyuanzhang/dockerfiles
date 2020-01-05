FROM ubuntu:18.04
MAINTAINER Thomas Cheng <thomas@beamstyle.com.hk>

ENV DEBIAN_FRONTEND=noninteractive

# Install some basic dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common \
    vim \
    curl \
    git \
    zip \
    unzip \
    wget

# Add APT repository for PHP 7.3
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php

# Installing Git
RUN apt-get update 
RUN apt-get install -y \
    git
RUN git config --global http.postBuffer 157286400

# Installing Composer
RUN apt-get update && apt-get install -y \
    php7.3 \
    php7.3-sqlite3 \
    php7.3-curl \
    php7.3-gd \
    php7.3-mbstring \
    php7.3-mysql \
    php7.3-xml \
    php7.3-zip \
    gettext

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer


# Installing SSH

RUN apt-get update
RUN apt-get install -y openssh-server

# Setup for SSH server
RUN mkdir /var/run/sshd

# Enabling password-based login for SSH server
RUN sed -ri 's/#PermitRootLogin.*$/PermitRootLogin yes/g' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

# Login fix (otherwise user is kicked off after login) for SSH server
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# Set user visibility
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# Exposing the SSH port
EXPOSE 22

# Running the custom script file "run.sh"
ADD run.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/run.sh

CMD ["/usr/local/bin/run.sh"]

# https://docs.docker.com/engine/examples/running_ssh_service/#build-an-eg-sshd-image



