FROM ruby:2.1

RUN set -ex \
  && apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y --no-install-recommends ca-certificates apt-transport-https \
    curl wget net-tools dnsutils mtr telnet rsync git-core htop iftop screen vim \
    cron supervisor locales openssh-server bzip2 libfontconfig less \
    libmysqlclient-dev redis-tools netcat logrotate \
  && rm -rf /var/lib/apt/lists/*


RUN set -ex \
  && { \
      echo '[program:cron]'; \
      echo 'command=/usr/sbin/cron -f'; \
  } >> /etc/supervisor/conf.d/cron.conf \
  \
  && mkdir -p /var/log/supervisor \
  && { \
    echo '[supervisord]'; \
    echo 'nodaemon=true'; \
  } >> /etc/supervisor/conf.d/supervisord.conf \
  \
  && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
  && locale-gen \
  && update-locale LANG=en_US.UTF-8 LANGUAGE=en_US:en: \
  \
  && mkdir -p /var/run/sshd \
  && { \
    echo '[program:sshd]'; \
    echo 'command=/usr/sbin/sshd -D'; \
  } >> /etc/supervisor/conf.d/sshd.conf

ENV LC_ALL en_US.UTF-8


RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
  && echo "deb http://nginx.org/packages/debian/ $(awk -F"[)(]+" '/VERSION=/ {print $2}' /etc/os-release) nginx" >> /etc/apt/sources.list \
  && apt-get update \
  && apt-get install --no-install-recommends --no-install-suggests -y \
            ca-certificates \
            nginx \
  && { \
    echo '[program:nginx]'; \
    echo 'command=nginx -g "daemon off;"'; \
  } >> /etc/supervisor/conf.d/nginx.conf \
  && rm -rf /var/lib/apt/lists/*


RUN set -ex \
  && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
  && apt-get update \
  && apt-get install -y --no-install-recommends nodejs \
  && rm -rf /var/lib/apt/lists/*

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
  && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
  && apt-get update \
  && apt-get install --no-install-recommends yarn \
  && rm -rf /var/lib/apt/lists/*

RUN set -ex \
  && echo "Asia/Shanghai" > /etc/timezone \
  && dpkg-reconfigure -f noninteractive tzdata \
  && mkdir -p /root/.ssh \
  && { \
    echo 'Host *'; \
    echo 'ServerAliveInterval=15'; \
    echo 'ServerAliveCountMax=6'; \
    echo 'ForwardAgent yes'; \
  } >> /root/.ssh/config \
  && mkdir -p /root/.bash.d \
  && touch /root/.app.bash \
  && curl -SL https://raw.githubusercontent.com/agideo/docker-library-ruby/master/files/bash.d/10_ssh-agent.bash -o /root/.bash.d/10_ssh-agent.bash \
  && { \
    echo 'source ~/.bash.d/10_ssh-agent.bash'; \
    echo 'source ~/.app.bash'; \
    echo "export TERM=xterm"; \
    echo "export PATH=$(echo $PATH)"; \
    echo "unset HISTFILE"; \
  } >> /root/.bashrc


ENV TELEPORT_VERSION 4.0.10
RUN set -ex \
  && wget https://get.gravitational.com/teleport-v$TELEPORT_VERSION-linux-amd64-bin.tar.gz \
  && mkdir -p /tmp/teleport \
  && tar -xzf teleport-v$TELEPORT_VERSION-linux-amd64-bin.tar.gz -C /tmp/teleport --strip-components=1 \
  && mv /tmp/teleport/teleport /usr/local/bin/ \
  && rm -rf teleport-v$TELEPORT_VERSION-linux-amd64-bin.tar.gz /tmp/teleport

WORKDIR /app

EXPOSE 22 80 3000
CMD ["sh", "-c", "env >> /etc/environment ; /usr/bin/supervisord"]
