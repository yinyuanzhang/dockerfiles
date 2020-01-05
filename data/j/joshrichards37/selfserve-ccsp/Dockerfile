FROM debian:stretch-slim

ENV DEBIAN_FRONTEND noninteractive

RUN cat /etc/apt/sources.list

RUN apt-get update
RUN apt-get install sudo openssh-client curl -y
RUN apt-get install ca-certificates apt-transport-https gnupg gcc g++ make wget curl libpng-dev -y
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash - \
    && wget -q https://packages.sury.org/php/apt.gpg -O- | apt-key add - \
    && echo "deb https://packages.sury.org/php/ stretch main" | tee /etc/apt/sources.list.d/php.list \
    && apt-get update
RUN apt-get install php7.2-cli php7.2-common php7.2-curl php7.2-gd php7.2-json php7.2-ldap php7.2-mbstring php7.2-mysql php7.2-xml php7.2-zip php7.2-intl nodejs -y

RUN curl -fsSL https://getcomposer.org/installer | php \
&& mv composer.phar /usr/local/bin/composer
