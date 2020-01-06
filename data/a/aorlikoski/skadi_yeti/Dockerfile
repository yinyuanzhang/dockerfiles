FROM ubuntu:18.04

ARG DEBIAN_FRONTEND=noninteractive

# Install YETI dependencies
RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y && apt-get install -y --no-install-suggests --no-install-recommends \
  build-essential \
  python-dev \
  libxml2-dev \
  libxslt-dev \
  zlib1g-dev \
  python-pip \
  python-setuptools \
  python-dev \
  python-wheel \
  locales \
  git \
  libmagic1 \
  curl \
  apt-transport-https \
  uwsgi-plugin-python \
  uwsgi && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/* /usr/share/man/* /root/.cache/*

# Setup locales
RUN locale-gen en_US.UTF-8 && \
        echo "LC_ALL=en_US.UTF-8" >> /etc/environment && \
        echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
        echo "LANG=en_US.UTF-8" > /etc/locale.conf

# Install frontend dependencies
RUN apt-get update && apt-get install -y --no-install-suggests --no-install-recommends gnupg2 && \
        curl -sL https://deb.nodesource.com/setup_8.x |  bash - && \
        curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
        echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
        apt-get update && apt-get install -y nodejs yarn && \
        rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/* /usr/share/man/* /root/.cache/*


# Upgrade pip
RUN pip install --upgrade pip

# Install & Configure YETI
RUN git clone https://github.com/yeti-platform/yeti.git /opt/yeti
WORKDIR /opt/yeti
RUN git checkout a293be9
RUN pip install -r requirements.txt && \
        pip install uwsgi && \
        yarn install && \
        mv yeti.conf.sample yeti.conf && \
        sed -i '25s/# host = 127.0.0.1/host = mongodb/' yeti.conf && \
        sed -i '38s/# host = 127.0.0.1/host = redis/' yeti.conf

# Configure image
RUN git clone https://github.com/vishnubob/wait-for-it.git /opt/wait-for-it && \
       cd /opt/wait-for-it && \
       git checkout 54d1f0b && \
       cp /opt/wait-for-it/wait-for-it.sh /usr/local/bin/ && \
       cd /opt/yeti

RUN groupadd yeti && \
        useradd -r --home-dir /opt/yeti -g yeti yeti && \
        mv /opt/yeti/extras/docker/scripts/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh && \
        chmod 755 /usr/local/bin/wait-for-it.sh /usr/local/bin/docker-entrypoint.sh && \
        chown -R yeti.yeti /opt/yeti
RUN mkdir /var/log/yeti; chown yeti /var/log/yeti

USER yeti

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["docker-entrypoint.sh", "webserver"]
