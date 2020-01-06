FROM alpine

ENV MN_DOMAIN='example.com'
ENV MN_EMAIL='email@example.com'
ENV MN_WALLET=''
ENV MN_WALLET_FILENAME='wallet'

RUN apk add --no-cache certbot openssl
RUN apk add --update bash && rm -rf /var/cache/apk/*

WORKDIR /app
COPY init.sh .

RUN chmod +x init.sh

VOLUME ['/app/wallet']
VOLUME ['/app/content']
VOLUME ['/etc/letsencrypt']

CMD ["sh", "init.sh"]