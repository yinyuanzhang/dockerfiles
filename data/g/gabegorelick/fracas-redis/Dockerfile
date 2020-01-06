###############################################################################
# Dockerfile for Redis. Based on docker-library/redis, but uses debian-testing
# (jessie) instead of stable (wheezy), since that's what we use for everything
# else and we want to share container layers as much as possible.
###############################################################################

FROM debian:jessie

MAINTAINER Gabe Gorelick, "https://github.com/gabegorelick"

# add our user and group first to make sure their IDs get assigned consistently,
# regardless of whatever dependencies get added
RUN groupadd -r redis && useradd -r -g redis redis

ENV REDIS_DOWNLOAD_URL http://download.redis.io/releases/redis-2.8.17.tar.gz
ENV REDIS_DOWNLOAD_SHA1 913479f9d2a283bfaadd1444e17e7bab560e5d1e

RUN buildDeps='gcc libc6-dev make'; \
	set -x; \
	apt-get update && apt-get install -y $buildDeps curl --no-install-recommends \
	&& rm -rf /var/lib/apt/lists/* \
	&& mkdir -p /usr/src/redis \
	&& curl -sSL "$REDIS_DOWNLOAD_URL" -o redis.tar.gz \
	&& echo "$REDIS_DOWNLOAD_SHA1 *redis.tar.gz" | sha1sum -c - \
	&& tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1 \
	&& rm redis.tar.gz \
	&& make -C /usr/src/redis \
	&& make -C /usr/src/redis install \
	&& rm -r /usr/src/redis \
	&& apt-get purge -y $buildDeps curl \
	&& apt-get autoremove -y

RUN mkdir /data && chown redis:redis /data
VOLUME /data
WORKDIR /data

USER redis
EXPOSE 6379
CMD ["redis-server"]
