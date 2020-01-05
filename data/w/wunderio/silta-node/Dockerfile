FROM node:lts-alpine

RUN apk add --no-cache openssh bash python py-requests py-yaml rsync

EXPOSE 22

RUN mkdir /etc/ssh/keys

# Copy scripts
COPY gitauth_keys.py /etc/ssh/gitauth_keys.py
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

WORKDIR /app

CMD npm run start

