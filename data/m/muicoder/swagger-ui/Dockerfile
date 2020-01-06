FROM nginx:mainline-alpine

RUN apk add --no-cache bash libstdc++ curl wget tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    wget -qO- github.com/swagger-api/swagger-ui/archive/master.tar.gz | tar -xzf - -C /tmp && \
        mv -f /tmp/swagger-ui-master/dist/* /usr/share/nginx/html && \
    rm -rf /tmp/*
