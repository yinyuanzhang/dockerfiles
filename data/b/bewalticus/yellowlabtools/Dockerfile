FROM    node:6.14.3

# last commit=v1.12.0
ENV     VERSION=phantomas-timeout

WORKDIR /usr/src/ylt

RUN     npm install -g node-gyp \
        && npm install -g grunt-cli \
        && git clone https://github.com/Bewalticus/YellowLabTools.git -b ${VERSION} . \
        && npm install \
        && grunt build

EXPOSE  8383

ENV     NODE_ENV=production
CMD     ["node", "bin/server.js"]
