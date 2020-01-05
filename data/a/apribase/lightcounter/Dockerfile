FROM apribase/debian-jp
MAINTAINER apribase

#### create user

RUN groupadd -g 8001 lightcounter
RUN useradd -d /srv/lightcounter -m -g lightcounter -u 8001 lightcounter
RUN chown -R lightcounter:lightcounter /srv/lightcounter

#### add lightcounter binary

ADD dist/lightcounter.js /srv/lightcounter/lightcounter.js
ADD node_modules /srv/lightcounter/node_modules
RUN chown -R lightcounter:lightcounter /srv/lightcounter

#### install node

USER lightcounter
WORKDIR /srv/lightcounter

RUN mkdir -p /srv/lightcounter/app
RUN wget http://nodejs.org/dist/v0.10.31/node-v0.10.31-linux-x64.tar.gz
RUN tar zxf node-v0.10.31-linux-x64.tar.gz -C /srv/lightcounter/app/
RUN rm -f node-v0.10.31-linux-x64.tar.gz

#### run

EXPOSE 8001

RUN mkdir -p /srv/lightcounter/var
ENV NODE_ENV production
CMD ["/srv/lightcounter/app/node-v0.10.31-linux-x64/bin/node", "/srv/lightcounter/lightcounter.js"]

