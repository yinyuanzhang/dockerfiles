FROM joshuacox/ubuntu:14.04
MAINTAINER 'josh 'at' webhosting coop'
ENV UBUNTU_NGINX_UPDATED 20160808
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E1DF1F24 \
 && echo "deb http://ppa.launchpad.net/git-core/ppa/ubuntu trusty main" >> /etc/apt/sources.list \
 && apt-key adv --keyserver keyserver.ubuntu.com --recv C3173AA6 \
 && echo "deb http://ppa.launchpad.net/brightbox/ruby-ng/ubuntu trusty main" >> /etc/apt/sources.list \
 && apt-key adv --keyserver keyserver.ubuntu.com --recv C300EE8C \
 && echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu trusty main" >> /etc/apt/sources.list \
 && apt-get update \
 && apt-get install -y supervisor logrotate locales \
      nginx openssh-server mysql-client postgresql-client redis-tools \
      git-core ruby2.1 python2.7 python-docutils \
      libmysqlclient18 libpq5 zlib1g libyaml-0-2 libssl1.0.0 \
      libgdbm3 libreadline6 libncurses5 libffi6 \
      libxml2 libxslt1.1 libcurl3 libicu52 \
 && update-locale LANG=C.UTF-8 LC_MESSAGES=POSIX \
 && locale-gen en_US.UTF-8 \
 && dpkg-reconfigure locales \
 && gem install --no-document bundler \
 && rm -rf /var/lib/apt/lists/* 
