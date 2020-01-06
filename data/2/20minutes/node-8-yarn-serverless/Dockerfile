FROM node:8.10-alpine

# python & aws cli
RUN apk -v --update add python py-pip groff less make gcc patch \
    && pip install --upgrade awscli==1.* \
    && apk -v --purge del py-pip \
    && rm /var/cache/apk/*

# yarn
RUN apk -v --update add curl bash gnupg ca-certificates git \
    # ensure local version of yarn from the source image are gone
    && rm -rf /usr/local/bin/yarn /usr/local/bin/yarnpkg \
    && curl -o- -L https://yarnpkg.com/install.sh | bash \
    && ln -s ~/.yarn/bin/yarn /usr/local/bin/yarn \
    && ln -s ~/.yarn/bin/yarnpkg /usr/local/bin/yarnpkg \
    && apk -v --purge del bash gnupg \
    && rm /var/cache/apk/*

# serverless & check for versions
RUN npm install -g serverless@1.57.0 \
    && serverless -v \
    && node -v \
    && yarn --version

CMD [ "node" ]
