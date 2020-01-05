FROM ubuntu:14.04
ENV DEBIAN_FRONTEND noninteractive

MAINTAINER Fabio Robayo  <fabio.robayo@risk-mi.com>

# update and install packages
RUN apt-get -qq update \
        && apt-get -qq upgrade -y \
        && apt-get -qq install -y apache2 php5 php5-mysql php5-sqlite php5-curl php5-intl php5-xdebug libphp-jpgraph octave epstool transfig sendmail cron

RUN apt-get install -y aria2 make libatlas-base-dev gfortran gcc-multilib \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir ~/glpk \
    && cd ~/glpk \
    && aria2c -s 16 -x 16 -k 30M ftp://ftp.gnu.org/gnu/glpk/glpk-4.47.tar.gz -o glpk-4.47.tar.gz \
    && tar -xzvf glpk-4.47.tar.gz \
    && cd glpk-4.47 \
    && ./configure \
    && make check \
    && make install \
    && make clean \
    && rm -rf ../glpk-4.47.tar.gz

# setting apache env vars
ENV APACHE_CONFDIR /etc/apache2
ENV APACHE_ENVVARS $APACHE_CONFDIR/envvars
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_PID_FILE $APACHE_RUN_DIR/apache2.pid
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_LOG_DIR /var/log/apache2
ENV LANG C
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR

# redirect logs to stdout and stderr
RUN find "$APACHE_CONFDIR" -type f -exec sed -ri ' \
        s!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g; \
        s!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g; \
        ' '{}' ';'

# adding assets
ADD assets/ /assets/

EXPOSE 80

ENTRYPOINT ["/assets/entrypoint.sh"]
