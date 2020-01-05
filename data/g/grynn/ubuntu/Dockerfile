FROM ubuntu:trusty
RUN sed -i 's/\/archive.ubuntu/\/in.archive.ubuntu/' /etc/apt/sources.list
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qy 
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -qy
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy software-properties-common curl
RUN locale-gen en_US en_US.UTF-8
RUN DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales
RUN update-locale --reset LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
RUN LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 apt-add-repository -y ppa:ondrej/php
RUN apt-add-repository -y ppa:webupd8team/java
RUN apt-add-repository -y ppa:git-core/ppa
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN DEBIAN_FRONTEND=noninteractive apt-get install -dy nginx php7.2 php7.2-fpm apache2 redis-server redis-tools nodejs git mysql-server 
