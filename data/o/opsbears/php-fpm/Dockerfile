# We absolutely NEED a sendmail binary, even if it doesn't work, otherwise the mail() function will cause weird stuff to happen.
FROM opsbears/nullmailer:stable

ARG PACKAGEVERSION=7.0.26-2+ubuntu16.04.1+deb.sury.org+2

RUN add-apt-repository ppa:ondrej/php -y && \
  apt-get update -y && \
  apt-get install -y \
    php7.0-common=$PACKAGEVERSION \
    php7.0-cli=$PACKAGEVERSION \
    php7.0-fpm=$PACKAGEVERSION \
    php7.0-mysql=$PACKAGEVERSION \
    php7.0-mcrypt=$PACKAGEVERSION \
    php7.0-imap=$PACKAGEVERSION \
    php7.0-gmp=$PACKAGEVERSION \
    php7.0-curl=$PACKAGEVERSION \
    php7.0-xmlrpc=$PACKAGEVERSION \
    php7.0-xsl=$PACKAGEVERSION \
    php7.0-mbstring=$PACKAGEVERSION \
    php7.0-zip=$PACKAGEVERSION \
    php7.0-bz2=$PACKAGEVERSION \
    php7.0-intl=$PACKAGEVERSION \
    php7.0-imap=$PACKAGEVERSION \
    php7.0-soap=$PACKAGEVERSION \
    php7.0-gd=$PACKAGEVERSION \
    php7.0-zip=$PACKAGEVERSION \
    php-geoip \
    php-zip \
    php-bz2 \
    libfcgi0ldbl && \
  mkdir /run/php && \
  chown www-data:www-data /run/php && \
  mkdir /var/log/php && \
  chown www-data:www-data /var/log/php
RUN sed -i -e "s/;pm.status_path =/pm.status_path =/" /etc/php/7.0/fpm/pool.d/www.conf && \
 sed -i -e 's/listen = \/run\/php\/php7.0-fpm.sock/listen = 0.0.0.0:9000/' /etc/php/7.0/fpm/pool.d/www.conf && \
 sed -i -e 's/disable_functions = .*/disable_functions = pcntl_alarm,pcntl_fork,pcntl_waitpid,pcntl_wait,pcntl_wifexited,pcntl_wifstopped,pcntl_wifsignaled,pcntl_wifcontinued,pcntl_wexitstatus,pcntl_wtermsig,pcntl_wstopsig,pcntl_signal,pcntl_signal_dispatch,pcntl_get_last_error,pcntl_strerror,pcntl_sigprocmask,pcntl_sigwaitinfo,pcntl_sigtimedwait,pcntl_exec,pcntl_getpriority,pcntl_setpriority,exec,passthru,proc_open,proc_nice,shell_exec,system,popen,posix_kill,posix_setsid,posix_uname,dl,php_uname,phpinfo/' /etc/php/7.0/fpm/php.ini

COPY etc /etc
COPY usr /usr

EXPOSE 9000
HEALTHCHECK --interval=10s --timeout=3s CMD /usr/local/bin/healthcheck
