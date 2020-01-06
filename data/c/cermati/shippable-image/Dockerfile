FROM ubuntu:16.04


# Install Redis 2.8.24
# Sources: https://github.com/docker-library/redis/blob/master/4.0/Dockerfile
#          https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-redis-on-ubuntu-16-04
ENV REDIS_VERSION 2.8.24
ENV REDIS_DOWNLOAD_URL http://download.redis.io/releases/redis-2.8.24.tar.gz
ENV REDIS_DOWNLOAD_SHA 6c86ca5291ca7f4e37d9c90511eed67beb6649befe57e2e26307f74adb8630fe

RUN groupadd -r redis && useradd -r -g redis redis
RUN mkdir /var/lib/redis && chown redis:redis /var/lib/redis
RUN set -ex; \
	\
	buildDeps=' \
		wget \
		\
		gcc \
		libc6-dev \
		make \
	'; \
	apt-get update; \
	apt-get install -y $buildDeps --no-install-recommends; \
	rm -rf /var/lib/apt/lists/*; \
	\
	wget -O redis.tar.gz "$REDIS_DOWNLOAD_URL"; \
	echo "$REDIS_DOWNLOAD_SHA *redis.tar.gz" | sha256sum -c -; \
	mkdir -p /usr/src/redis; \
	tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1; \
	rm redis.tar.gz; \
	\
	make -C /usr/src/redis -j "$(nproc)"; \
	make -C /usr/src/redis install

RUN set -ex; \
	\
	mkdir /etc/redis; \
	cp /usr/src/redis/redis.conf /etc/redis; \
	sed -i 's/^supervised.*/supervised systemd/g' /etc/redis/redis.conf; \
	sed -i 's/^daemonize.*/daemonize yes/g' /etc/redis/redis.conf; \
	sed -i 's/^dir.*/dir \/var\/lib\/redis/g' /etc/redis/redis.conf


# Install MongoDB 3.4.6
# Sources: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
ENV MONGODB_VERSION 3.4.6
ENV MONGODB_ENV_SRC "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse"

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6; \
	echo "$MONGODB_ENV_SRC" | tee /etc/apt/sources.list.d/mongodb-org-3.4.list; \
	apt-get update

RUN apt-get install mongodb-org="$MONGODB_VERSION" mongodb-org-server="$MONGODB_VERSION" mongodb-org-shell="$MONGODB_VERSION" \
	mongodb-org-mongos="$MONGODB_VERSION" mongodb-org-tools="$MONGODB_VERSION"


# Add Yarn dependencies
RUN apt-get install -y curl
RUN curl -sS http://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

# Install dependencies for node package `canvas` for Image Quality Assessor
RUN apt-get install -y libcairo2-dev libjpeg8-dev libpango1.0-dev libgif-dev build-essential g++


# Install NVM, nodejs, and yarn
# Sources: https://github.com/dry-dock/u16/blob/master/node/install.sh
ENV NVM_DIR="/root/.nvm"
ENV NODE_VERSION 8.10.0

RUN curl -sS https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash \
	&& . $NVM_DIR/nvm.sh \
	&& nvm install $NODE_VERSION \
	&& nvm alias default $NODE_VERSION \
	&& nvm use default

RUN apt-key adv --fetch-keys http://dl.yarnpkg.com/debian/pubkey.gpg
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update
RUN apt-get install -y yarn=0.24.5-1

# Install git
RUN apt-get install -y git

# Install s3cmd
RUN apt-get install -y s3cmd

# Entrypoint
ADD entrypoint.sh /opt/entrypoint.sh
RUN chmod 755 /opt/entrypoint.sh
CMD "/opt/entrypoint.sh"
