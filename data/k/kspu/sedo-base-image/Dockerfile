FROM ubuntu:bionic AS base
RUN apt update && apt upgrade -y
RUN DEBIAN_FRONTEND=noninteractive apt install -y tzdata && ln -fs /usr/share/zoneinfo/Asia/Krasnoyarsk /etc/localtime && dpkg-reconfigure --frontend noninteractive tzdata
RUN DEBIAN_FRONTEND=noninteractive apt install -y software-properties-common && add-apt-repository ppa:ondrej/php && apt update

RUN DEBIAN_FRONTEND=noninteractive apt install -y nginx apache2 php5.6 php5.6-fpm libapache2-mod-php5.6
RUN DEBIAN_FRONTEND=noninteractive apt install -y php5.6-mysql php5.6-intl php5.6-ldap php5.6-xml php5.6-mbstring php5.6-curl php5.6-gd php5.6-zip unzip composer sudo
RUN DEBIAN_FRONTEND=noninteractive apt install -y npm && npm install -g bower yarn gulp

