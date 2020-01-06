FROM dkolibar/ksandermann-updated:latest

RUN apt-get update && \
apt-get install -y apt-transport-https ca-certificates gnupg2 software-properties-common && \
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic test" && \
apt-get update && \
apt-get install -y docker-ce jq maven openjdk-8-jdk

ENV REDIS_VERSION 4.0.12
ENV REDIS_DOWNLOAD_URL http://download.redis.io/releases/redis-${REDIS_VERSION}.tar.gz
RUN apt-get install -y gcc make tar wget \
    && wget -O redis.tar.gz "$REDIS_DOWNLOAD_URL" \
    && mkdir -p /usr/src/redis \
    && tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1 \
    && rm redis.tar.gz \
    && make -C /usr/src/redis install redis-cli /usr/bin \
    && rm -r /usr/src/redis \
    && rm -rf /var/cache/apk/*


RUN docker -v
RUN mvn -v

ADD run.sh /tmp/run.sh
RUN chmod +x /tmp/run.sh
ENTRYPOINT ["/tmp/run.sh"]
