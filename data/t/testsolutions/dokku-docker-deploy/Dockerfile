FROM alpine:3.8
RUN apk add --no-cache \
    openssh
ADD dokku_deploy.sh /bin/
RUN chmod +x /bin/dokku_deploy.sh
ENTRYPOINT /bin/dokku_deploy.sh
