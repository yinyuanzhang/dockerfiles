FROM node:6.3.0

EXPOSE 80

RUN \
  apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y nginx build-essential && \
  mkdir -p /app

ADD nginx.conf /etc/nginx/sites-available/adevav

WORKDIR /app

ADD . /app

RUN \
  ln -s /etc/nginx/sites-available/adevav /etc/nginx/sites-enabled/adevav && \
  rm /etc/nginx/sites-enabled/default && \
  npm install

ENTRYPOINT npm run build && service nginx start && sleep infinity
