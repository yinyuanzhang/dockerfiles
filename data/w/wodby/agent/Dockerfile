FROM wodby/base-alpine:3.4
MAINTAINER Wodby <hello@wodby.com>

COPY rootfs /

RUN chown -R root:root /root/.ssh \
    && chmod -R 700 /root/.ssh \
    && apk add --update nodejs \
                        openssh-client \
                        git \
                        socat \
    && npm update -g \
    && npm cache clear \
    && git clone git@bitbucket.org:wodby/dashboard-agent.git /srv/app \
    && cd /srv/app \
    && git checkout 4.1.2 \
    && cd /srv/app/app \
    && npm install --production \
    && npm cache clear \
    && apk del git openssh-client \
    && rm -rf /var/cache/apk/* /srv/app/.git
