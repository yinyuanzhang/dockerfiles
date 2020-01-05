FROM codeception/codeception

# Install PhantomJS (https://github.com/wernight/docker-phantomjs/blob/master/Dockerfile).
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        ca-certificates \
        bzip2 \
        libfontconfig \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN set -x  \
    # Install official PhantomJS release
 && apt-get update \
 && apt-get install -y --no-install-recommends \
        curl \
 && mkdir /tmp/phantomjs \
 && curl -L https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
        | tar -xj --strip-components=1 -C /tmp/phantomjs \
 && mv /tmp/phantomjs/bin/phantomjs /usr/local/bin \
    # Install dumb-init (to handle PID 1 correctly).
    # https://github.com/Yelp/dumb-init
 && curl -Lo /tmp/dumb-init.deb https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-init_1.1.3_amd64.deb \
 && dpkg -i /tmp/dumb-init.deb \
    # Clean up
 && apt-get clean \
 && rm -rf /tmp/* /var/lib/apt/lists/*
# The end of the PhantomJS installation.

# Install Supervisor.
RUN apt-get update && apt-get -y install supervisor && \
  mkdir -p /var/log/supervisor && \
  mkdir -p /etc/supervisor/conf.d

# Install ssh-client.
RUN apt-get update && apt-get install ssh-client -y

# Install Drush: http://docs.drush.org/en/8.x/install-alternative/
RUN composer global require consolidation/cgr:2.0.* \
  && export PATH="$HOME/.composer/vendor/bin:$PATH" \
  && echo "export PATH=\"$HOME/.composer/vendor/bin:$PATH\"" >> ~/.bashrc \
  && cgr drush/drush:8.x

# Install Terminus: https://pantheon.io/docs/terminus/install/
RUN mkdir ~/terminus \
  && cd ~/terminus \
  && curl -O https://raw.githubusercontent.com/pantheon-systems/terminus-installer/master/builds/installer.phar \
  && php installer.phar install

RUN { \
	echo '[supervisord]'; \
        echo 'nodaemon=true'; \
        echo '[program:phantomjs]'; \
        echo 'command=/bin/bash -c "phantomjs --webdriver=4444"'; \
        echo 'autostart=true'; \
        echo 'autorestart=true'; \
	} > /etc/supervisor/conf.d/supervisord.conf

ENTRYPOINT ["/usr/bin/supervisord"]
