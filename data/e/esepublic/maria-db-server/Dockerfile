FROM esepublic/baseimage
MAINTAINER Keith Bentrup <kbentrup@ebay.com>

# tmp fix if archive.ubuntu.com is slow
# RUN sed -i.bak 's/archive.ubuntu.com/us.archive.ubuntu.com/g' /etc/apt/sources.list

RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db && \
  add-apt-repository 'deb http://sfo1.mirrors.digitalocean.com/mariadb/repo/10.1/ubuntu trusty main' && \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes mariadb-server \
    inotify-tools \
    libxml2-utils \
    software-properties-common && \ 
  apt-get --purge autoremove -y && \
  apt-get clean && \
  rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*

COPY conf/additional.cnf /etc/mysql/conf.d/

EXPOSE 3306

