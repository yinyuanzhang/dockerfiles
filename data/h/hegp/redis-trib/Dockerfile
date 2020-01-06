FROM ruby:2.5-alpine3.7

# RUN echo "http://mirrors.aliyun.com/alpine/v3.7/main" > /etc/apk/repositories && \
#    echo "http://mirrors.aliyun.com/alpine/v3.7/community" >> /etc/apk/repositories
# gem安装制定版本软件的命令  gem install redis -v 4.0.1 , 与 redis的版本相匹配, 避免版本不匹配导致问题
RUN gem install redis:4.0.1; \
    apk add --no-cache curl tar; \
    curl http://download.redis.io/releases/redis-4.0.9.tar.gz -s -o /redis-4.0.9.tar.gz; \
    tar -zxvf /redis-4.0.9.tar.gz -C / ; \
    cp /redis-4.0.9/src/redis-trib.rb /usr/bin; \
    chmod +x /usr/bin/redis-trib.rb; \
    rm -rf /redis-4.0.9; \
    rm -rf /redis-4.0.9.tar.gz; \
    apk del tar curl

CMD ["sh"]
