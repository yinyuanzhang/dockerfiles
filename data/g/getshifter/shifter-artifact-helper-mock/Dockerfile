FROM node:10-alpine
LABEL maintainer="sawanoboriyu@higanworks.com"

ADD package.json /srv/code/package.json
WORKDIR /srv/code
RUN yarn install
ADD . /srv/code
ENTRYPOINT [ "yarn" ]
# start / start404 / start500

EXPOSE 3000
CMD ["start"]
