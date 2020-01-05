FROM node
LABEL maintainer="Thomas de Saint Exupery <incoming+stexthomas-vuepress-10449128-issue-@incoming.gitlab.com>"

COPY package.json yarn.lock /srv/

WORKDIR /srv

RUN yarn

COPY docs /srv-init/
COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
CMD ["dev"]

