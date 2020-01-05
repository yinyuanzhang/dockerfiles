FROM rustybrooks/flannelcat-base:latest

RUN apt-get -y update \
 && DEBIAN_FRONTEND=noninteractive apt-get -yq install curl apt-utils \
 && curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash - \
 && apt-get install -y nodejs

COPY . /srv/src
WORKDIR /srv/src/ui/app
RUN npm install
RUN npm run build

ENTRYPOINT /srv/src/ui/entrypoint.sh
