FROM node:argon

RUN apt-get -y update && \
  apt-get -y --no-install-recommends install \
  nginx

ENV APP_ENV=development

# Update NPM
RUN npm --user root --unsafe-perm true install npm -g

ADD ./docker/nginx/nginx.conf /etc/nginx/nginx.conf
ADD ./docker/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf
ADD package.json /tmp/package.json

WORKDIR /var/www/html

ADD . /var/www/html

EXPOSE 80 443

CMD ["/bin/bash", "docker/run.sh"]
