FROM docker:latest

LABEL org.label-schema.vcs-url=https://github.com/sdelements/gitlab-ci-dockerjs-runner org.label-schema.vendor=sdelements org.label-schema.name=gitlab-ci-dockerjs-runner

RUN echo "http://dl-3.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && apk add --update --no-cache python py-pip python-dev nodejs\<9 npm git openssh curl make gcc g++ linux-headers binutils-gold gnupg libstdc++ && pip install docker-compose && pip install virtualenv
RUN npm install -g n yarn

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["sh"]
