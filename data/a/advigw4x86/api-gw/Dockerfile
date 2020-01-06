FROM alpine

RUN apk update && apk add --no-cache git nodejs && \
    git clone https://github.com/ADVANTECH-Corp/APIGateway.git /home/adv/APIGateway && \
    cp /home/adv/APIGateway/script/advigw-restapi /usr/local/bin/. && \
    apk del git && rm -rf /tmp/* /var/cache/apk/*
    
VOLUME ["/home/adv/wsn_setting"]

EXPOSE 3000

ENTRYPOINT ["advigw-restapi"]

